"""
Articles for the Articles page.

`body` is a single string with paragraphs separated by blank lines;
the template splits on double newlines and wraps each in <p>. Dates
are ISO format (YYYY-MM-DD).
"""

ARTICLES = [
    {
        "id": "why-i-started-learning-cybersecurity",
        "title": "Why I Started Learning Cybersecurity (And Why You Might Want To)",
        "date": "2026-06-15",
        "read_time": "5 min read",
        "tags": ["Personal", "Getting Started"],
        "excerpt": (
            "I didn't start out wanting to be a 'security person.' I "
            "started out building things, and then asked one "
            "uncomfortable question."
        ),
        "body": (
            "I didn't walk into Cybersecurity I already knowing I "
            "wanted to do this. Before I ever took a security class, I "
            "was already building things -- small AI projects, websites, "
            "little tools that solved problems I actually had. I liked "
            "building. I didn't think much about breaking.\n\n"

            "Then one day, building something that stored a little bit "
            "of user data, I asked myself a question I couldn't shake: "
            "what happens if someone I've never met, who I'll never see "
            "coming, decides to try to break this? Not maliciously "
            "curious -- actually try. I realized I had absolutely no "
            "idea how to answer that. I knew how to make things work. I "
            "had no idea how to make them hard to break.\n\n"

            "That gap bothered me enough that I signed up for "
            "Cybersecurity I the next semester, mostly out of "
            "curiosity. What hooked me wasn't the technical stuff, "
            "though that came fast too -- it was realizing how much of "
            "security is actually about people. The CIA triad, "
            "firewalls, encryption -- all of that matters, but the "
            "thing that stuck with me was learning how a scam email "
            "gets someone to click in the first five seconds, before "
            "their brain even catches up to their hand. That's not a "
            "computer science problem. That's a psychology problem "
            "wearing a computer science costume.\n\n"

            "By the time AP Cybersecurity opened up this year -- one of "
            "the first times it's been offered anywhere, since College "
            "Board just took it national -- I didn't hesitate. And this "
            "site exists because of a habit I picked up along the way: "
            "I don't feel like I actually understand something until "
            "I've built it. Reading about how AES-256 encryption works "
            "is fine. Writing a password manager that actually uses it "
            "correctly, and watching it correctly reject a wrong master "
            "password, is a completely different level of "
            "understanding.\n\n"

            "If you're on the fence about trying a cybersecurity class "
            "or elective, here's my honest pitch: you don't need to be "
            "'a computer person' already. You need to be a little "
            "suspicious of things, curious about how systems break, and "
            "willing to build something and then try to figure out how "
            "you'd break your own work. That's basically the whole "
            "job."
        ),
    },
    {
        "id": "cia-triad-explained",
        "title": "The CIA Triad Isn't About Spies: Confidentiality, Integrity, Availability, Explained",
        "date": "2026-06-29",
        "read_time": "6 min read",
        "tags": ["Concepts", "Foundations"],
        "excerpt": (
            "It's the first thing every cybersecurity class teaches, "
            "and also the thing that quietly explains almost every "
            "security decision that follows it."
        ),
        "body": (
            "Every cybersecurity course I've taken starts with the same "
            "three letters: CIA. Not the agency -- the triad. "
            "Confidentiality, Integrity, Availability. It sounds like "
            "the kind of thing you memorize for a quiz and forget by "
            "June. I thought that too, until I noticed I couldn't stop "
            "using it to explain literally everything else in the "
            "course.\n\n"

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
            "database needs integrity: if a hacker (or an ambitious "
            "student) could quietly edit it, the number stops meaning "
            "anything. This is why systems use things like hashes and "
            "checksums -- little mathematical fingerprints that change "
            "the instant even one character does.\n\n"

            "**Availability** is the one people forget exists until it "
            "doesn't. A system can be perfectly confidential and have "
            "flawless integrity and still fail completely if nobody who "
            "needs it can actually use it. This is exactly what a DDoS "
            "attack targets -- it doesn't steal anything or change "
            "anything, it just floods a system with traffic until real "
            "users can't get through. Availability is also why backups "
            "matter so much: ransomware is, at its core, an attack on "
            "availability. Your files still technically exist. You just "
            "can't use them anymore.\n\n"

            "What clicked for me is that almost every security decision "
            "is really a decision about which side of this triangle "
            "you're protecting, and that those three goals sometimes "
            "pull against each other. The most confidential system "
            "imaginable -- locked in a vault, disconnected from "
            "everything -- has terrible availability. The most "
            "available system imaginable -- open to everyone, no "
            "authentication -- has zero confidentiality. Security isn't "
            "about maximizing all three. It's about deciding, "
            "deliberately, how much of each a specific system actually "
            "needs.\n\n"

            "That reframing is honestly why the triad stuck with me. "
            "It's not a memorization exercise. It's a lens. Once you "
            "have it, you start looking at security news differently: "
            "instead of 'a company got hacked,' you start asking which "
            "part of the triad actually failed, and that question "
            "usually tells you a lot about what should have been done "
            "differently."
        ),
    },
    {
        "id": "five-password-habits",
        "title": "5 Password Habits That Are Quietly Wrecking Your Security",
        "date": "2026-07-10",
        "read_time": "5 min read",
        "tags": ["Best Practices", "Practical"],
        "excerpt": (
            "None of these require buying anything or learning to "
            "code. They just require breaking a few habits you "
            "probably don't think about twice."
        ),
        "body": (
            "I built a password entropy analyzer for this site "
            "partly because I wanted to see, in actual math, why some "
            "of the passwords I used to think were 'pretty good' "
            "really weren't. Here's what I'd tell a friend, not a "
            "textbook.\n\n"

            "**1. Reusing the same password everywhere.** This is the "
            "big one. It doesn't matter how strong your password is if "
            "you use it on ten different sites and one of them gets "
            "breached -- and someone eventually will. Attackers "
            "specifically take leaked passwords from one breach and try "
            "them on other sites. It's called credential stuffing, and "
            "it works embarrassingly often because of exactly this "
            "habit.\n\n"

            "**2. Treating length as optional.** A shorter password "
            "with symbols swapped in ('P@ssw0rd!') is not meaningfully "
            "stronger than a longer plain-English one. Length beats "
            "complexity almost every time, because of how fast modern "
            "hardware can guess short passwords. Four random unrelated "
            "words strung together is both easier to remember and "
            "mathematically far stronger than eight characters of "
            "substituted symbols.\n\n"

            "**3. Skipping MFA because it's 'annoying.'** I get it, "
            "typing in a six-digit code is one more step. But MFA is "
            "one of the single highest-leverage things you can do -- "
            "it means a leaked password alone usually isn't enough to "
            "get into your account. Turn it on for email and banking "
            "first if you do nothing else.\n\n"

            "**4. Never checking if you've already been breached.** "
            "There's a free, legitimate tool called Have I Been Pwned "
            "where you can check if your email shows up in a known data "
            "breach. I checked mine expecting nothing and found two "
            "breaches I'd never heard about. Takes thirty seconds, and "
            "it's a genuinely useful wake-up call.\n\n"

            "**5. Writing passwords down somewhere insecure -- or "
            "keeping them all in your head.** Neither extreme works "
            "well. A sticky note on a monitor is an obvious problem, "
            "but so is refusing to use a password manager and then "
            "reusing one 'good' password everywhere because it's the "
            "only one you can remember. A password manager (I wrote my "
            "own, mostly to understand how one actually works under "
            "the hood) solves this cleanly: one strong master password "
            "protects a vault of unique, actually-strong passwords for "
            "everything else.\n\n"

            "None of this requires being a security expert. It requires "
            "about twenty minutes and a willingness to admit your "
            "current habits are probably worse than you think. Mine "
            "were."
        ),
    },
    {
        "id": "building-a-phishing-simulator",
        "title": "I Built a Phishing Simulator for This Site — Here's What It Taught Me",
        "date": "2026-07-24",
        "read_time": "6 min read",
        "tags": ["Projects", "Social Engineering"],
        "excerpt": (
            "Writing the fake emails turned out to be harder, and more "
            "revealing, than writing the code around them."
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

            "The most obvious template I wrote -- a fake prize "
            "notification -- was almost boring to design. Urgency, a "
            "reward, a countdown. Anyone who's used the internet for "
            "five years has some instinct against that one. But the "
            "one modeled after 'CEO fraud' -- a short, casual message "
            "that appears to be from a company's CEO, asking someone to "
            "quickly buy gift cards -- that one bothered me. It doesn't "
            "look scary. It doesn't use any urgency tricks that are "
            "obvious on the surface. It works by borrowing someone's "
            "authority and their busy schedule as an excuse for why you "
            "shouldn't ask questions. When I ran the simulation against "
            "my synthetic test personas, that template consistently got "
            "the highest click rate, by a lot -- which matched what I'd "
            "read about how real-world CEO fraud actually performs "
            "against real organizations.\n\n"

            "That was the actual lesson, and it wasn't a technical one: "
            "the most dangerous phishing isn't the one that looks like "
            "a scam. It's the one that looks like a completely ordinary "
            "message from someone you'd normally trust, asking for "
            "something slightly unusual, with just enough urgency that "
            "stopping to double-check feels awkward. The fix isn't "
            "'be more suspicious of scary emails.' It's 'when a request "
            "involves money, credentials, or access, verify it through "
            "a second channel -- even if that means the mildly "
            "uncomfortable step of just calling the person and asking "
            "if they actually sent it.'\n\n"

            "I came out of that project more convinced that phishing "
            "awareness training actually matters, and less convinced "
            "that it's mostly about spotting bad grammar or sketchy "
            "links. The best fake emails don't have either."
        ),
    },
    {
        "id": "cybersecurity-isnt-just-for-computer-people",
        "title": "Cybersecurity Isn't Just for \"Computer People\"",
        "date": "2026-08-07",
        "read_time": "4 min read",
        "tags": ["Awareness", "General Audience"],
        "excerpt": (
            "You don't need to write code to have a stake in this. "
            "You just need an email address."
        ),
        "body": (
            "Whenever I tell someone I'm taking a cybersecurity class, "
            "I get a version of the same response: 'I'm not really a "
            "computer person, so that's not for me.' I understand the "
            "instinct, but I think it's backwards. Cybersecurity isn't "
            "a niche interest for people who like computers. It's a "
            "basic life skill now, the same way knowing not to give "
            "your Social Security number to a stranger on the phone is "
            "a basic life skill.\n\n"

            "Think about how much of an ordinary day runs through "
            "accounts and devices that have nothing to do with a tech "
            "career: your school login, your bank app, your email, "
            "whatever social platform your friend group actually uses "
            "this year, the family group chat. None of that requires "
            "you to understand how encryption works. All of it can be "
            "meaningfully protected, or meaningfully put at risk, by "
            "habits that have nothing to do with being 'good at "
            "computers.'\n\n"

            "This is actually why I built a self-assessment tool for "
            "this site instead of just another quiz. A knowledge quiz "
            "tests whether you can define 'phishing.' A self-assessment "
            "asks whether you reuse passwords, whether you have MFA "
            "turned on, whether your phone updates itself automatically "
            "-- the actual behaviors that determine whether a random "
            "attacker has an easy or hard time with you specifically. "
            "You can ace a vocabulary quiz and still have terrible "
            "habits. The habits are what actually matter.\n\n"

            "I'd also push back gently on the idea that security "
            "awareness is a 'young person' or 'tech person' thing at "
            "all. Every generation has its own version of the same "
            "vulnerability: my grandparents' generation grew up trained "
            "to trust an official-sounding voice on the phone; my "
            "generation grew up trained to trust an official-looking "
            "message on a screen. Neither instinct was unreasonable "
            "when it formed. Both get exploited constantly now.\n\n"

            "You don't need to become a security professional to "
            "benefit from thinking about this stuff. You need about "
            "fifteen minutes, a willingness to turn on a few settings "
            "you've been ignoring, and enough healthy suspicion to "
            "pause before clicking something that's asking you to hurry."
        ),
    },
    {
        "id": "red-team-vs-blue-team",
        "title": "Red Team vs. Blue Team: Which Path Fits You?",
        "date": "2026-08-14",
        "read_time": "6 min read",
        "tags": ["Careers", "For Students"],
        "excerpt": (
            "If you're curious about a cybersecurity path, this is the "
            "first fork in the road worth thinking about."
        ),
        "body": (
            "If you tell people you're into cybersecurity, a common "
            "next question is 'so, do you want to be a hacker?' The "
            "honest answer is that 'hacker' isn't really one job, and "
            "the field usually gets split into two broad camps: red "
            "team and blue team. If you're a student trying to figure "
            "out which direction actually interests you, this is a "
            "decent place to start thinking about it.\n\n"

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
            "team, and the work of actually stopping or containing a "
            "real incident is a genuinely high-stakes skill.\n\n"

            "Here's what I've noticed trying both, in a small way, "
            "through school projects: they reward different kinds of "
            "thinking. Red team work rewards creative, lateral "
            "thinking -- looking at a system and asking 'what's the "
            "weird, unintended way I could misuse this?' Blue team "
            "work rewards methodical, patient thinking -- looking at a "
            "flood of logs and noticing the one entry that doesn't "
            "belong. Neither is 'better.' They're just different "
            "muscles.\n\n"

            "A third option worth knowing about, since it doesn't get "
            "mentioned as often: **purple team**, which isn't really a "
            "separate skill so much as a mindset -- red and blue "
            "teams actively collaborating, where the attackers share "
            "exactly what they found and how, so defenders can close "
            "the gap immediately instead of guessing. If you like both "
            "sides of the puzzle, that combined role is worth keeping "
            "on your radar as you learn more.\n\n"

            "If you're still deciding, my honest advice is to just try "
            "small pieces of both before picking a lane. I went in "
            "assuming I'd be purely interested in the offensive side, "
            "and building actual defensive tools -- a password manager, "
            "a phishing simulator meant to train people, not fool them "
            "-- turned out to be just as satisfying, in a quieter way."
        ),
    },
    {
        "id": "three-breaches-that-changed-how-i-think",
        "title": "3 Real Data Breaches That Changed How I Think About Security",
        "date": "2026-08-21",
        "read_time": "7 min read",
        "tags": ["Case Studies", "History"],
        "excerpt": (
            "None of these were caused by some genius, movie-style "
            "hack. That's exactly what makes them worth studying."
        ),
        "body": (
            "One thing that surprised me learning about real-world "
            "breaches is how rarely they involve some brilliant, "
            "unstoppable technical genius. Most of the time, the cause "
            "is something almost boring -- which is honestly a lot more "
            "useful to learn from, because it means the lesson usually "
            "applies to normal decisions, not exotic ones.\n\n"

            "**Equifax, 2017.** One of the credit bureaus that holds "
            "financial data on most American adults suffered a breach "
            "that exposed the personal information -- including Social "
            "Security numbers -- of about 147 million people. The root "
            "cause wasn't some undiscovered zero-day. It was a known "
            "vulnerability in a piece of web software (Apache Struts) "
            "that had a patch available for months before the breach "
            "happened. The lesson I took from this one is almost "
            "uncomfortably simple: patch management isn't a boring "
            "afterthought, it's one of the highest-leverage things a "
            "security program does, and skipping it is how 'we knew "
            "about this weakness' turns into 'and we got breached "
            "through it anyway.'\n\n"

            "**Target, 2013.** During the holiday shopping season, "
            "attackers stole roughly 40 million customers' credit and "
            "debit card numbers. The way in wasn't Target's own systems "
            "directly -- it was stolen network credentials from a "
            "third-party HVAC (heating and air conditioning) vendor "
            "that had remote access into Target's network for billing "
            "purposes. This one reshaped how I think about trust "
            "boundaries: your security isn't just about your own "
            "systems, it's about every third party you've handed access "
            "to, even ones that seem completely unrelated to your core "
            "business.\n\n"

            "**Colonial Pipeline, 2021.** A ransomware attack (by a "
            "group known as DarkSide) hit the company operating a major "
            "fuel pipeline supplying a large part of the U.S. East "
            "Coast. The company shut the pipeline down as a precaution, "
            "which led to real fuel shortages and panic buying. Colonial "
            "ultimately paid a multi-million dollar ransom, part of "
            "which U.S. law enforcement later recovered. What struck me "
            "about this case is how it made 'cybersecurity' impossible "
            "to think of as purely a digital problem -- a ransomware "
            "attack on IT systems produced lines at gas stations. "
            "Security incidents increasingly have real, physical, "
            "economy-scale consequences, not just leaked data.\n\n"

            "Put together, these three cases taught me more about "
            "practical security priorities than any single lecture: "
            "patch what's already known to be broken, watch every "
            "third party you trust with access, and take backups and "
            "incident response planning seriously, because the cost of "
            "an incident is rarely contained to just 'computer stuff.' "
            "None of these breaches needed a genius attacker. They "
            "needed one skipped patch, one over-trusted vendor "
            "connection, and one unpatched entry point respectively. "
            "That's the part that stuck with me."
        ),
    },
    {
        "id": "ai-and-cybersecurity",
        "title": "How AI Is Changing Both Sides of Cybersecurity",
        "date": "2026-09-04",
        "read_time": "6 min read",
        "tags": ["AI", "Trends"],
        "excerpt": (
            "I got into this from the AI side first, so this is the "
            "intersection I can't stop paying attention to."
        ),
        "body": (
            "Most of my writing and building before cybersecurity was "
            "in AI, so I probably notice this intersection more than "
            "most people would. AI isn't just one more tool in the "
            "cybersecurity world -- it's actively changing both sides "
            "of the fight, attack and defense, at the same time, and "
            "not always in ways that feel comfortable.\n\n"

            "On the attack side, the most obvious shift is quality. "
            "Phishing emails used to be a reasonably reliable tell -- "
            "awkward phrasing, weird grammar, the kind of thing my "
            "'password expiring in 2 hours' example template leans on "
            "for a class demo. A language model can now write a "
            "grammatically perfect, contextually appropriate, "
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
            "actually matter out of an ocean of noise. That's not "
            "science fiction; it's already how a lot of modern security "
            "operations centers function, and it's part of why 'log "
            "analysis' is one of the areas I want to keep building "
            "projects around.\n\n"

            "What I find most interesting isn't either side alone -- "
            "it's that this is fundamentally an arms race running at AI "
            "speed instead of human speed. Every improvement in "
            "AI-assisted attack tooling puts pressure on defenders to "
            "adopt AI-assisted detection just to keep pace, and vice "
            "versa. I don't think that race has an obvious permanent "
            "winner, and I'm skeptical of anyone who claims it does in "
            "either direction.\n\n"

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
    },
]
