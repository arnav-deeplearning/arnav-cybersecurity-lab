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
import json
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

from data import content, phishing_content

ROOT = Path(__file__).parent
TEMPLATES_DIR = ROOT / "templates"
OUTPUT_DIR = ROOT

BASE_CONTEXT = {
    "site": content.SITE,
    "nav": content.NAV,
}

PAGES = [
    ("index.html", "index.html", {
        "categories": content.CATEGORIES,
        "projects": content.PROJECTS,
        "status_labels": content.STATUS_LABELS,
    }),
    ("about.html", "about.html", {}),
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
]


def build():
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )

    for template_name, output_name, extra_context in PAGES:
        template = env.get_template(template_name)
        context = {**BASE_CONTEXT, **extra_context, "active_page": output_name}
        html = template.render(**context)
        out_path = OUTPUT_DIR / output_name
        out_path.write_text(html, encoding="utf-8")
        print(f"built {out_path.relative_to(ROOT)}")


if __name__ == "__main__":
    build()
