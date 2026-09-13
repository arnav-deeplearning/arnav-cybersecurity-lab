"""
Inline SVG chart/diagram generators for articles.

Every number in these charts is computed from real data already living
elsewhere in this repo (the phishing simulator's own formula, the real
course timeline) or is a widely-reported public figure cited in the
article's own text -- nothing here is invented to make a chart look
nicer.

Each function returns a raw SVG string sized to fill its container.
Colors use CSS custom properties (var(--accent) etc.) so the charts
inherit the site's theme automatically.
"""
from data import phishing_content, resources


def _bar_chart(title: str, rows: list, unit: str = "%", max_value: float = None) -> str:
    """rows: list of (label, value, sublabel) tuples."""
    max_value = max_value or max(v for _, v, _ in rows) * 1.15
    bar_h = 34
    gap = 14
    top_pad = 36
    height = top_pad + len(rows) * (bar_h + gap)
    width = 620
    label_w = 190
    chart_w = width - label_w - 90

    bars = []
    for i, (label, value, sub) in enumerate(rows):
        y = top_pad + i * (bar_h + gap)
        bar_len = max(4, (value / max_value) * chart_w)
        bars.append(f'''
          <text x="0" y="{y + bar_h / 2 + 5}" fill="var(--text)" font-size="13" font-family="var(--font)">{label}</text>
          <rect x="{label_w}" y="{y}" width="{chart_w}" height="{bar_h}" rx="6" fill="var(--bg)" stroke="var(--border)"/>
          <rect x="{label_w}" y="{y}" width="{bar_len:.1f}" height="{bar_h}" rx="6" fill="var(--accent)"/>
          <text x="{label_w + chart_w + 10}" y="{y + bar_h / 2 + 5}" fill="var(--text)" font-size="13" font-weight="700" font-family="var(--font-mono)">{value:g}{unit}</text>
          <text x="{label_w}" y="{y + bar_h + 12}" fill="var(--text-muted)" font-size="10.5" font-family="var(--font)">{sub}</text>
        ''')

    return f'''<svg viewBox="0 0 {width} {height + 14}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{title}">
      <text x="0" y="18" fill="var(--text)" font-size="14" font-weight="700" font-family="var(--font)">{title}</text>
      <g>{''.join(bars)}</g>
    </svg>'''


def phishing_click_rate_chart() -> str:
    """
    Real expected click rate per template, computed with the exact
    same formula as tools/phishing-simulator/simulate.py:
        click_chance = clamp(susceptibility * (0.5 + difficulty))
    averaged across the same synthetic recipient pool. This is the
    true expected value, not a random sample -- reproducible from the
    data already in data/phishing_content.py.
    """
    rows = []
    for t in phishing_content.TEMPLATES:
        chances = [
            min(1.0, max(0.0, r["susceptibility"] * (0.5 + t["difficulty"])))
            for r in phishing_content.RECIPIENTS
        ]
        avg_pct = round((sum(chances) / len(chances)) * 100, 1)
        rows.append((t["subject"][:30] + ("…" if len(t["subject"]) > 30 else ""), avg_pct, f'Difficulty {t["difficulty"]:.2f}'))
    rows.sort(key=lambda r: r[1], reverse=True)
    return _bar_chart("Expected click rate by template (my simulator's own formula)", rows, unit="%")


def breach_scale_chart() -> str:
    """Widely-reported public figures, cited in the article text itself."""
    rows = [
        ("Equifax (2017)", 147, "million people affected"),
        ("Target (2013)", 40, "million card numbers stolen"),
    ]
    return _bar_chart("Records exposed, in millions (publicly reported figures)", rows, unit="M")


