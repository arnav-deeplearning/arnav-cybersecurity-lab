# arnav-cybersecurity-lab

A hands-on cybersecurity learning log, organized into three areas:
**defensive security (blue team)**, **security tool development**, and
**white-hat / offensive security education** (sandboxed only).

Live site: https://arnav-deeplearning.github.io/arnav-cybersecurity-lab/

## Repo layout

```
data/content.py       -> all editable site content (projects, categories)
templates/             -> Jinja2 templates (base.html + one per page)
static/                -> CSS, JS for the site
build.py               -> renders templates + data into HTML at repo root
index.html, about.html, password-manager.html
                       -> generated site output (committed, served by GitHub Pages)

tools/                 -> real, standalone tools (each is its own project
                          with its own README/tests, not part of the
                          Jinja2-rendered site)
  password-manager/    -> Python CLI password manager, AES-256-GCM
```

## Building the site

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python build.py
```

## Adding a new project card

Edit `PROJECTS` in `data/content.py`, then re-run `python build.py`. Use
`"status": "live"` only once there's a real, working tool and (ideally)
a detail page + demo to link to -- `"coming-soon"` and `"hands-on"` are
for anything not built yet.

## The tools

Each subfolder under `tools/` is a real, independent project with its
own `requirements.txt`, `README.md`, and (where it makes sense) tests.
See [`tools/password-manager/README.md`](tools/password-manager/README.md)
for the first one.

## Ground rules for this project

- Home network tools (the network monitor, the firewall) only ever run
  against this lab's own network -- never anyone else's.
- Any offensive-security practice happens exclusively on sandboxed
  platforms built for that purpose (VulnHub, Hack The Box), never
  against real third-party systems.
- The phishing-simulator demo is a fully synthetic sandbox (fake inbox,
  fake recipients) -- it does not send real email to real people.
