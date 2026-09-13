(function () {
  var dataEl = document.getElementById("flashcards-data");
  if (!dataEl) return;
  var payload = JSON.parse(dataEl.textContent);
  var allCards = payload.cards;

  var STORAGE_KEY = "cyberlab-flashcards-progress";
  var levelSelect = document.getElementById("levelSelect");
  var categorySelect = document.getElementById("categorySelect");
  var stage = document.getElementById("flashcardStage");
  var card = document.getElementById("flashcard");
  var cardLevel = document.getElementById("cardLevel");
  var cardTerm = document.getElementById("cardTerm");
  var cardDefinition = document.getElementById("cardDefinition");
  var cardExample = document.getElementById("cardExample");
  var progressFill = document.getElementById("progressFill");
  var progressLabel = document.getElementById("progressLabel");
  var deckEmpty = document.getElementById("deckEmpty");
  var deckSummary = document.getElementById("deckSummary");

  var deck = [];
  var index = 0;

  function loadProgress() {
    try { return JSON.parse(localStorage.getItem(STORAGE_KEY)) || {}; }
    catch (e) { return {}; }
  }
  function saveProgress(progress) {
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(progress)); } catch (e) { /* ignore */ }
  }

  function shuffle(arr) {
    for (var i = arr.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var tmp = arr[i]; arr[i] = arr[j]; arr[j] = tmp;
    }
    return arr;
  }

  function buildDeck() {
    var level = levelSelect.value;
    var category = categorySelect.value;
    deck = allCards.filter(function (c) {
      return (level === "all" || c.level === level) && (category === "all" || c.category === category);
    });
    index = 0;
    render();
  }

  function render() {
    if (deck.length === 0) {
      stage.style.display = "none";
      document.querySelector(".deck-actions").style.display = "none";
      deckEmpty.style.display = "";
      deckSummary.textContent = "No cards match this filter -- try a different level or category.";
      progressLabel.textContent = "";
      progressFill.style.width = "0%";
      return;
    }
    if (index >= deck.length) {
      stage.style.display = "none";
      document.querySelector(".deck-actions").style.display = "none";
      deckEmpty.style.display = "";
      var progress = loadProgress();
      var mastered = deck.filter(function (c) { return progress[c.id] === "known"; }).length;
      deckSummary.textContent = "You reviewed " + deck.length + " cards -- " + mastered + " marked Got It, " + (deck.length - mastered) + " still learning.";
      return;
    }

    stage.style.display = "";
    document.querySelector(".deck-actions").style.display = "";
    deckEmpty.style.display = "none";
    card.classList.remove("is-flipped");

    var c = deck[index];
    cardLevel.textContent = c.level;
    cardTerm.textContent = c.term;
    cardDefinition.textContent = c.definition;
    cardExample.textContent = c.example ? "Example: " + c.example : "";

    var progress = loadProgress();
    var known = deck.filter(function (d) { return progress[d.id] === "known"; }).length;
    var learning = deck.filter(function (d) { return progress[d.id] === "learning"; }).length;
    progressLabel.textContent = "Card " + (index + 1) + " of " + deck.length + " — " + known + " known, " + learning + " still learning";
    progressFill.style.width = Math.round(((index) / deck.length) * 100) + "%";
  }

  function mark(status) {
    if (index >= deck.length) return;
    var progress = loadProgress();
    progress[deck[index].id] = status;
    saveProgress(progress);
    index++;
    render();
  }

  card.addEventListener("click", function () { card.classList.toggle("is-flipped"); });
  document.addEventListener("keydown", function (e) {
    if (e.code === "Space" && stage.style.display !== "none") {
      e.preventDefault();
      card.classList.toggle("is-flipped");
    }
  });

  document.getElementById("gotItBtn").addEventListener("click", function () { mark("known"); });
  document.getElementById("stillLearningBtn").addEventListener("click", function () { mark("learning"); });
  document.getElementById("nextBtn").addEventListener("click", function () {
    if (deck.length === 0) return;
    index = Math.min(index + 1, deck.length);
    render();
  });
  document.getElementById("prevBtn").addEventListener("click", function () {
    if (deck.length === 0) return;
    index = Math.max(index - 1, 0);
    render();
  });
  document.getElementById("shuffleBtn").addEventListener("click", function () {
    shuffle(deck);
    index = 0;
    render();
  });
  document.getElementById("resetProgressBtn").addEventListener("click", function () {
    saveProgress({});
    render();
  });
  document.getElementById("restartBtn").addEventListener("click", function () {
    index = 0;
    render();
  });

  levelSelect.addEventListener("change", buildDeck);
  categorySelect.addEventListener("change", buildDeck);

  buildDeck();
})();
