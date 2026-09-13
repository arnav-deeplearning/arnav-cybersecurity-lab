#!/usr/bin/env python3
"""
Static site builder.

Renders the Jinja2 templates in templates/ into plain HTML files at the
repo root so GitHub Pages can serve them directly, with zero
server-side code required at runtime.

Note: the real tools (e.g. tools/password-manager/) are separate,
standalone Python projects with their own README/tests -- this build
script only touches the site/ content that shows them off.

Usage:
    python build.py
"""
import html
import json
import re
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape
from markupsafe import Markup

import charts
from data import articles, content, flashcards, phishing_content, quiz, resources

ROOT = Path(__file__).parent
TEMPLATES_DIR = ROOT / "templates"
OUTPUT_DIR = ROOT

BASE_CONTEXT = {
    "site": content.SITE,
    "nav": content.NAV,
}


def _inline_html(text: str) -> Markup:
    """Escape text, then turn **bold** into <strong>. Safe to render directly."""
    escaped = html.escape(text.strip())
    return Markup(re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped))


def _parse_table(para: str) -> dict:
    lines = [ln.strip() for ln in para.strip().split("\n") if ln.strip()]

    def split_row(line):
        return [c.strip() for c in line.strip("|").split("|")]

    header = [_inline_html(c) for c in split_row(lines[0])]
    body_lines = lines[1:]
    if body_lines and re.fullmatch(r"[\s|:-]+", body_lines[0]):
        body_lines = body_lines[1:]
    rows = [[_inline_html(c) for c in split_row(line)] for line in body_lines]
    return {"type": "table", "header": header, "rows": rows}


def parse_body_blocks(body: str) -> list:
    """
    A tiny markdown-like format for article bodies, parsed into typed
    blocks for the template to render:
      - blank-line-separated paragraphs, with **bold** support
      - a paragraph starting with "> " becomes a pull-quote
      - a paragraph made of "| a | b |" lines becomes a table
      - a lone "[CHART:key]" line inserts a pre-generated, real-data SVG chart
    """
    blocks = []
    for para in body.strip().split("\n\n"):
        para = para.strip()
        if not para:
            continue
        chart_match = re.fullmatch(r"\[CHART:([a-z0-9\-]+)\]", para)
        if chart_match:
            key = chart_match.group(1)
            blocks.append({"type": "chart", "svg": Markup(charts.CHARTS[key]())})
        elif para.startswith("> "):
            blocks.append({"type": "quote", "text": _inline_html(para[2:].strip())})
        elif para.startswith("|"):
            blocks.append(_parse_table(para))
        else:
            blocks.append({"type": "paragraph", "text": _inline_html(para)})
    return blocks


def build():
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )

    flashcards_data = {"levels": flashcards.LEVELS, "categories": flashcards.FLASHCARD_CATEGORIES, "cards": flashcards.FLASHCARDS}
    quiz_data = {"levels": quiz.QUIZ_LEVELS, "categories": quiz.QUIZ_CATEGORIES, "questions": quiz.QUESTIONS}

    pages = [
        ("index.html", "index.html", {
            "profile": content.PROFILE,
            "course_timeline": content.COURSE_TIMELINE,
            "intro_paragraphs": content.INTRO_PARAGRAPHS,
            "why_this_matters": content.WHY_THIS_MATTERS,
            "ground_rules": content.GROUND_RULES,
            "featured_projects": [p for p in content.PROJECTS if p.get("status") == "live"][:3],
            "status_labels": content.STATUS_LABELS,
        }),
        ("apps.html", "apps.html", {
            "categories": content.CATEGORIES,
            "projects": content.PROJECTS,
            "status_labels": content.STATUS_LABELS,
        }),
        ("resources.html", "resources.html", {
            "resource_categories": resources.RESOURCE_CATEGORIES,
            "resources": resources.RESOURCES,
        }),
        ("articles.html", "articles.html", {
            "articles": articles.ARTICLES,
        }),
        ("password-manager.html", "password-manager.html", {
            "project": next(p for p in content.PROJECTS if p["id"] == "password-manager"),
        }),
        ("phishing-simulator.html", "phishing-simulator.html", {
            "project": next(p for p in content.PROJECTS if p["id"] == "phishing-simulator"),
            "templates_list": phishing_content.TEMPLATES,
            "phishing_json": json.dumps({
                "templates": phishing_content.TEMPLATES,
                "recipients": phishing_content.RECIPIENTS,
            }),
        }),
        ("flashcards.html", "flashcards.html", {
            "project": next(p for p in content.PROJECTS if p["id"] == "flashcards"),
            "levels": flashcards.LEVELS,
            "categories": flashcards.FLASHCARD_CATEGORIES,
            "cards_json": json.dumps(flashcards_data),
        }),
        ("quiz.html", "quiz.html", {
            "project": next(p for p in content.PROJECTS if p["id"] == "quiz"),
            "levels": quiz.QUIZ_LEVELS,
            "categories": quiz.QUIZ_CATEGORIES,
            "quiz_json": json.dumps(quiz_data),
        }),
        ("password-strength.html", "password-strength.html", {
            "project": next(p for p in content.PROJECTS if p["id"] == "password-strength"),
        }),
        ("cipher-challenge.html", "cipher-challenge.html", {
            "project": next(p for p in content.PROJECTS if p["id"] == "cipher-challenge"),
        }),
        ("security-checkup.html", "security-checkup.html", {
            "project": next(p for p in content.PROJECTS if p["id"] == "security-checkup"),
        }),
        ("spot-the-url.html", "spot-the-url.html", {
            "project": next(p for p in content.PROJECTS if p["id"] == "spot-the-url"),
        }),
    ]

    # The timeline chart needs live data (content.COURSE_TIMELINE), so it's
    # registered here rather than as a zero-arg entry in charts.CHARTS.
    charts.CHARTS["course-timeline"] = lambda: charts.course_timeline_diagram(content.COURSE_TIMELINE)

    all_articles = sorted(articles.ARTICLES, key=lambda a: a["date"])
    for i, article in enumerate(all_articles):
        prev_article = all_articles[i - 1] if i > 0 else None
        next_article = all_articles[i + 1] if i + 1 < len(all_articles) else None
        pages.append((
            "article.html",
            f"article-{article['id']}.html",
            {
                "article": article,
                "blocks": parse_body_blocks(article["body"]),
                "prev_article": prev_article,
                "next_article": next_article,
            },
        ))

    for template_name, output_name, extra_context in pages:
        template = env.get_template(template_name)
        context = {**BASE_CONTEXT, **extra_context, "active_page": output_name}
        html_out = template.render(**context)
        out_path = OUTPUT_DIR / output_name
        out_path.write_text(html_out, encoding="utf-8")
        print(f"built {out_path.relative_to(ROOT)}")


if __name__ == "__main__":
    build()
