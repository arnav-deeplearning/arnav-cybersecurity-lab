(function () {
  var input = document.getElementById("passwordInput");
  var toggleBtn = document.getElementById("toggleVisibilityBtn");
  var strengthFill = document.getElementById("strengthFill");
  var strengthLabel = document.getElementById("strengthLabel");
  var strengthStats = document.getElementById("strengthStats");
  var statLength = document.getElementById("statLength");
  var statCharset = document.getElementById("statCharset");
  var statEntropy = document.getElementById("statEntropy");
  var statCrackTime = document.getElementById("statCrackTime");
  var warningsList = document.getElementById("strengthWarnings");
  if (!input) return;

  var GUESSES_PER_SECOND = 10e9; // 10 billion/sec: a realistic offline fast-hash cracking benchmark

  var COMMON_PATTERNS = [
    "password", "letmein", "qwerty", "admin", "welcome", "dragon",
    "monkey", "football", "iloveyou", "123456", "abc123", "trustno1",
  ];

  function charsetSize(pw) {
    var size = 0;
    if (/[a-z]/.test(pw)) size += 26;
    if (/[A-Z]/.test(pw)) size += 26;
    if (/[0-9]/.test(pw)) size += 10;
    if (/[^a-zA-Z0-9]/.test(pw)) size += 32;
    return size || 1;
  }

  function hasSequential(pw) {
    var seqs = ["0123456789", "abcdefghijklmnopqrstuvwxyz", "qwertyuiop", "asdfghjkl", "zxcvbnm"];
    var lower = pw.toLowerCase();
    for (var i = 0; i < seqs.length; i++) {
      for (var j = 0; j <= seqs[i].length - 3; j++) {
        if (lower.indexOf(seqs[i].substr(j, 3)) > -1) return true;
      }
    }
    return false;
  }

  function hasRepeatedChars(pw) {
    return /(.)\1\1/.test(pw);
  }

  function containsCommonPattern(pw) {
    var lower = pw.toLowerCase();
    return COMMON_PATTERNS.some(function (p) { return lower.indexOf(p) > -1; });
  }

  function formatCrackTime(seconds) {
    if (!isFinite(seconds)) return "effectively never";
    var units = [
      ["years", 365 * 24 * 3600],
      ["days", 24 * 3600],
      ["hours", 3600],
      ["minutes", 60],
      ["seconds", 1],
    ];
    if (seconds < 1) return "instantly";
    for (var i = 0; i < units.length; i++) {
      if (seconds >= units[i][1]) {
        var value = seconds / units[i][1];
        if (value > 1e12) return "longer than the age of the universe";
        return Math.round(value).toLocaleString() + " " + units[i][0];
      }
    }
    return "instantly";
  }

  function analyze() {
    var pw = input.value;
    if (!pw) {
      strengthFill.style.width = "0%";
      strengthFill.className = "strength-fill";
      strengthLabel.textContent = "Start typing to see your analysis";
      strengthStats.style.display = "none";
      warningsList.innerHTML = "";
      return;
    }

    var size = charsetSize(pw);
    var entropy = pw.length * (Math.log(size) / Math.log(2));
    var crackSeconds = Math.pow(2, entropy) / GUESSES_PER_SECOND;

    var warnings = [];
    if (containsCommonPattern(pw)) warnings.push("Contains a common password or word found in most attacker dictionaries -- this makes it far weaker than the raw entropy number suggests.");
    if (hasSequential(pw)) warnings.push("Contains a sequential pattern (like '123' or 'qwerty') -- these are tried first by real attackers.");
    if (hasRepeatedChars(pw)) warnings.push("Contains 3+ repeated characters in a row, which reduces real-world randomness.");
    if (pw.length < 12) warnings.push("Under 12 characters -- length is one of the strongest factors in real password strength.");

    var effectiveEntropy = entropy;
    if (containsCommonPattern(pw)) effectiveEntropy = Math.min(entropy, 10);

    var label, fillClass, fillPct;
    if (effectiveEntropy < 28) { label = "Very Weak"; fillClass = "is-weak"; fillPct = 15; }
    else if (effectiveEntropy < 36) { label = "Weak"; fillClass = "is-weak"; fillPct = 35; }
    else if (effectiveEntropy < 60) { label = "Reasonable"; fillClass = "is-medium"; fillPct = 55; }
    else if (effectiveEntropy < 100) { label = "Strong"; fillClass = "is-strong"; fillPct = 80; }
    else { label = "Very Strong"; fillClass = "is-strong"; fillPct = 100; }

    strengthFill.style.width = fillPct + "%";
    strengthFill.className = "strength-fill " + fillClass;
    strengthLabel.textContent = label;

    strengthStats.style.display = "";
    statLength.textContent = pw.length + " characters";
    statCharset.textContent = size + " possible characters";
    statEntropy.textContent = Math.round(entropy) + " bits";
    statCrackTime.textContent = formatCrackTime(crackSeconds);

    warningsList.innerHTML = "";
    warnings.forEach(function (w) {
      var li = document.createElement("li");
      li.textContent = w;
      warningsList.appendChild(li);
    });
  }

  toggleBtn.addEventListener("click", function () {
    if (input.type === "password") {
      input.type = "text";
      toggleBtn.textContent = "Hide";
    } else {
      input.type = "password";
      toggleBtn.textContent = "Show";
    }
  });

  input.addEventListener("input", analyze);
  analyze();
})();
