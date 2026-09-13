"""
Content for the in-browser phishing-simulator demo page.

Mirrors tools/phishing-simulator/templates.py and recipients.py so the
site demo and the real Python tool tell the same story. Kept as a
separate, site-specific copy (plain dicts, JSON-serializable) rather
than importing across the tools/ boundary, since the site build and
the standalone tool are independent projects.
"""

TEMPLATES = [
    {
        "id": "password-expiring",
        "subject": "URGENT: Your NorthPeak Cloud password expires in 2 hours",
        "sender_name": "NorthPeak Cloud IT Support",
        "sender_address": "it-support@northpeak-cloud-alerts.com",
        "body": (
            "Dear User,\n\n"
            "Our records indicate that your password will expire in "
            "2 HOURS. To avoid losing access to your account, you must "
            "verify your identity immediately by clicking the link "
            "below.\n\n"
            "Failure to act will result in permanent account "
            "suspension.\n\n"
            "Thank you,\nNorthPeak Cloud IT Support Team"
        ),
        "link_text": "Verify My Account Now",
        "link_preview": "http://northpeak-cloud-alerts.com.secure-verify.ru/login",
        "red_flags": [
            "Generic greeting ('Dear User') instead of your actual name.",
            "Manufactured urgency ('2 HOURS', 'permanent suspension') to short-circuit careful thinking.",
            "Sender domain (northpeak-cloud-alerts.com) doesn't match the real company's actual domain.",
            "The link preview shows a completely different domain (.ru) than the sender's own domain -- a classic mismatch.",
            "Legitimate IT departments almost never threaten immediate account suspension over email.",
        ],
        "difficulty": 0.4,
    },
    {
        "id": "ceo-gift-card",
        "subject": "Quick favor?",
        "sender_name": "Alex Rivera (CEO)",
        "sender_address": "alex.rivera@northpeak-corp-office.com",
        "body": (
            "Hey,\n\n"
            "Are you at your desk? I'm stuck in back-to-back meetings "
            "and need a quick favor -- can you pick up a few gift cards "
            "for a client thank-you? I'll pay you back today. Let me "
            "know and I'll send the details.\n\n"
            "Thanks,\nAlex"
        ),
        "link_text": "Reply to Alex",
        "link_preview": "mailto:alex.rivera@northpeak-corp-office.com",
        "red_flags": [
            "Impersonates a real executive's name and role to borrow their authority (a technique called 'CEO fraud').",
            "The sender's actual email domain doesn't match the real company's domain -- always check, don't trust the display name alone.",
            "Deliberately vague and casual, hoping you won't ask verifying questions before you reply.",
            "Creates time pressure ('stuck in meetings', 'quick') to discourage picking up the phone to confirm.",
            "Any request involving gift cards or wire transfers should always be verified through a second channel (call them).",
        ],
        "difficulty": 0.7,
    },
    {
        "id": "prize-notification",
        "subject": "Congratulations! You've won a $500 gift card \U0001F389",
        "sender_name": "Rewards Team",
        "sender_address": "rewards@totally-real-prizes.net",
        "body": (
            "You have been randomly selected to receive a $500 gift "
            "card! This offer expires soon, so claim your prize before "
            "it's given to someone else.\n\n"
            "Click below to claim your reward now."
        ),
        "link_text": "Claim My Prize",
        "link_preview": "http://totally-real-prizes.net/claim?id=88213",
        "red_flags": [
            "You almost never win a contest you never entered.",
            "'Randomly selected' with no context of what for is a red flag on its own.",
            "Manufactured scarcity ('before it's given to someone else') is a classic pressure tactic.",
            "The domain name itself ('totally-real-prizes') is a good reminder that domain names can say anything -- they aren't proof of legitimacy.",
        ],
        "difficulty": 0.15,
    },
]

# Fictional, composite personas -- not real people.
RECIPIENTS = [
    {"name": "Jordan P. (test persona)", "role": "New Hire", "susceptibility": 0.7},
    {"name": "Priya S. (test persona)", "role": "Marketing", "susceptibility": 0.55},
    {"name": "Sam K. (test persona)", "role": "Sales", "susceptibility": 0.5},
    {"name": "Morgan T. (test persona)", "role": "Finance", "susceptibility": 0.45},
    {"name": "Casey R. (test persona)", "role": "Support", "susceptibility": 0.4},
    {"name": "Devon L. (test persona)", "role": "Engineering", "susceptibility": 0.25},
    {"name": "Aisha M. (test persona)", "role": "IT / Security", "susceptibility": 0.1},
]
