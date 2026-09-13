(function () {
  var STORAGE_KEY = "cyberlab-checkup-last-result";

  var CATEGORIES = {
    passwords: "Passwords & Authentication",
    devices: "Devices & Updates",
    backups: "Backups & Recovery",
    awareness: "Awareness & Privacy",
  };

  var QUESTIONS = [
    { category: "passwords", question: "Do you reuse the same password across multiple accounts?",
      options: [["Never -- every account has a unique password", 3], ["A few important ones are unique, but I reuse for less important stuff", 1], ["Yes, I reuse the same password on most sites", 0]] },
    { category: "passwords", question: "Do you have multi-factor authentication (MFA/2FA) turned on for your main email account?",
      options: [["Yes", 3], ["Not sure", 1], ["No", 0]] },
    { category: "passwords", question: "How do you actually store your passwords?",
      options: [["A password manager", 3], ["Browser-saved, or a few memorized strong ones", 2], ["Written down somewhere insecure, or memorized weak/reused ones", 0]] },
    { category: "passwords", question: "When did you last check if any of your accounts appeared in a known data breach?",
      options: [["Within the last few months", 3], ["More than a year ago", 1], ["Never", 0]] },

    { category: "devices", question: "Do you install software and OS updates promptly when they're available?",
      options: [["Usually right away, or automatic updates are on", 3], ["Eventually, within a few weeks", 1], ["I ignore or postpone them indefinitely", 0]] },
    { category: "devices", question: "Does your phone or computer lock automatically with a PIN, password, or biometric?",
      options: [["Yes, always", 3], ["Sometimes", 1], ["No lock screen at all", 0]] },
    { category: "devices", question: "If your phone or laptop were lost or stolen today, could you remotely locate, lock, or wipe it?",
      options: [["Yes, it's already set up", 3], ["I know the feature exists but haven't set it up", 1], ["No idea", 0]] },

    { category: "backups", question: "Do you have a backup of your important files that isn't just on the same device?",
      options: [["Yes, automatic cloud or external backup", 3], ["Occasionally, manually", 1], ["No backup at all", 0]] },
    { category: "backups", question: "If ransomware encrypted your device today, could you recover your files without paying?",
      options: [["Yes, confidently", 3], ["Maybe some of it", 1], ["No", 0]] },

    { category: "awareness", question: "When you get an unexpected, urgent email asking you to click a link or provide info, what do you usually do?",
      options: [["Verify through another channel before acting", 3], ["Look for obvious red flags, then decide", 2], ["Usually just act on it", 0]] },
    { category: "awareness", question: "Do you use sensitive accounts (banking, email) over public Wi-Fi without a VPN?",
      options: [["No, I avoid it or use a VPN", 3], ["Sometimes, without really thinking about it", 1], ["Yes, regularly", 0]] },
    { category: "awareness", question: "How much of your social media profile info (birthday, location, school) is visible to the public?",
      options: [["Mostly private / limited to people I know", 3], ["Some of it is public", 1], ["Fully public", 0]] },
  ];

  var TIPS = {
    passwords: "Get a password manager and turn on MFA for your email first -- email is usually the account that can reset everything else.",
    devices: "Turn on automatic updates and set up 'Find My Device' (or your platform's equivalent) before you actually need it, not after.",
    backups: "Set up one automatic backup (cloud or external drive) today. If ransomware hit right now, would you actually be fine?",
    awareness: "Practice pausing on urgent requests -- verify through a second channel (a phone call, a separate message) before acting.",
  };

  var introEl = document.getElementById("checkupIntro");
  var playEl = document.getElementById("checkupPlay");
  var resultsEl = document.getElementById("checkupResults");
  var progressFill = document.getElementById("progressFill");
  var progressLabel = document.getElementById("progressLabel");
  var questionCategory = document.getElementById("questionCategory");
  var questionText = document.getElementById("questionText");
  var checkupOptions = document.getElementById("checkupOptions");
  var overallScore = document.getElementById("overallScore");
  var categoryBreakdown = document.getElementById("categoryBreakdown");
  var checkupTips = document.getElementById("checkupTips");

  var index = 0;
  var answers = []; // {category, points}

  function shuffleQuestions() {
    // Keep a stable, readable order (grouped by category) rather than shuffling --
    // this is a self-assessment, not a quiz, so order doesn't need randomizing.
    return QUESTIONS.slice();
  }

  var pool = shuffleQuestions();

  function startCheckup() {
    index = 0;
    answers = [];
    introEl.style.display = "none";
    resultsEl.style.display = "none";
    playEl.style.display = "";
    renderQuestion();
  }

  function renderQuestion() {
    var q = pool[index];
    questionCategory.textContent = CATEGORIES[q.category];
    questionText.textContent = q.question;
    progressLabel.textContent = "Question " + (index + 1) + " of " + pool.length;
    progressFill.style.width = Math.round((index / pool.length) * 100) + "%";

    checkupOptions.innerHTML = "";
    q.options.forEach(function (opt) {
      var btn = document.createElement("button");
      btn.type = "button";
      btn.className = "quiz-option";
      btn.textContent = opt[0];
      btn.addEventListener("click", function () {
        answers.push({ category: q.category, points: opt[1] });
        index++;
        if (index >= pool.length) finish();
        else renderQuestion();
      });
      checkupOptions.appendChild(btn);
    });
  }

  function finish() {
    playEl.style.display = "none";
    resultsEl.style.display = "";

    var totalPoints = answers.reduce(function (sum, a) { return sum + a.points; }, 0);
    var maxPoints = pool.length * 3;
    var pct = Math.round((totalPoints / maxPoints) * 100);
    overallScore.textContent = "Overall score: " + pct + "% (" + totalPoints + " / " + maxPoints + " points)";

    var byCategory = {};
    Object.keys(CATEGORIES).forEach(function (cat) { byCategory[cat] = { points: 0, max: 0 }; });
    answers.forEach(function (a) { byCategory[a.category].points += a.points; });
    pool.forEach(function (q) { byCategory[q.category].max += 3; });

    categoryBreakdown.innerHTML = "";
    var weakCategories = [];
    Object.keys(CATEGORIES).forEach(function (cat) {
      var c = byCategory[cat];
      var catPct = Math.round((c.points / c.max) * 100);
      if (catPct < 70) weakCategories.push(cat);

      var row = document.createElement("div");
      row.className = "category-row";
      row.innerHTML =
        '<span>' + CATEGORIES[cat] + '</span>' +
        '<div class="category-bar"><div class="category-bar-fill" style="width:' + catPct + '%"></div></div>' +
        '<span>' + catPct + '%</span>';
      categoryBreakdown.appendChild(row);
    });

    checkupTips.innerHTML = "";
    if (weakCategories.length === 0) {
      var li = document.createElement("li");
      li.textContent = "Solid across the board -- the biggest thing left is just keeping these habits up over time.";
      checkupTips.appendChild(li);
    } else {
      weakCategories.forEach(function (cat) {
        var tip = document.createElement("li");
        tip.textContent = TIPS[cat];
        checkupTips.appendChild(tip);
      });
    }

    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify({ pct: pct, date: new Date().toISOString() }));
    } catch (e) { /* ignore */ }
  }

  document.getElementById("startCheckupBtn").addEventListener("click", startCheckup);
  document.getElementById("retakeBtn").addEventListener("click", function () {
    resultsEl.style.display = "none";
    introEl.style.display = "";
  });
})();
