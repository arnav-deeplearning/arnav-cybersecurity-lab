"""
Example phishing-awareness email templates.

These are entirely fictional -- fictional company names, fictional
domains, fictional senders. None of them impersonate a real brand,
because a *training* tool doesn't need to spoof a real company to
teach the underlying tactics, and doing so would risk the templates
being reused to actually impersonate that company.

Each template lists its own `red_flags`: the specific tells a trained
recipient should notice. That list is the actual teaching content --
the simulation's "click rate" is just a hook to get someone to read it.
"""
from dataclasses import dataclass, field


@dataclass(frozen=True)
class PhishingTemplate:
    id: str
    subject: str
    sender_name: str
    sender_address: str
    body: str
    link_text: str
    link_preview: str
    red_flags: list = field(default_factory=list)
    difficulty: float = 0.5  # 0 = obviously fake, 1 = very convincing


TEMPLATES = [
    PhishingTemplate(
        id="password-expiring",
        subject="URGENT: Your NorthPeak Cloud password expires in 2 hours",
        sender_name="NorthPeak Cloud IT Support",
        sender_address="it-support@northpeak-cloud-alerts.com",
        body=(
            "Dear User,\n\n"
            "Our records indicate that your password will expire in "
            "2 HOURS. To avoid losing access to your account, you must "
            "verify your identity immediately by clicking the link "
            "below.\n\n"
            "Failure to act will result in permanent account "
            "suspension.\n\n"
            "Thank you,\nNorthPeak Cloud IT Support Team"
        ),
        link_text="Verify My Account Now",
        link_preview="http://northpeak-cloud-alerts.com.secure-verify.ru/login",
        red_flags=[
            "Generic greeting ('Dear User') instead of your actual name.",
            "Manufactured urgency ('2 HOURS', 'permanent suspension') to "
            "short-circuit careful thinking.",
            "Sender domain (northpeak-cloud-alerts.com) doesn't match "
            "the real company's actual domain.",
            "The link preview shows a completely different domain "
            "(.ru) than the sender's own domain -- a classic mismatch.",
            "Legitimate IT departments almost never threaten immediate "
            "account suspension over email.",
        ],
        difficulty=0.4,
    ),
    PhishingTemplate(
        id="ceo-gift-card",
        subject="Quick favor?",
        sender_name="Alex Rivera (CEO)",
        sender_address="alex.rivera@northpeak-corp-office.com",
        body=(
            "Hey,\n\n"
            "Are you at your desk? I'm stuck in back-to-back meetings "
            "and need a quick favor -- can you pick up a few gift cards "
            "for a client thank-you? I'll pay you back today. Let me "
            "know and I'll send the details.\n\n"
            "Thanks,\nAlex"
        ),
        link_text="Reply to Alex",
        link_preview="mailto:alex.rivera@northpeak-corp-office.com",
        red_flags=[
            "Impersonates a real executive's name and role to borrow "
            "their authority (a technique called 'CEO fraud').",
            "The sender's actual email domain doesn't match the real "
            "company's domain -- always check, don't trust the display "
            "name alone.",
            "Deliberately vague and casual, hoping you won't ask "
            "verifying questions before you reply.",
            "Creates time pressure ('stuck in meetings', 'quick') to "
            "discourage picking up the phone to confirm.",
            "Any request involving gift cards or wire transfers should "
            "always be verified through a second channel (call them).",
        ],
        difficulty=0.7,
    ),
    PhishingTemplate(
        id="prize-notification",
        subject="Congratulations! You've won a $500 gift card 🎉",
        sender_name="Rewards Team",
        sender_address="rewards@totally-real-prizes.net",
        body=(
            "You have been randomly selected to receive a $500 gift "
            "card! This offer expires soon, so claim your prize before "
            "it's given to someone else.\n\n"
            "Click below to claim your reward now."
        ),
        link_text="Claim My Prize",
        link_preview="http://totally-real-prizes.net/claim?id=88213",
        red_flags=[
            "You almost never win a contest you never entered.",
            "'Randomly selected' with no context of what for is a red "
            "flag on its own.",
            "Manufactured scarcity ('before it's given to someone "
            "else') is a classic pressure tactic.",
            "The domain name itself ('totally-real-prizes') is a good "
            "reminder that domain names can say anything -- they aren't "
            "proof of legitimacy.",
        ],
        difficulty=0.15,
    ),
]

TEMPLATES_BY_ID = {t.id: t for t in TEMPLATES}
