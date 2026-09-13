# Phishing Awareness Simulator (Fully Synthetic)

Simulates a phishing-awareness campaign against a pool of **synthetic,
fictional recipients** — never real people, never a real email.

## Why it's structurally safe

This tool has **no networking code anywhere** — no `smtplib`, no
`requests`, no sockets. It only runs a statistical simulation over the
recipients in [`recipients.py`](recipients.py). It is incapable of
sending a real email to a real person, by construction, not just by
policy.

The email templates in [`templates.py`](templates.py) are entirely
fictional (fictional company, fictional domains) — they don't impersonate
any real brand, so they can't be reused to actually impersonate one.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install pytest  # only needed for tests; the tool itself has zero dependencies
```

## Usage

```bash
python cli.py list-templates
python cli.py run password-expiring --seed 3
python cli.py run ceo-gift-card --json
```

Each run prints (or emits as JSON) which synthetic personas "clicked,"
an overall click rate, and — the actual point of the tool — the list of
specific red flags that email contains, so the "click rate" hook leads
into the real lesson.

## How the simulation works

Each synthetic recipient has a fixed `susceptibility` (0–1), loosely
modeled on published security-awareness research showing newer/less
technical roles click more often than IT staff. Each template has a
`difficulty` (0–1): more convincing templates raise everyone's
effective click chance, obvious ones lower it. A campaign is just a
weighted coin flip per recipient — see [`simulate.py`](simulate.py).

## Tests

```bash
python -m pytest tests/ -v
```

Covers determinism under a fixed seed, that a more convincing template
produces a higher average click rate across many simulated runs than
an obvious one, and that the campaign report never contains anything
resembling a real email address or SMTP-sending code.
