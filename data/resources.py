"""
Curated cybersecurity learning resources.

Every URL here was checked by actually fetching it and confirming it
resolves to the described content -- these are the same sources used
as background/context when writing this site's flashcards, quiz, and
articles. No fabricated or guessed links.
"""

RESOURCE_CATEGORIES = [
    {"id": "official", "label": "Official & Government"},
    {"id": "standards", "label": "Standards & Frameworks"},
    {"id": "nonprofit", "label": "Education Nonprofits"},
    {"id": "news", "label": "News & Journalism"},
    {"id": "tools", "label": "Practical Safety Tools"},
    {"id": "certs", "label": "Certifications & Learning Paths"},
    {"id": "practice", "label": "Hands-On Practice Platforms"},
]

RESOURCES = [
    {
        "name": "CISA / NICCS — Cybersecurity for Students",
        "url": "https://niccs.cisa.gov/audience/cybersecurity-students",
        "category": "official",
        "description": (
            "A page CISA (the federal Cybersecurity and Infrastructure "
            "Security Agency) built specifically for students -- career "
            "profiles, scholarship listings, competitions, and how to "
            "start building a cybersecurity path in high school."
        ),
    },
    {
        "name": "NIST Cybersecurity Framework",
        "url": "https://www.nist.gov/cyberframework",
        "category": "official",
        "description": (
            "The official home of NIST's Cybersecurity Framework (CSF "
            "2.0) -- the government-developed model (Govern, Identify, "
            "Protect, Detect, Respond, Recover) that real organizations "
            "use to structure their security programs."
        ),
    },
    {
        "name": "OWASP Top 10",
        "url": "https://owasp.org/Top10/",
        "category": "standards",
        "description": (
            "The industry-standard list of the most critical web "
            "application security risks, maintained by the nonprofit "
            "OWASP Foundation. Essential vocabulary for understanding "
            "how real apps actually get exploited."
        ),
    },
    {
        "name": "MITRE ATT&CK",
        "url": "https://attack.mitre.org/",
        "category": "standards",
        "description": (
            "A free, globally used knowledge base cataloging real-world "
            "attacker tactics and techniques (like phishing or "
            "credential dumping). Professional analysts use this exact "
            "framework -- it's a great way to see how attacks get "
            "classified in practice."
        ),
    },
    {
        "name": "National Cybersecurity Alliance (StaySafeOnline)",
        "url": "https://www.staysafeonline.org/",
        "category": "nonprofit",
        "description": (
            "A nonprofit that co-leads Cybersecurity Awareness Month "
            "with CISA, offering free articles, videos, and toolkits on "
            "personal cyber hygiene written for a general audience."
        ),
    },
    {
        "name": "(ISC)² Certified in Cybersecurity (CC)",
        "url": "https://www.isc2.org/certifications/cc",
        "category": "nonprofit",
        "description": (
            "An entry-level credential -- with free self-study "
            "resources -- from the nonprofit behind the CISSP. "
            "Explicitly designed for people with no prior experience, "
            "including students, making it a realistic near-term goal."
        ),
    },
    {
        "name": "Krebs on Security",
        "url": "https://krebsonsecurity.com/",
        "category": "news",
        "description": (
            "Brian Krebs' independent, investigative security "
            "journalism -- 16+ years of breaking real cybercrime and "
            "data-breach stories with primary-source reporting. A good "
            "site to follow to actually stay current."
        ),
    },
    {
        "name": "Have I Been Pwned",
        "url": "https://haveibeenpwned.com/",
        "category": "tools",
        "description": (
            "Troy Hunt's free breach-notification tool -- check whether "
            "your own email address has appeared in a known data "
            "breach. A hands-on, personally relevant way to see breach "
            "data instead of just reading about it."
        ),
    },
    {
        "name": "Google Safety Center",
        "url": "https://safety.google/",
        "category": "tools",
        "description": (
            "Google's consumer-facing hub explaining account security "
            "settings, privacy controls, and built-in protections -- "
            "practical guidance you can actually apply to your own "
            "accounts today."
        ),
    },
    {
        "name": "CompTIA Security+",
        "url": "https://www.comptia.org/certifications/security",
        "category": "certs",
        "description": (
            "The industry-standard entry-level security certification. "
            "Its exam objectives are essentially a well-structured "
            "syllabus of foundational cybersecurity topics, useful even "
            "if you're not taking the exam yet."
        ),
    },
    {
        "name": "SANS Cyber Aces",
        "url": "https://www.sans.org/cyberaces",
        "category": "certs",
        "description": (
            "Free, selected training modules from the SANS Institute -- "
            "Linux, Windows, and networking security fundamentals -- "
            "made publicly available at no cost."
        ),
    },
    {
        "name": "AP Cybersecurity (College Board)",
        "url": "https://apcentral.collegeboard.org/courses/ap-cybersecurity",
        "category": "certs",
        "description": (
            "The official course page for AP Cybersecurity, part of "
            "College Board's new AP Career Kickstart program -- "
            "developed with Cisco, launching nationally in fall 2026 "
            "with the first exam in May 2027. This is the actual course "
            "behind a lot of the content on this site."
        ),
    },
    {
        "name": "TryHackMe",
        "url": "https://tryhackme.com/",
        "category": "practice",
        "description": (
            "Browser-based, gamified hands-on security labs with guided "
            "beginner paths. No local setup required, which makes it a "
            "genuinely good first hands-on platform."
        ),
    },
    {
        "name": "OverTheWire: Bandit",
        "url": "https://overthewire.org/wargames/bandit/",
        "category": "practice",
        "description": (
            "A free, SSH-based wargame that teaches Linux and "
            "command-line fundamentals level by level. The classic "
            "starting point before attempting harder wargames."
        ),
    },
    {
        "name": "picoCTF",
        "url": "https://picoctf.org/",
        "category": "practice",
        "description": (
            "Carnegie Mellon University's free, beginner-friendly "
            "capture-the-flag platform covering cryptography, web "
            "exploitation, forensics, and reverse engineering."
        ),
    },
]
