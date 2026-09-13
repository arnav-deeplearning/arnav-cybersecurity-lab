"""
Simulation engine for the phishing-awareness demo.

Important: there is no networking code anywhere in this tool -- no
smtplib, no requests, no sockets. It only ever runs a statistical
simulation over the synthetic recipients in recipients.py. That's a
deliberate structural choice, not an oversight: this tool is
incapable of sending a real email to a real person, by construction.

The "click" for each synthetic recipient is a weighted coin flip based
on that recipient's fixed susceptibility and the template's difficulty
(an easier-to-spot template lowers everyone's effective click chance;
a more convincing one raises it).
"""
import random
from dataclasses import dataclass

from recipients import SYNTHETIC_RECIPIENTS, SyntheticRecipient
from templates import TEMPLATES_BY_ID, PhishingTemplate


@dataclass
class RecipientResult:
    recipient: SyntheticRecipient
    clicked: bool
    click_chance_used: float


@dataclass
class CampaignResult:
    template: PhishingTemplate
    results: list

    @property
    def click_rate(self) -> float:
        if not self.results:
            return 0.0
        clicked = sum(1 for r in self.results if r.clicked)
        return clicked / len(self.results)

    def to_dict(self) -> dict:
        return {
            "template_id": self.template.id,
            "subject": self.template.subject,
            "click_rate": round(self.click_rate, 3),
            "recipients": [
                {
                    "name": r.recipient.name,
                    "role": r.recipient.role,
                    "clicked": r.clicked,
                }
                for r in self.results
            ],
        }


def run_campaign(template_id: str, seed: int | None = None) -> CampaignResult:
    if template_id not in TEMPLATES_BY_ID:
        raise ValueError(f"Unknown template '{template_id}'. Options: {list(TEMPLATES_BY_ID)}")

    template = TEMPLATES_BY_ID[template_id]
    rng = random.Random(seed)

    results = []
    for recipient in SYNTHETIC_RECIPIENTS:
        # A convincing (high-difficulty) template raises everyone's
        # effective click chance; an obvious one lowers it. Clamped to
        # [0, 1] since susceptibility and difficulty can compound.
        click_chance = min(1.0, max(0.0, recipient.susceptibility * (0.5 + template.difficulty)))
        clicked = rng.random() < click_chance
        results.append(RecipientResult(recipient=recipient, clicked=clicked, click_chance_used=click_chance))

    return CampaignResult(template=template, results=results)
