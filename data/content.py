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
    {"label": "Projects", "href": "index.html"},
    {"label": "About", "href": "about.html"},
]

CATEGORIES = [
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
        "status": "coming-soon",
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
