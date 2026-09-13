#!/usr/bin/env python3
"""
Phishing-awareness campaign simulator (fully synthetic -- sends no
real email to anyone; see simulate.py).

Usage:
    python cli.py list-templates
    python cli.py run <template-id> [--seed N] [--json]
"""
import argparse
import json
import sys

from simulate import run_campaign
from templates import TEMPLATES


def cmd_list_templates(args):
    for t in TEMPLATES:
        print(f"{t.id:20s} \"{t.subject}\"")
    return 0


def cmd_run(args):
    result = run_campaign(args.template_id, seed=args.seed)

    if args.json:
        print(json.dumps(result.to_dict(), indent=2))
        return 0

    print(f"Campaign: {result.template.subject}")
    print(f"From:     {result.template.sender_name} <{result.template.sender_address}>")
    print()
    for r in result.results:
        mark = "CLICKED " if r.clicked else "no click"
        print(f"  [{mark}] {r.recipient.name:28s} ({r.recipient.role})")
    print()
    print(f"Click rate: {result.click_rate * 100:.0f}% ({sum(1 for r in result.results if r.clicked)}/{len(result.results)})")
    print()
    print("Red flags this template contains:")
    for flag in result.template.red_flags:
        print(f"  - {flag}")
    return 0


def build_parser():
    parser = argparse.ArgumentParser(description="Synthetic phishing-awareness campaign simulator.")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("list-templates", help="List available email templates").set_defaults(func=cmd_list_templates)

    run_parser = sub.add_parser("run", help="Run a simulated campaign against the synthetic recipient pool")
    run_parser.add_argument("template_id")
    run_parser.add_argument("--seed", type=int, default=None, help="Random seed, for reproducible results")
    run_parser.add_argument("--json", action="store_true", help="Print machine-readable JSON instead of text")
    run_parser.set_defaults(func=cmd_run)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
