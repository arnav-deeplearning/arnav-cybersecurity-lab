"""
Central content store for the Cybersecurity Lab site.

Same pattern as the other sites: plain Python data structures rendered
by Jinja2 templates in build.py. Add a new project by editing PROJECTS
below -- no template changes needed.
"""

SITE = {
    "name": "Arnav Saravanakumar",
    "short_name": "Arnav",
    "title": "Cybersecurity Lab | Arnav's Security Projects",
    "tagline": "Learning security by building it: blue team, tool development, and white-hat basics.",
    "mission": (
        "A hands-on log of cybersecurity projects, from home network "
        "defense to writing real cryptography in Python. Everything "
        "here is either working code you can read, or a documented "
        "write-up of something actually built and tested -- nothing "
        "is aspirational marketing copy."
    ),
}

NAV = [
    {"label": "Home", "href": "index.html"},
    {"label": "Apps", "href": "apps.html"},
    {"label": "Articles", "href": "articles.html"},
    {"label": "Resources", "href": "resources.html"},
]

# ---------------------------------------------------------------------
# Homepage / "About" content
# ---------------------------------------------------------------------

PROFILE = {
    "grade": "Senior",
    "current_course": "AP Cybersecurity",
    "prior_course": "Cybersecurity I (elective)",
}

INTRO_PARAGRAPHS = [
    "Hi, I'm Arnav -- a high school senior currently taking AP "
    "Cybersecurity, after getting hooked during Cybersecurity I, the "
    "elective I took the year before. AP Cybersecurity is brand new -- "
    "College Board took it national this fall after a smaller pilot "
    "last year -- so my class is one of the first cohorts anywhere "
    "actually taking it, which is a fun thing to be early to. This "
    "site is where I keep track of what I'm learning and build small "
    "projects to actually test whether I understand a concept, "
    "instead of just being able to define it on a quiz.",

    "I got into this from a slightly different angle than most people "
    "expect. I'd already been building things with AI and writing "
    "software before I ever took a security class, and at some point "
    "the obvious question hit me: everything I was building could be "
    "broken into. That question -- how do you actually protect "
    "something you've built, and how do the people trying to break in "
    "actually think -- is what pulled me into cybersecurity for real.",

    "What I like about this field is that it's not one skill, it's a "
    "few very different ones stacked on top of each other: you need "
    "to understand how systems and networks actually work, you need "
    "to think like both the person defending something and the person "
    "trying to get past that defense, and you need enough math and "
    "code to actually build the tools instead of just reading about "
    "them. AP Cybersecurity is where I'm getting the structured, "
    "textbook version of all of that. This lab is where I try to turn "
    "it into something real.",

    "Everything you'll find here follows one rule: it's either real, "
    "working code with tests, or it's honestly labeled as 'not built "
    "yet.' Nothing on this site is aspirational marketing copy, and "
    "nothing here targets real systems without authorization -- "
    "practice happens on my own devices or on sandboxed platforms "
    "built for that purpose.",
]

WHY_THIS_MATTERS = [
    {
        "icon": "\U0001F9E9",
        "title": "It's genuinely interesting",
        "text": (
            "Security sits at the intersection of psychology (how "
            "scams actually work on people), math (cryptography), and "
            "systems thinking (how one small misconfiguration cascades "
            "into a breach). Almost nothing else I study touches all "
            "three."
        ),
    },
    {
        "icon": "\U0001F310",
        "title": "It matters beyond tech careers",
        "text": (
            "You don't need to be a 'computer person' to need security "
            "awareness -- every single career now runs on accounts, "
            "devices, and data. The self-assessment app on this site "
            "exists because I think this stuff is genuinely useful to "
            "know, not just to me."
        ),
    },
    {
        "icon": "\U0001F916",
        "title": "AI is changing both sides of it",
        "text": (
            "AI is making both attacks (better-written phishing, "
            "deepfakes) and defenses (faster log analysis, anomaly "
            "detection) more powerful at the same time. Combining my "
            "interest in AI with security feels like the right place "
            "to be paying attention right now."
        ),
    },
]

