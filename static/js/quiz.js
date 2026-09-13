(function () {
  var dataEl = document.getElementById("quiz-data");
  if (!dataEl) return;
  var payload = JSON.parse(dataEl.textContent);
  var allQuestions = payload.questions;

  var STORAGE_KEY = "cyberlab-quiz-best-scores";
  var levelSelect = document.getElementById("levelSelect");
  var categorySelect = document.getElementById("categorySelect");
  var questionCountLabel = document.getElementById("questionCountLabel");
  var bestScoreLabel = document.getElementById("bestScoreLabel");
  var startBtn = document.getElementById("startQuizBtn");

  var setupEl = document.getElementById("quizSetup");
  var playEl = document.getElementById("quizPlay");
  var resultsEl = document.getElementById("quizResults");

  var progressFill = document.getElementById("progressFill");
  var progressLabel = document.getElementById("progressLabel");
  var questionLevel = document.getElementById("questionLevel");
  var questionText = document.getElementById("questionText");
  var quizOptions = document.getElementById("quizOptions");
  var quizExplanation = document.getElementById("quizExplanation");
  var nextBtn = document.getElementById("nextQuestionBtn");
  var resultsSummary = document.getElementById("resultsSummary");

  var pool = [];
  var index = 0;
  var score = 0;
  var answered = false;

  function loadBestScores() {
    try { return JSON.parse(localStorage.getItem(STORAGE_KEY)) || {}; }
    catch (e) { return {}; }
  }
  function saveBestScore(key, score, total) {
    var scores = loadBestScores();
    var pct = Math.round((score / total) * 100);
    if (!scores[key] || pct > scores[key]) {
      scores[key] = pct;
      try { localStorage.setItem(STORAGE_KEY, JSON.stringify(scores)); } catch (e) { /* ignore */ }
    }
  }

  function currentKey() {
    return levelSelect.value + "|" + categorySelect.value;
  }

  function shuffle(arr) {
    for (var i = arr.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var tmp = arr[i]; arr[i] = arr[j]; arr[j] = tmp;
    }
    return arr;
  }

  function updateSetupLabels() {
    var level = levelSelect.value;
    var category = categorySelect.value;
    var matches = allQuestions.filter(function (q) {
      return (level === "all" || q.level === level) && (category === "all" || q.category === category);
    });
    questionCountLabel.textContent = matches.length + " question" + (matches.length === 1 ? "" : "s") + " in this selection.";
    var best = loadBestScores()[currentKey()];
    bestScoreLabel.textContent = best !== undefined ? ("Best score so far: " + best + "%") : "";
    startBtn.disabled = matches.length === 0;
  }

  function startQuiz() {
    var level = levelSelect.value;
    var category = categorySelect.value;
    pool = shuffle(allQuestions.filter(function (q) {
      return (level === "all" || q.level === level) && (category === "all" || q.category === category);
    }).slice());
    index = 0;
    score = 0;
    setupEl.style.display = "none";
    resultsEl.style.display = "none";
    playEl.style.display = "";
    renderQuestion();
  }

  function renderQuestion() {
    answered = false;
    nextBtn.style.display = "none";
    quizExplanation.style.display = "none";

    var q = pool[index];
    questionLevel.textContent = q.level;
    questionText.textContent = q.question;
    progressLabel.textContent = "Question " + (index + 1) + " of " + pool.length + " — Score: " + score;
    progressFill.style.width = Math.round((index / pool.length) * 100) + "%";

    quizOptions.innerHTML = "";
    q.options.forEach(function (option, i) {
      var btn = document.createElement("button");
      btn.type = "button";
      btn.className = "quiz-option";
      btn.textContent = option;
      btn.addEventListener("click", function () { selectAnswer(i); });
      quizOptions.appendChild(btn);
    });
  }

  function selectAnswer(i) {
    if (answered) return;
    answered = true;
    var q = pool[index];
    var buttons = quizOptions.querySelectorAll(".quiz-option");
    buttons.forEach(function (btn, idx) {
      btn.classList.add("is-disabled");
      if (idx === q.correct_index) btn.classList.add("is-correct");
      else if (idx === i) btn.classList.add("is-incorrect");
    });
    if (i === q.correct_index) score++;

    quizExplanation.style.display = "";
    quizExplanation.textContent = (i === q.correct_index ? "Correct. " : "Not quite. ") + q.explanation;
    quizExplanation.className = "quiz-explanation " + (i === q.correct_index ? "is-correct" : "is-incorrect");

    nextBtn.style.display = "";
    nextBtn.textContent = (index + 1 < pool.length) ? "Next Question →" : "See Results";
  }

  function nextQuestion() {
    index++;
    if (index >= pool.length) {
      finishQuiz();
      return;
    }
    renderQuestion();
  }

  function finishQuiz() {
    playEl.style.display = "none";
    resultsEl.style.display = "";
    var pct = Math.round((score / pool.length) * 100);
    saveBestScore(currentKey(), score, pool.length);
    var best = loadBestScores()[currentKey()];
    resultsSummary.textContent = "You scored " + score + " / " + pool.length + " (" + pct + "%). Best score for this selection: " + best + "%.";
  }

  startBtn.addEventListener("click", startQuiz);
  nextBtn.addEventListener("click", nextQuestion);
  levelSelect.addEventListener("change", updateSetupLabels);
  categorySelect.addEventListener("change", updateSetupLabels);
  document.getElementById("retryQuizBtn").addEventListener("click", function () {
    resultsEl.style.display = "none";
    setupEl.style.display = "";
    updateSetupLabels();
  });

  updateSetupLabels();
})();
