(function () {
  var ROUND = [
    { url: "https://www.northpeakcorp.com/login", safe: true,
      explanation: "This is the company's actual root domain -- clean, no tricks." },
    { url: "https://northpeakcorp.com.account-verify.ru/login", safe: false,
      explanation: "The real brand name is just the start of a subdomain. The actual domain being visited is account-verify.ru -- read domains from right to left." },
    { url: "https://mail.cloudsend.com/inbox", safe: true,
      explanation: "A legitimate subdomain (mail.) of the real cloudsend.com root domain." },
    { url: "http://cloudsend-secure-login.net/inbox", safe: false,
      explanation: "Completely different domain (cloudsend-secure-login.net, not cloudsend.com) -- and it's not even using HTTPS." },
    { url: "https://www.pixelloop.com/gallery", safe: true,
      explanation: "The correct domain, spelled correctly." },
    { url: "https://www.pixeİloop.com/gallery", safe: false,
      explanation: "Look closely -- that's a capital I standing in for a lowercase l. This kind of character-swap trick (a homograph) is designed to be almost invisible at a glance." },
    { url: "https://shopnest.com/deals", safe: true,
      explanation: "The real, plain root domain." },
    { url: "https://shopnest-bonus-rewards.win/claim", safe: false,
      explanation: "A different domain entirely, using an unusual TLD (.win) and a 'too good to be true' bonus/reward hook -- classic bait." },
    { url: "https://support.northpeakcorp.com/help", safe: true,
      explanation: "A real subdomain (support.) of the same legitimate root domain from question 1." },
    { url: "https://185.23.44.9/peaksocial-login", safe: false,
      explanation: "A raw IP address instead of a domain name. Legitimate login pages essentially never ask you to visit a bare IP address." },
  ];

  var introEl = document.getElementById("urlIntro");
  var playEl = document.getElementById("urlPlay");
  var resultsEl = document.getElementById("urlResults");
  var progressFill = document.getElementById("progressFill");
  var progressLabel = document.getElementById("progressLabel");
  var urlDisplay = document.getElementById("urlDisplay");
  var urlResult = document.getElementById("urlResult");
  var nextBtn = document.getElementById("nextUrlBtn");
  var safeBtn = document.getElementById("safeBtn");
  var suspiciousBtn = document.getElementById("suspiciousBtn");
  var urlResultsSummary = document.getElementById("urlResultsSummary");
  var urlReview = document.getElementById("urlReview");

  var pool = [];
  var index = 0;
  var score = 0;
  var missed = [];
  var answered = false;

  function shuffle(arr) {
    for (var i = arr.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var tmp = arr[i]; arr[i] = arr[j]; arr[j] = tmp;
    }
    return arr;
  }

  function start() {
    pool = shuffle(ROUND.slice());
    index = 0;
    score = 0;
    missed = [];
    introEl.style.display = "none";
    resultsEl.style.display = "none";
    playEl.style.display = "";
    renderRound();
  }

  function renderRound() {
    answered = false;
    var item = pool[index];
    urlDisplay.textContent = item.url;
    urlResult.textContent = "";
    urlResult.className = "demo-result";
    nextBtn.style.display = "none";
    safeBtn.disabled = false;
    suspiciousBtn.disabled = false;
    progressLabel.textContent = "URL " + (index + 1) + " of " + pool.length + " — Score: " + score;
    progressFill.style.width = Math.round((index / pool.length) * 100) + "%";
  }

  function answer(guessSafe) {
    if (answered) return;
    answered = true;
    safeBtn.disabled = true;
    suspiciousBtn.disabled = true;

    var item = pool[index];
    var correct = guessSafe === item.safe;
    if (correct) score++;
    else missed.push(item);

    urlResult.textContent = (correct ? "Correct. " : "Not quite. ") + item.explanation;
    urlResult.className = "demo-result " + (correct ? "is-success" : "is-error");
    nextBtn.style.display = "";
    nextBtn.textContent = (index + 1 < pool.length) ? "Next →" : "See Results";
  }

  function next() {
    index++;
    if (index >= pool.length) return finish();
    renderRound();
  }

  function finish() {
    playEl.style.display = "none";
    resultsEl.style.display = "";
    var pct = Math.round((score / pool.length) * 100);
    urlResultsSummary.textContent = "You got " + score + " / " + pool.length + " right (" + pct + "%).";

    urlReview.innerHTML = "";
    if (missed.length > 0) {
      var heading = document.createElement("p");
      heading.className = "muted";
      heading.textContent = "Worth a second look:";
      urlReview.appendChild(heading);
      var list = document.createElement("ul");
      list.className = "red-flag-list";
      missed.forEach(function (item) {
        var li = document.createElement("li");
        li.innerHTML = "<code>" + item.url + "</code> — " + item.explanation;
        list.appendChild(li);
      });
      urlReview.appendChild(list);
    }
  }

  document.getElementById("startUrlGameBtn").addEventListener("click", start);
  document.getElementById("restartUrlGameBtn").addEventListener("click", start);
  safeBtn.addEventListener("click", function () { answer(true); });
  suspiciousBtn.addEventListener("click", function () { answer(false); });
  nextBtn.addEventListener("click", next);
})();