GROUND_RULES = [
    "Home network tools (the network monitor, the firewall) only ever "
    "run against this lab's own network -- never anyone else's.",
    "Any offensive-security practice happens exclusively on sandboxed "
    "platforms built for that purpose (like PicoCTF, TryHackMe, or "
    "OverTheWire), never against real third-party systems.",
    "The phishing-simulator and URL-safety apps are fully synthetic "
    "sandboxes -- fake recipients, fictional brands, no real email or "
    "real websites involved.",
    "Nothing on this site collects, stores, or transmits real personal "
    "data. Quiz scores, flashcard progress, and self-assessment "
    "answers all stay in your own browser's local storage.",
]

# ---------------------------------------------------------------------
# Apps grid
# ---------------------------------------------------------------------

CATEGORIES = [
    {"id": "learn", "label": "Learn & Practice", "icon": "\U0001F393"},
    {"id": "blue-team", "label": "Defensive Security (Blue Team)", "icon": "\U0001F6E1️"},
    {"id": "tool-dev", "label": "Security Tool Development", "icon": "\U0001F4BB"},
    {"id": "white-hat", "label": "Offensive Security & Education (White Hat)", "icon": "\U0001F310"},
]

# Status values:
#   "live"        -- real, working code + demo on this site
#   "coming-soon" -- planned, not built yet
#   "hands-on"    -- requires physical hardware or an external lab
#                    (Arnav does the work himself; this site documents
#                    it once it's done, it isn't something to "demo"
#                    in a browser)
PROJECTS = [
    {
        "id": "flashcards",
        "title": "Cybersecurity Flashcards",
        "category": "learn",
        "icon": "\U0001F0CF",
        "status": "live",
        "href": "flashcards.html",
        "description": (
            "Flip through core cybersecurity terms and concepts, "
            "leveled from Foundational to Advanced -- the same "
            "vocabulary AP Cybersecurity actually tests."
        ),
        "tags": ["Leveled", "Terminology"],
    },
    {
        "id": "quiz",
        "title": "Cybersecurity Knowledge Quiz",
        "category": "learn",
        "icon": "\U0001F3AF",
        "status": "live",
        "href": "quiz.html",
        "description": (
            "Test your knowledge and security awareness with leveled "
            "quizzes covering concepts, threats, and best practices."
        ),
        "tags": ["Leveled", "Awareness"],
    },
    {
        "id": "password-strength",
        "title": "Password Strength & Entropy Analyzer",
        "category": "learn",
        "icon": "\U0001F4AA",
        "status": "live",
        "href": "password-strength.html",
        "description": (
            "Type a password and see its real entropy in bits, an "
            "estimated crack time, and exactly why it's weak or "
            "strong. Nothing you type ever leaves your browser."
        ),
        "tags": ["Cryptography", "Interactive"],
    },
    {
        "id": "cipher-challenge",
        "title": "Cipher Challenge",
        "category": "learn",
        "icon": "\U0001F5DD️",
        "status": "live",
        "href": "cipher-challenge.html",
        "description": (
            "Crack a series of real encoded messages -- Caesar cipher, "
            "ROT13, Base64, and hex -- and learn how each one actually "
            "works after you solve it."
        ),
        "tags": ["Cryptography", "Puzzle"],
    },
    {
        "id": "security-checkup",
        "title": "Personal Security Checkup",
        "category": "learn",
        "icon": "✅",
        "status": "live",
        "href": "security-checkup.html",
        "description": (
            "A self-assessment of your own security habits -- "
            "passwords, 2FA, updates, backups -- that scores you and "
            "gives specific, non-judgmental next steps."
        ),
        "tags": ["Self-assessment", "Best practices"],
    },
    {
        "id": "spot-the-url",
        "title": "Spot the Fake URL",
        "category": "learn",
        "icon": "\U0001F50D",
        "status": "live",
        "href": "spot-the-url.html",
        "description": (
            "A fast-paced game: is this web address legitimate or a "
            "lookalike? Learn to spot typosquatting, fake subdomains, "
            "and other URL tricks."
        ),
        "tags": ["Game", "Phishing awareness"],
    },
    {
        "id": "password-manager",
        "title": "Local Password Manager",
        "category": "tool-dev",
        "icon": "\U0001F510",
        "status": "live",
        "href": "password-manager.html",
        "description": (
            "A command-line password manager written in Python with "
            "real AES-256-GCM encryption behind a master password -- "
            "no plaintext ever touches disk."
        ),
        "tags": ["Python", "AES-256", "Cryptography"],
    },
    {
        "id": "packet-scanner",
        "title": "Packet Sniffer / Scanner",
        "category": "tool-dev",
        "icon": "\U0001F4E1",
        "status": "coming-soon",
        "description": (
            "A lightweight network scanner using Python and Scapy to "
            "identify open ports and active devices on a local "
            "network."
        ),
        "tags": ["Python", "Scapy", "Networking"],
    },
    {
        "id": "encrypted-chat",
        "title": "Encrypted Chat Program",
        "category": "tool-dev",
        "icon": "\U0001F4AC",
        "status": "coming-soon",
        "description": (
            "A peer-to-peer chat app using RSA public/private key "
            "pairs for end-to-end encryption, so messages can't be "
            "read in transit."
        ),
        "tags": ["Python", "RSA", "E2EE"],
    },
    {
        "id": "log-dashboard",
        "title": "Log Analysis Dashboard",
        "category": "blue-team",
        "icon": "\U0001F4CA",
        "status": "coming-soon",
        "description": (
            "A dashboard that parses system logs and visually flags "
            "failed login attempts and other suspicious patterns."
        ),
        "tags": ["Blue team", "Log analysis"],
    },
    {
        "id": "phishing-simulator",
        "title": "Phishing Simulator (Sandbox Demo)",
        "category": "white-hat",
        "icon": "\U0001F3A3",
        "status": "live",
        "href": "phishing-simulator.html",
        "description": (
            "A fully synthetic demo of a phishing-awareness tool -- "
            "fake inbox, fake test recipients, real click-tracking "
            "dashboard. No real email is ever sent to a real person "
            "by this demo."
        ),
        "tags": ["Security awareness", "Sandbox only"],
    },
    {
        "id": "home-lab-monitor",
        "title": "Home Lab Network Monitor",
        "category": "blue-team",
        "icon": "\U0001F4E1",
        "status": "hands-on",
        "description": (
            "A Raspberry Pi running Zeek/Wireshark on the home "
            "network, alerting on unusual traffic or unrecognized "
            "devices. Write-up coming once it's set up."
        ),
        "tags": ["Zeek", "Raspberry Pi", "Home lab"],
    },
    {
        "id": "custom-firewall",
        "title": "Custom Firewall (pfSense/OPNsense)",
        "category": "blue-team",
        "icon": "\U0001F9F1",
        "status": "hands-on",
        "description": (
            "A dedicated open-source firewall segmenting the home "
            "network, isolating IoT devices from personal computers. "
            "Write-up coming once it's set up."
        ),
        "tags": ["pfSense", "Network segmentation"],
    },
    {
        "id": "vulnerability-writeups",
        "title": "Vulnerability Write-ups",
        "category": "white-hat",
        "icon": "\U0001F4DD",
        "status": "hands-on",
        "description": (
            "Technical write-ups documenting vulnerabilities found "
            "and patched in sandboxed environments like VulnHub and "
            "Hack The Box."
        ),
        "tags": ["VulnHub", "Hack The Box", "CTF"],
    },
]

STATUS_LABELS = {
    "live": "Live",
    "coming-soon": "Coming Soon",
    "hands-on": "In Progress (hands-on)",
}
