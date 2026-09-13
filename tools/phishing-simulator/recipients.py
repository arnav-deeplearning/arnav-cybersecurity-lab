"""
Synthetic recipient pool for the phishing-awareness simulation.

These are fictional, composite personas -- not real people. Each has a
`susceptibility` in [0, 1] representing, for this simulation only, how
likely that persona is to click a phishing link before any training
(loosely modeled on published security-awareness research: newer /
less technical roles tend to have higher click rates than IT staff).
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class SyntheticRecipient:
    name: str
    role: str
    susceptibility: float


SYNTHETIC_RECIPIENTS = [
    SyntheticRecipient("Jordan P. (test persona)", "New Hire", 0.7),
    SyntheticRecipient("Priya S. (test persona)", "Marketing", 0.55),
    SyntheticRecipient("Sam K. (test persona)", "Sales", 0.5),
    SyntheticRecipient("Morgan T. (test persona)", "Finance", 0.45),
    SyntheticRecipient("Casey R. (test persona)", "Support", 0.4),
    SyntheticRecipient("Devon L. (test persona)", "Engineering", 0.25),
    SyntheticRecipient("Aisha M. (test persona)", "IT / Security", 0.1),
]
