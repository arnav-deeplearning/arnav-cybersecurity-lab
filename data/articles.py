"""
Articles for the Articles page.

`body` is a tiny markdown-like format, parsed by build.py's
parse_body_blocks() into typed blocks:
  - blank-line-separated paragraphs, with **bold** support
  - a paragraph starting with "> " becomes a pull-quote
  - a paragraph made of "| a | b |" lines becomes a table
  - a lone "[CHART:key]" line inserts a pre-generated, real-data SVG
    chart (see charts.py -- CIA triad diagram, network flow diagram,
    the phishing simulator's own real click-rate math, the actual
    course timeline, and public breach-scale figures)

Dates are chosen to line up with when each topic was actually being
learned, per the real transcript: Cybersecurity I was grade 10
(2024-25), AP Computer Science Principles + AP Research were grade 11
(2025-26, no cyber class that year), and AP Cybersecurity is the
current grade 12 course (2026-27). Articles are written as if
published at the time, so earlier ones don't reference tools or
classes that didn't exist yet.
"""

ARTICLES = [
    {
        "id": "cia-triad-explained",
        "title": "The CIA Triad Isn't About Spies: Confidentiality, Integrity, Availability, Explained",
        "date": "2024-11-15",
        "read_time": "6 min read",
        "tags": ["Concepts", "Foundations"],
        "excerpt": (
            "It's the first thing every cybersecurity class teaches, "
            "and also the thing that quietly explains almost every "
            "security decision that follows it."
        ),
        "tldr": (
            "The CIA triad -- Confidentiality, Integrity, Availability -- "
            "is the three-question checklist behind almost every "
            "security decision. Once you see the pattern, you can't "
            "unsee it."
        ),
        "body": (
            "Every cybersecurity course I've taken starts with the same "
            "three letters: CIA. Not the agency -- the triad. "
            "Confidentiality, Integrity, Availability. It sounds like "
            "the kind of thing you memorize for a quiz and forget by "
            "December. I thought that too, until I noticed I couldn't "
            "stop using it to explain literally everything else in the "
            "course.\n\n"

            "[CHART:cia-triad]\n\n"

            "**Confidentiality** is the one people usually get "
            "immediately: information should only be accessible to "
            "people who are actually authorized to see it. Encrypting a "
            "file, requiring a password, restricting who can view a "
            "document -- all confidentiality controls. This is the part "
            "of security that maps most directly to the word "
            "'privacy.'\n\n"

            "**Integrity** is less intuitive at first. It's not about "
            "who can see data -- it's about whether the data is "
            "trustworthy. Has it been changed, accidentally or on "
            "purpose, since it was created? A grade in a school's "
            "database needs integrity: if someone could quietly edit "
            "it, the number stops meaning anything. This is why systems "
            "use things like hashes and checksums -- little "
            "mathematical fingerprints that change the instant even one "
            "character does.\n\n"

            "**Availability** is the one people forget exists until it "
            "doesn't. A system can be perfectly confidential and have "
            "flawless integrity and still fail completely if nobody who "
            "needs it can actually use it. This is exactly what a DDoS "
            "attack targets -- it doesn't steal anything or change "
            "anything, it just floods a system with traffic until real "
            "users can't get through.\n\n"

            "| Principle | Gets broken by | Common real fix |\n"
            "|---|---|---|\n"
            "| Confidentiality | Data exposure, weak access control | Encryption, least privilege |\n"
            "| Integrity | Tampering, corruption | Hashing, checksums, digital signatures |\n"
            "| Availability | DDoS, ransomware, hardware failure | Redundancy, backups, rate limiting |\n\n"

            "> Security isn't about maximizing all three at once. It's "
            "about deciding, deliberately, how much of each a specific "
            "system actually needs -- and accepting that pushing one up "
            "usually pushes another one down.\n\n"

            "The most confidential system imaginable -- locked in a "
            "vault, disconnected from everything -- has terrible "
            "availability. The most available system imaginable -- open "
            "to everyone, no authentication -- has zero confidentiality. "
            "That tension is basically the whole job.\n\n"

            "That reframing is honestly why the triad stuck with me. "
            "It's not a memorization exercise, it's a lens. Once you "
            "have it, you start looking at security news differently: "
            "instead of 'a company got hacked,' you start asking which "
            "part of the triad actually failed -- and that question "
            "usually tells you a lot about what should have been done "
            "differently."
        ),
        "sources": [
            {"name": "NIST Cybersecurity Framework", "url": "https://www.nist.gov/cyberframework"},
        ],
    },
    {
        "id": "networking-basics-explained",
        "title": "Networking Basics That Finally Made Sense (A Diagram Helped)",
        "date": "2025-02-20",
        "read_time": "5 min read",
        "tags": ["Concepts", "Networking"],
        "excerpt": (
            "Ports, DNS, firewalls -- I could define all of them on a "
            "quiz for weeks before I actually understood how they fit "
            "together. Drawing it out is what finally did it."
        ),
        "tldr": (
            "A request from your device to a website passes through a "
            "firewall, a router, and a DNS lookup before it ever "
            "leaves your network. Seeing that as a diagram made the "
            "vocabulary click in a way flashcards never did."
        ),
        "body": (
            "For the first few weeks of the networking unit in "
            "Cybersecurity I, I could define every term on command and "
            "still couldn't have explained what actually happens when "
            "you type a website into your browser. Firewall, port, DNS, "
            "router -- I had definitions for all of them floating "
            "around independently, with no picture connecting them.\n\n"

            "What fixed it, embarrassingly, was just drawing the path a "
            "request actually takes.\n\n"

            "[CHART:network-flow]\n\n"

            "Your device doesn't talk to the internet directly. The "
            "request first hits your **firewall**, which checks it "
            "against a set of rules before deciding whether it's even "
            "allowed to continue -- think of it as a bouncer checking a "
            "list, not a lock on a door. Assuming it's allowed through, "
            "it reaches your **router**, and somewhere around there a "
            "**DNS** lookup happens: the human-readable name you typed "
            "(like a website's address) gets translated into the actual "
            "numerical IP address computers use to find each other. "
            "Only after all of that does anything leave for the open "
            "internet.\n\n"

            "Ports were the other piece that finally clicked once I had "
            "the picture. A port isn't a physical thing -- it's a "
            "number that tells a device which specific service a piece "
            "of traffic is meant for, the same way an apartment number "
            "tells mail which unit in a building to go to.\n\n"

            "| Port | Used for |\n"
            "|---|---|\n"
            "| 22 | SSH -- secure remote command-line access |\n"
            "| 80 | HTTP -- unencrypted web traffic |\n"
            "| 443 | HTTPS -- encrypted web traffic |\n"
            "| 53 | DNS -- domain name lookups |\n"
            "| 3389 | RDP -- remote desktop access |\n\n"

            "> A firewall blocking everything except the ports a "
            "service actually needs isn't paranoia. It's just refusing "
            "to leave every apartment door in the building unlocked "
            "because a couple of units need mail delivered.\n\n"

            "None of this required understanding any math or writing "
            "any code -- it just required a diagram instead of a "
            "flashcard. I've noticed that's true for a lot of "
            "networking concepts: the vocabulary is dense, but the "
            "actual mechanism, once you can see it, is usually pretty "
            "simple."
        ),
    },
    {
        "id": "five-password-habits",
        "title": "5 Password Habits That Are Quietly Wrecking Your Security",
        "date": "2025-05-09",
        "read_time": "5 min read",
        "tags": ["Best Practices", "Practical"],
        "excerpt": (
            "None of these require buying anything or learning to "
            "code. They just require breaking a few habits you "
            "probably don't think about twice."
        ),
        "tldr": (
            "Length beats complexity, reuse is the single biggest "
            "risk, and MFA is the highest-leverage five minutes you'll "
            "spend on security all year."
        ),
        "body": (
            "End-of-year review in Cybersecurity I meant revisiting a "
            "lot of material, and the password unit is the one I keep "
            "coming back to, because it's the rare cybersecurity topic "
            "where the advice is genuinely actionable in the next ten "
            "minutes, not 'buy a firewall' actionable.\n\n"

            "**1. Reusing the same password everywhere.** This is the "
            "big one. It doesn't matter how strong your password is if "
            "you use it on ten different sites and one of them gets "
            "breached -- and someone eventually will. Attackers "
            "specifically take leaked passwords from one breach and try "
            "them on other sites. It's called credential stuffing, and "
            "it works embarrassingly often because of exactly this "
            "habit.\n\n"

            "**2. Treating length as optional.** A shorter password "
            "with symbols swapped in ('P@ssw0rd!') is not as strong as "
            "people assume. Length beats complexity almost every time, "
            "because of how the math actually works -- adding "
            "characters multiplies the number of guesses needed far "
            "faster than adding symbol variety does.\n\n"

            "| Password | Length | Character types | Estimated entropy |\n"
            "|---|---|---|---|\n"
            "| password | 8 | lowercase only | ~38 bits |\n"
            "| P@ssw0rd! | 9 | upper, lower, digit, symbol | ~59 bits |\n"
            "| Tr0ub4dor&3 | 11 | upper, lower, digit, symbol | ~72 bits |\n"
            "| correcthorsebatterystaple | 26 | lowercase only | ~118 bits |\n\n"

            "That's not a typo -- four random unrelated lowercase words "
            "strung together outscores a short password stuffed with "
            "symbols, and it's easier to actually remember. (Entropy "
            "here is calculated as length times log base 2 of the "
            "character set size -- a standard way to estimate worst-case "
            "brute-force difficulty. It's a rough model, not gospel: a "
            "real attacker tries common words and patterns first, which "
            "is exactly why 'password' scores 38 bits on paper but "
            "would actually fall in under a second.)\n\n"

            "**3. Skipping MFA because it's 'annoying.'** I get it, "
            "typing in a six-digit code is one more step. But MFA is "
            "one of the single highest-leverage things you can do -- "
            "it means a leaked password alone usually isn't enough to "
            "get into your account. Turn it on for email and banking "
            "first if you do nothing else.\n\n"

            "**4. Never checking if you've already been breached.** "
            "There's a free, legitimate tool where you can check if "
            "your email shows up in a known data breach. I checked mine "
            "expecting nothing and found two breaches I'd never heard "
            "about. Takes thirty seconds, and it's a genuinely useful "
            "wake-up call.\n\n"

            "**5. Writing passwords down somewhere insecure -- or "
            "keeping them all in your head.** Neither extreme works "
            "well. A sticky note on a monitor is an obvious problem, "
            "but so is refusing to use a password manager and then "
            "reusing one 'good' password everywhere because it's the "
            "only one you can remember.\n\n"

            "None of this requires being a security expert. It requires "
            "about twenty minutes and a willingness to admit your "
            "current habits are probably worse than you think. Mine "
            "were."
        ),
        "sources": [
            {"name": "Have I Been Pwned", "url": "https://haveibeenpwned.com/"},
        ],
    },
    {
        "id": "red-team-vs-blue-team",
        "title": "Red Team vs. Blue Team: Which Path Fits You?",
        "date": "2025-10-21",
        "read_time": "6 min read",
        "tags": ["Careers", "For Students"],
        "excerpt": (
            "I don't have a cybersecurity class on my schedule this "
            "year, which turned out to be a pretty good excuse to "
            "actually think about where this is all heading."
        ),
        "tldr": (
            "Red team breaks things (with permission) to find "
            "weaknesses first. Blue team builds and defends the actual "
            "systems. Both reward completely different kinds of "
            "thinking -- try both before picking a lane."
        ),
        "body": (
            "Funny timing: the year I don't have an actual "
            "cybersecurity class on my schedule -- AP Computer Science "
            "Principles and AP Research took its spot -- is the year "
            "I've had the most time to actually think about where this "
            "interest is heading long-term. If you tell people you're "
            "into cybersecurity, a common next question is 'so, do you "
            "want to be a hacker?' The honest answer is that 'hacker' "
            "isn't really one job, and the field usually splits into "
            "two broad camps: red team and blue team.\n\n"

            "| | Focus | Rewards | Try it (legally) |\n"
            "|---|---|---|---|\n"
            "| Red team | Finding weaknesses before attackers do | Creative, lateral thinking | picoCTF, TryHackMe |\n"
            "| Blue team | Detecting, containing, and recovering | Patient, methodical thinking | Log-analysis practice, home labs |\n"
            "| Purple team | Both sides sharing findings in real time | Communication + both skill sets | Usually grown into, not started in |\n\n"

            "**Red team** is offensive security: people (with explicit, "
            "legal authorization) who try to break into systems the way "
            "a real attacker would, to find weaknesses before an actual "
            "attacker does. Penetration testers, red team operators, "
            "bug bounty hunters -- this is the side that gets the "
            "dramatic movie treatment, and honestly, some of it is "
            "genuinely close to a puzzle-solving game. Platforms like "
            "picoCTF and TryHackMe let you try this style of thinking "
            "legally and safely, working through deliberately built "
            "challenges instead of real systems.\n\n"

            "**Blue team** is defensive security: the people building "
            "and maintaining the actual defenses, monitoring systems "
            "for suspicious activity, responding when something does "
            "go wrong, and doing the unglamorous but essential work of "
            "keeping patches current and configurations sane. It's less "
            "cinematic and, in my opinion, underrated -- most "
            "organizations need far more blue team capacity than red "
            "team, and actually stopping or containing a real incident "
            "is a genuinely high-stakes skill.\n\n"

            "> Red team work rewards creative, lateral thinking: what's "
            "the weird, unintended way I could misuse this? Blue team "
            "work rewards patient, methodical thinking: which one log "
            "entry, out of a million, doesn't belong?\n\n"

            "Neither is 'better.' They're just different muscles, and "
            "I don't think you need to commit early. My plan for this "
            "year and next is to keep poking at both through practice "
            "platforms and small projects, rather than deciding right "
            "now which one I'm 'supposed' to be."
        ),
        "sources": [
            {"name": "picoCTF", "url": "https://picoctf.org/"},
            {"name": "TryHackMe", "url": "https://tryhackme.com/"},
            {"name": "OverTheWire: Bandit", "url": "https://overthewire.org/wargames/bandit/"},
        ],
    },
    {
        "id": "what-ap-research-taught-me",
        "title": "What AP Research Taught Me About Picking a Fight With My Own Argument",
        "date": "2026-04-25",
        "read_time": "6 min read",
        "tags": ["Research", "Skills"],
        "excerpt": (
            "The most useful class I took this year didn't have "
            "'cyber' anywhere in the title."
        ),
        "tldr": (
            "AP Research isn't about being right. It's about proving "
            "you checked whether you're right -- a habit that turns "
            "out to matter just as much for evaluating a security "
            "claim as it does for a research paper."
        ),
        "body": (
            "AP Research is the second half of the AP Capstone program, "
            "after AP Seminar the year before, and it's the most "
            "unusual class I've taken. You pick your own research "
            "question, spend most of a year investigating it, and "
            "defend it in front of people whose entire job in that room "
            "is to find the hole in your argument. There's no "
            "cybersecurity in the syllabus at all. I'd still argue it's "
            "shaped how I think about this field more than almost "
            "anything else I've taken.\n\n"

            "The first real lesson was humbling: before you get to "
            "argue anything, you have to prove someone hasn't already "
            "answered your question, and answered it better than you "
            "were about to. That means actually reading the existing "
            "research, not skimming the first three results that "
            "confirm what you already believed. It is much less "
            "satisfying than jumping straight to your own idea, and it "
            "is also the only way to avoid confidently reinventing "
            "something that's been known for a decade.\n\n"

            "> A source that agrees with you isn't automatically a good "
            "source. A source that would let you check its work is.\n\n"

            "The second lesson was about being honest regarding what "
            "your own evidence actually supports, especially when it's "
            "less than you hoped. It's tempting to stretch a small, "
            "messy result into a bigger claim than it can carry. My "
            "research advisor's favorite question, asked about nearly "
            "every claim in every draft, was some version of 'what "
            "would have to be true for this to be wrong?' Answering "
            "that honestly, instead of defensively, turned out to be "
            "the actual skill being taught.\n\n"

            "That question transfers almost perfectly to security. When "
            "a headline says a company got breached because of some "
            "specific cause, the AP Research habit is to ask: what "
            "would have to be true for that explanation to be wrong or "
            "incomplete? Usually there's a more boring, more accurate "
            "answer buried a layer deeper than the headline -- which is "
            "exactly the kind of thing I want to get right before I "
            "write about it anywhere, including here.\n\n"

            "I'm registered for AP Cybersecurity next year, and I have "
            "a feeling this is going to matter more than I expect: the "
            "actual technical material is only half of what a good "
            "security analyst does. The other half is exactly what this "
            "class spent a year drilling into me -- checking your "
            "claims before you trust them."
        ),
        "sources": [
            {"name": "AP Cybersecurity (College Board)", "url": "https://apcentral.collegeboard.org/courses/ap-cybersecurity"},
        ],
    },
    {
        "id": "cybersecurity-isnt-just-for-computer-people",
        "title": "Cybersecurity Isn't Just for \"Computer People\"",
        "date": "2026-07-14",
        "read_time": "4 min read",
        "tags": ["Awareness", "General Audience"],
        "excerpt": (
            "You don't need to write code to have a stake in this. "
            "You just need an email address."
        ),
        "tldr": (
            "Every career now runs on accounts, devices, and data. "
            "Security awareness isn't a tech-career skill anymore -- "
            "it's closer to knowing not to give your SSN to a stranger "
            "on the phone."
        ),
        "body": (
            "Whenever I tell someone I'm taking a cybersecurity class, "
            "I get a version of the same response: 'I'm not really a "
            "computer person, so that's not for me.' I understand the "
            "instinct, but I think it's backwards. Cybersecurity isn't "
            "a niche interest for people who like computers. It's a "
            "basic life skill now.\n\n"

            "| Everyday account | What a breach of it actually costs you |\n"
            "|---|---|\n"
            "| Email | Usually the master key -- most other accounts can be reset through it |\n"
            "| School/work login | Grades, records, or work product exposed or altered |\n"
            "| Banking app | Direct financial loss |\n"
            "| Social media | Impersonation, private messages, contact list exposure |\n\n"

            "None of that requires you to understand how encryption "
            "works. All of it can be meaningfully protected, or "
            "meaningfully put at risk, by habits that have nothing to "
            "do with being 'good at computers.'\n\n"

            "This is actually why one of the tools on this site is a "
            "self-assessment instead of another knowledge quiz. A "
            "knowledge quiz tests whether you can define 'phishing.' A "
            "self-assessment asks whether you reuse passwords, whether "
            "you have MFA turned on, whether your phone updates itself "
            "automatically -- the actual behaviors that determine "
            "whether a random attacker has an easy or hard time with "
            "you specifically. You can ace a vocabulary quiz and still "
            "have terrible habits. The habits are what actually "
            "matter.\n\n"

            "> Every generation has its own version of the same "
            "vulnerability. My grandparents' generation grew up trained "
            "to trust an official-sounding voice on the phone. My "
            "generation grew up trained to trust an official-looking "
            "message on a screen. Neither instinct was unreasonable "
            "when it formed. Both get exploited constantly now.\n\n"

            "You don't need to become a security professional to "
            "benefit from thinking about this stuff. You need about "
            "fifteen minutes, a willingness to turn on a few settings "
            "you've been ignoring, and enough healthy suspicion to "
            "pause before clicking something that's asking you to "
            "hurry."
        ),
    },
    {
        "id": "why-i-started-learning-cybersecurity",
        "title": "Why I Started Learning Cybersecurity (Looking Back on Two Years of It)",
        "date": "2026-08-04",
        "read_time": "6 min read",
        "tags": ["Personal", "Reflection"],
        "excerpt": (
            "I didn't start out wanting to be a 'security person.' I "
            "started out building things, and then asked one "
            "uncomfortable question."
        ),
        "tldr": (
            "Two years, three very different classes, and one "
            "uncomfortable question about my own AI projects turned an "
            "elective into the thing I want to keep doing after high "
            "school."
        ),
        "body": (
            "I'm writing this at the start of senior year, which feels "
            "like a reasonable point to actually look back at how I got "
            "here, instead of just where I'm currently headed.\n\n"

            "[CHART:course-timeline]\n\n"

            "It didn't start with a plan. Before I ever took a security "
            "class, I was already building things -- small AI projects, "
            "websites, little tools that solved problems I actually "
            "had. I liked building. I didn't think much about "
            "breaking.\n\n"

            "Then, building something that stored a little bit of user "
            "data, I asked myself a question I couldn't shake: what "
            "happens if someone I've never met, who I'll never see "
            "coming, decides to try to break this? Not maliciously "
            "curious -- actually try. I realized I had absolutely no "
            "idea how to answer that. I knew how to make things work. I "
            "had no idea how to make them hard to break.\n\n"

            "That gap is what got me into Cybersecurity I as a "
            "sophomore. What hooked me wasn't the technical material, "
            "though that came fast too -- it was realizing how much of "
            "security is actually about people. The CIA triad, "
            "firewalls, encryption -- all of that matters, but the "
            "thing that stuck with me was learning how a scam email "
            "gets someone to click in the first five seconds, before "
            "their brain even catches up to their hand. That's not a "
            "computer science problem. That's a psychology problem "
            "wearing a computer science costume.\n\n"

            "> I don't feel like I actually understand something until "
            "I've built it. Reading about how encryption works is fine. "
            "Writing a tool that uses it correctly, and watching it "
            "correctly reject a wrong master password, is a completely "
            "different level of understanding.\n\n"

            "Junior year didn't have a cybersecurity class on my "
            "schedule at all -- AP Computer Science Principles and AP "
            "Research took its place. I didn't expect either of those "
            "to matter much to this specific interest. I was wrong "
            "about that, especially about AP Research, which spent a "
            "year training me to actually check claims instead of "
            "trusting the first source that agrees with me -- a habit "
            "that turned out to matter constantly once I started "
            "building this site and had to decide which sources were "
            "actually worth citing.\n\n"

            "By the time AP Cybersecurity opened up this year -- one of "
            "the first times it's been offered anywhere, since College "
            "Board just took it national -- I didn't hesitate. This "
            "lab exists because of the habit that started somewhere in "
            "the middle of that timeline: I don't feel like I actually "
            "understand a concept until I've built something that uses "
            "it correctly and watched it fail in the right way when it "
            "should."
        ),
    },
    {
        "id": "building-a-phishing-simulator",
        "title": "I Built a Phishing Simulator for This Site — Here's What It Taught Me",
        "date": "2026-08-22",
        "read_time": "7 min read",
        "tags": ["Projects", "Social Engineering"],
        "excerpt": (
            "Writing the fake emails turned out to be harder, and more "
            "revealing, than writing the code around them."
        ),
        "tldr": (
            "My simulator's own math says the friendly, low-pressure "
            "'CEO fraud' email beats the obvious prize-scam email by "
            "roughly 2 to 1. The best phishing isn't the one that "
            "looks like a scam."
        ),
        "body": (
            "For one of the apps on this site, I built a phishing "
            "simulator -- a tool that sends a simulated phishing "
            "campaign against fictional test personas and reports a "
            "click rate. I want to be upfront about something first: "
            "it's fully synthetic. There is no networking code in it at "
            "all -- no way to send a real email to a real person, on "
            "purpose. I wanted the tool to be structurally incapable of "
            "being misused, not just responsibly used.\n\n"

            "What I didn't expect was how much I'd learn from writing "
            "the fake emails themselves. I assumed the hard part would "
            "be the simulation logic -- the code deciding who "
            "statistically 'clicks.' That part took maybe twenty "
            "minutes. Writing three convincing phishing emails took "
            "most of an afternoon, because it forced me to actually "
            "think like someone trying to manipulate a reader instead "
            "of someone writing a normal email.\n\n"

            "[CHART:phishing-click-rates]\n\n"

            "That chart isn't made up for effect -- it's the exact "
            "formula my simulator uses (each synthetic persona's "
            "susceptibility, adjusted by how convincing the template "
            "is), averaged out to its true expected value. The obvious "
            "prize-notification email -- countdown, too-good-to-be-true "
            "reward -- barely moves anyone. The email modeled after "
            "'CEO fraud,' a short, casual message that appears to be "
            "from a company's CEO asking someone to quickly buy gift "
            "cards, beats it by nearly two to one, and it doesn't use "
            "any urgency trick that's obvious on the surface.\n\n"

            "> The most dangerous phishing isn't the one that looks "
            "like a scam. It's the one that looks like a completely "
            "ordinary message from someone you'd normally trust, asking "
            "for something slightly unusual, with just enough urgency "
            "that stopping to double-check feels awkward.\n\n"

            "That gap between the two templates matched what I'd read "
            "about how real-world CEO fraud actually performs against "
            "real organizations, which was oddly reassuring -- it meant "
            "my simplified model was pointing in a direction that "
            "matches reality, not just producing a number that looked "
            "plausible.\n\n"

            "The fix isn't 'be more suspicious of scary emails.' It's "
            "'when a request involves money, credentials, or access, "
            "verify it through a second channel' -- even if that means "
            "the mildly uncomfortable step of just calling the person "
            "and asking if they actually sent it. I came out of this "
            "project more convinced that phishing awareness training "
            "matters, and less convinced that it's mostly about "
            "spotting bad grammar or sketchy links. The best fake "
            "emails don't have either."
        ),
    },
    {
        "id": "three-breaches-that-changed-how-i-think",
        "title": "3 Real Data Breaches That Changed How I Think About Security",
        "date": "2026-09-02",
        "read_time": "7 min read",
        "tags": ["Case Studies", "History"],
        "excerpt": (
            "None of these were caused by some genius, movie-style "
            "hack. That's exactly what makes them worth studying."
        ),
        "tldr": (
            "Equifax, Target, and Colonial Pipeline weren't broken by "
            "genius attackers. A missed patch, an over-trusted vendor, "
            "and one unpatched entry point did the damage -- which "
            "means the lessons apply to normal decisions, not exotic "
            "ones."
        ),
        "body": (
            "One thing that surprised me learning about real-world "
            "breaches is how rarely they involve some brilliant, "
            "unstoppable technical genius. Most of the time, the cause "
            "is something almost boring -- which is honestly a lot more "
            "useful to learn from, because it means the lesson usually "
            "applies to normal decisions, not exotic ones.\n\n"

            "[CHART:breach-scale]\n\n"

            "| Breach | Root cause | The lesson |\n"
            "|---|---|---|\n"
            "| Equifax (2017) | Known vulnerability, unpatched for months | Patch management is high-leverage, not busywork |\n"
            "| Target (2013) | Stolen credentials from a third-party HVAC vendor | Your security includes every third party you trust |\n"
            "| Colonial Pipeline (2021) | Ransomware via a single compromised password | Digital incidents can have real, physical consequences |\n\n"

            "**Equifax, 2017.** One of the credit bureaus that holds "
            "financial data on most American adults suffered a breach "
            "that exposed the personal information -- including Social "
            "Security numbers -- of about 147 million people. The root "
            "cause wasn't some undiscovered zero-day. It was a known "
            "vulnerability in a piece of web software (Apache Struts) "
            "that had a patch available for months before the breach "
            "happened.\n\n"

            "**Target, 2013.** During the holiday shopping season, "
            "attackers stole roughly 40 million customers' credit and "
            "debit card numbers. The way in wasn't Target's own systems "
            "directly -- it was stolen network credentials from a "
            "third-party HVAC (heating and air conditioning) vendor "
            "that had remote access into Target's network for billing "
            "purposes.\n\n"

            "**Colonial Pipeline, 2021.** A ransomware attack hit the "
            "company operating a major fuel pipeline supplying a large "
            "part of the U.S. East Coast. The company shut the pipeline "
            "down as a precaution, which led to real fuel shortages and "
            "panic buying. Colonial ultimately paid a multi-million "
            "dollar ransom, part of which U.S. law enforcement later "
            "recovered.\n\n"

            "> A ransomware attack on IT systems produced lines at gas "
            "stations. Security incidents increasingly have real, "
            "physical, economy-scale consequences -- not just leaked "
            "data.\n\n"

            "Put together, these three cases taught me more about "
            "practical security priorities than any single lecture: "
            "patch what's already known to be broken, watch every third "
            "party you trust with access, and take backups and "
            "incident response planning seriously. None of these "
            "breaches needed a genius attacker. They needed one skipped "
            "patch, one over-trusted vendor connection, and one "
            "unpatched entry point respectively. That's the part that "
            "stuck with me."
        ),
        "sources": [
            {"name": "Krebs on Security", "url": "https://krebsonsecurity.com/"},
        ],
    },
    {
        "id": "ai-and-cybersecurity",
        "title": "How AI Is Changing Both Sides of Cybersecurity",
        "date": "2026-09-12",
        "read_time": "6 min read",
        "tags": ["AI", "Trends"],
        "excerpt": (
            "I got into this from the AI side first, so this is the "
            "intersection I can't stop paying attention to."
        ),
        "tldr": (
            "AI is making attacks better-written and defenses "
            "faster-reacting at the same time. The old advice ('watch "
            "for bad grammar') is running out of runway -- the durable "
            "advice is behavioral, not surface-level."
        ),
        "body": (
            "Most of my writing and building before cybersecurity was "
            "in AI, so I probably notice this intersection more than "
            "most people would. AI isn't just one more tool in the "
            "cybersecurity world -- it's actively changing both sides "
            "of the fight, attack and defense, at the same time.\n\n"

            "| | Old approach | AI-accelerated version |\n"
            "|---|---|---|\n"
            "| Attack | Poorly-written phishing, obvious grammar tells | Grammatically perfect, personalized messages in seconds |\n"
            "| Attack | A human impersonator on the phone | Cloned voices and deepfake video calls |\n"
            "| Defense | A human analyst reading logs line by line | Anomaly detection across more data than any person could read |\n"
            "| Defense | Manual triage of every alert | ML models surfacing the handful of alerts that matter |\n\n"

            "On the attack side, the most obvious shift is quality. "
            "Phishing emails used to be a reasonably reliable tell -- "
            "awkward phrasing, weird grammar. A language model can now "
            "write a grammatically perfect, contextually appropriate, "
            "personalized message in seconds. The 'badly written scam "
            "email' red flag, one of the most commonly taught tells, is "
            "quietly becoming less reliable every year. Voice and video "
            "deepfakes push this even further -- the CEO fraud pattern "
            "I wrote about in my phishing simulator article gets a lot "
            "scarier when the 'CEO' isn't just a text message, but a "
            "convincing cloned voice on a phone call.\n\n"

            "On the defense side, the shift is at least as significant. "
            "Modern security teams deal with an amount of log and alert "
            "data that's genuinely impossible for a human analyst to "
            "read line by line. Machine learning models trained to spot "
            "anomalies -- a login from an unusual location, a pattern "
            "of file access that doesn't match someone's normal "
            "behavior -- can surface the handful of alerts that "
            "actually matter out of an ocean of noise. That's already "
            "how a lot of modern security operations centers function.\n\n"

            "> This is fundamentally an arms race running at AI speed "
            "instead of human speed. I don't think that race has an "
            "obvious permanent winner, and I'm skeptical of anyone who "
            "claims it does in either direction.\n\n"

            "My honest takeaway, as someone building small tools on "
            "both sides of that line, is that the old advice -- 'watch "
            "for bad grammar,' 'look for a sketchy link' -- is starting "
            "to run out of runway as a primary defense. The more "
            "durable version of that advice is behavioral, not "
            "surface-level: verify unusual requests through a second "
            "channel, question urgency regardless of how polished the "
            "message looks, and don't assume 'well-written' means "
            "'legitimate' anymore. That's a harder habit to build than "
            "spotting a typo, but it's the one that's actually going to "
            "keep working."
        ),
        "sources": [
            {"name": "MITRE ATT&CK", "url": "https://attack.mitre.org/"},
        ],
    },
]