def course_timeline_diagram(timeline: list) -> str:
    width = 640
    height = 150
    n = len(timeline)
    step = (width - 80) / (n - 1)
    dots = []
    for i, item in enumerate(timeline):
        x = 40 + i * step
        dots.append(f'''
          <circle cx="{x}" cy="60" r="7" fill="{"var(--accent)" if i == n - 1 else "var(--text-muted)"}"/>
          <text x="{x}" y="90" fill="var(--text)" font-size="12" font-weight="700" text-anchor="middle" font-family="var(--font)">{item['grade']}</text>
          <text x="{x}" y="106" fill="var(--text-muted)" font-size="10.5" text-anchor="middle" font-family="var(--font)">{item['year']}</text>
          <foreignObject x="{x - step/2 + 4}" y="118" width="{step - 8}" height="34">
            <div xmlns="http://www.w3.org/1999/xhtml" style="font-size:10.5px;color:var(--text-muted);text-align:center;font-family:var(--font);line-height:1.3;">{item['course']}</div>
          </foreignObject>
        ''')
    line = f'<line x1="40" y1="60" x2="{40 + (n-1)*step}" y2="60" stroke="var(--border)" stroke-width="2"/>'
    return f'''<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="My course timeline">
      {line}
      {''.join(dots)}
    </svg>'''


def cia_triad_diagram() -> str:
    return '''<svg viewBox="0 0 500 320" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="CIA triad diagram">
      <polygon points="250,30 460,290 40,290" fill="none" stroke="var(--border)" stroke-width="2"/>
      <circle cx="250" cy="70" r="46" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="2"/>
      <text x="250" y="65" text-anchor="middle" fill="var(--accent)" font-size="14" font-weight="700" font-family="var(--font)">Confidentiality</text>
      <text x="250" y="82" text-anchor="middle" fill="var(--text-muted)" font-size="10" font-family="var(--font)">Only the right people see it</text>

      <circle cx="105" cy="255" r="46" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="2"/>
      <text x="105" y="250" text-anchor="middle" fill="var(--accent)" font-size="14" font-weight="700" font-family="var(--font)">Integrity</text>
      <text x="105" y="267" text-anchor="middle" fill="var(--text-muted)" font-size="10" font-family="var(--font)">Nothing was tampered with</text>

      <circle cx="395" cy="255" r="46" fill="var(--accent-soft)" stroke="var(--accent)" stroke-width="2"/>
      <text x="395" y="250" text-anchor="middle" fill="var(--accent)" font-size="14" font-weight="700" font-family="var(--font)">Availability</text>
      <text x="395" y="267" text-anchor="middle" fill="var(--text-muted)" font-size="10" font-family="var(--font)">Accessible when needed</text>
    </svg>'''


def network_flow_diagram() -> str:
    return '''<svg viewBox="0 0 640 160" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Basic network flow diagram">
      <g font-family="var(--font)" font-size="12">
        <rect x="10" y="55" width="110" height="50" rx="8" fill="var(--bg)" stroke="var(--border)"/>
        <text x="65" y="85" text-anchor="middle" fill="var(--text)">Your device</text>

        <path d="M120 80 H180" stroke="var(--border)" stroke-width="2" marker-end="url(#arrow)"/>

        <rect x="180" y="55" width="110" height="50" rx="8" fill="var(--accent-soft)" stroke="var(--accent)"/>
        <text x="235" y="80" text-anchor="middle" fill="var(--accent)">Firewall</text>
        <text x="235" y="95" text-anchor="middle" fill="var(--text-muted)" font-size="9.5">allows/blocks by rule</text>

        <path d="M290 80 H350" stroke="var(--border)" stroke-width="2" marker-end="url(#arrow)"/>

        <rect x="350" y="55" width="110" height="50" rx="8" fill="var(--bg)" stroke="var(--border)"/>
        <text x="405" y="80" text-anchor="middle" fill="var(--text)">Router</text>
        <text x="405" y="95" text-anchor="middle" fill="var(--text-muted)" font-size="9.5">DNS lookup happens near here</text>

        <path d="M460 80 H520" stroke="var(--border)" stroke-width="2" marker-end="url(#arrow)"/>

        <rect x="520" y="55" width="110" height="50" rx="8" fill="var(--bg)" stroke="var(--border)"/>
        <text x="575" y="80" text-anchor="middle" fill="var(--text)">Internet</text>
      </g>
      <defs>
        <marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
          <path d="M0,0 L8,4 L0,8 Z" fill="var(--border)"/>
        </marker>
      </defs>
    </svg>'''


CHARTS = {
    "phishing-click-rates": phishing_click_rate_chart,
    "breach-scale": breach_scale_chart,
    "cia-triad": cia_triad_diagram,
    "network-flow": network_flow_diagram,
}
