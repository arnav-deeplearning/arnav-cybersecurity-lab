(function () {
  var STORAGE_KEY = "cyberlab-cipher-progress";

  function caesarDecode(text, shift) {
    return text.replace(/[a-zA-Z]/g, function (ch) {
      var base = ch === ch.toUpperCase() ? 65 : 97;
      return String.fromCharCode(((ch.charCodeAt(0) - base - shift + 26) % 26) + base);
    });
  }

  function rot13Decode(text) { return caesarDecode(text, 13); }

  function base64Decode(text) {
    try { return atob(text); } catch (e) { return ""; }
  }

  function hexDecode(text) {
    return text.trim().split(/\s+/).map(function (byte) {
      return String.fromCharCode(parseInt(byte, 16));
    }).join("");
  }

  function bonusDecode(text) {
    // Base64 was applied last during encoding, so decoding reverses that first, then un-shifts Caesar(5).
    return caesarDecode(base64Decode(text), 5);
  }

  var LEVELS = [
    {
      id: "caesar",
      title: "Level 1: Caesar Cipher",
      method: "Caesar cipher, shift 3",
      intro: "The oldest trick in the book -- literally. Julius Caesar reportedly used this to protect military messages: every letter is shifted a fixed number of places through the alphabet.",
      ciphertext: "PHHW PH DW QRRQ",
      hint: "Each letter has been shifted forward by 3. To undo it, shift each letter back by 3 (D -> A, E -> B, ...).",
      decode: function (text) { return caesarDecode(text, 3); },
      explanation: "A Caesar cipher shifts every letter by a fixed amount (here, 3). To decode, you shift each letter backward by the same amount. It's easy to break today (only 25 possible shifts to try), but it's the direct ancestor of every substitution cipher that came after it.",
    },
    {
      id: "rot13",
      title: "Level 2: ROT13",
      method: "ROT13",
      intro: "ROT13 is a Caesar cipher with a special property: shifting by exactly 13 is its own inverse, since the alphabet has 26 letters. Encoding and decoding use the exact same operation.",
      ciphertext: "PLORE FRPHEVGL VF SHA",
      hint: "This is a Caesar shift of 13. Try applying the same shift again -- ROT13 undoes itself.",
      decode: rot13Decode,
      explanation: "ROT13 shifts every letter 13 places -- exactly half of 26. That means running ROT13 twice gets you back to the original text. It was never meant to be real security; it's historically used to hide spoilers or puzzle answers from being read at a glance.",
    },
    {
      id: "base64",
      title: "Level 3: Base64",
      method: "Base64",
      intro: "Base64 isn't encryption at all -- it's an encoding scheme that represents binary data using only readable text characters, commonly used to embed data in places that expect plain text.",
      ciphertext: "U1RBWSBTQUZFIE9OTElORQ==",
      hint: "This uses only letters, numbers, +, /, and = padding at the end -- a signature of Base64. Try decoding it with a Base64 decoder.",
      decode: base64Decode,
      explanation: "Base64 maps every 3 bytes of data into 4 printable characters. It's reversible by anyone -- there's no secret key -- so it should never be mistaken for encryption, even though it visually looks like a 'code.'",
    },
    {
      id: "hex",
      title: "Level 4: Hexadecimal",
      method: "Hex encoding",
      intro: "Every character in a computer is ultimately a number. Hex encoding just writes each character's numeric code in base 16 instead of base 10.",
      ciphertext: "48 41 43 4b 20 54 48 45 20 50 4c 41 4e 45 54",
      hint: "Each pair of characters is one letter's ASCII code in hex. 48 in hex is 72 in decimal, which is the letter 'H'.",
      decode: hexDecode,
      explanation: "Each pair of hex digits represents one byte -- one character. Hex shows up constantly in security work, from reading memory dumps to inspecting raw network packets.",
    },
    {
      id: "bonus",
      title: "Bonus Level: Layered Encoding",
      method: "Caesar (shift 5) + Base64",
      intro: "Real obfuscation often stacks simple techniques together. This message was Caesar-shifted by 5, then the result was Base64 encoded. You'll need to undo both, in the right order.",
      ciphertext: "WVdaWFkgR1pZIEFKV05LRA==",
      hint: "Base64-decode it first to get the shifted letters, then Caesar-decode with shift 5 to get the original message.",
      decode: bonusDecode,
      explanation: "Encoding was applied Caesar-first, then Base64. To reverse it, you undo in the opposite order: Base64-decode first, then shift the letters back by 5. This is exactly how attackers sometimes layer simple encodings to slip past naive detection -- and exactly why analysts learn to peel them back one layer at a time.",
    },
  ];

  var tracker = document.getElementById("levelTracker");
  var cipherCard = document.getElementById("cipherCard");
  var cipherComplete = document.getElementById("cipherComplete");
  var cipherMethod = document.getElementById("cipherMethod");
  var cipherTitle = document.getElementById("cipherTitle");
  var cipherIntro = document.getElementById("cipherIntro");
  var cipherText = document.getElementById("cipherText");
  var cipherGuess = document.getElementById("cipherGuess");
  var cipherResult = document.getElementById("cipherResult");
  var cipherExplanation = document.getElementById("cipherExplanation");
  var nextLevelBtn = document.getElementById("nextLevelBtn");
  var checkBtn = document.getElementById("checkAnswerBtn");
  var hintBtn = document.getElementById("hintBtn");
  var revealBtn = document.getElementById("revealBtn");

  var currentIndex = 0;
  var solved = false;

  function loadCompleted() {
    try { return JSON.parse(localStorage.getItem(STORAGE_KEY)) || []; }
    catch (e) { return []; }
  }
  function saveCompleted(list) {
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(list)); } catch (e) { /* ignore */ }
  }

  function renderTracker() {
    var completed = loadCompleted();
    tracker.innerHTML = "";
    LEVELS.forEach(function (level, i) {
      var pill = document.createElement("span");
      pill.className = "cipher-pill" + (completed.indexOf(level.id) > -1 ? " is-done" : "") + (i === currentIndex ? " is-current" : "");
      pill.textContent = (completed.indexOf(level.id) > -1 ? "✓ " : "") + (i + 1);
      tracker.appendChild(pill);
    });
  }

  function normalize(text) {
    return text.trim().toUpperCase().replace(/\s+/g, " ");
  }

  function renderLevel() {
    if (currentIndex >= LEVELS.length) {
      cipherCard.style.display = "none";
      cipherComplete.style.display = "";
      renderTracker();
      return;
    }
    cipherCard.style.display = "";
    cipherComplete.style.display = "none";
    solved = false;

    var level = LEVELS[currentIndex];
    cipherMethod.textContent = level.method;
    cipherTitle.textContent = level.title;
    cipherIntro.textContent = level.intro;
    cipherText.textContent = level.ciphertext;
    cipherGuess.value = "";
    cipherGuess.disabled = false;
    cipherResult.textContent = "";
    cipherResult.className = "demo-result";
    cipherExplanation.style.display = "none";
    nextLevelBtn.style.display = "none";
    checkBtn.disabled = false;

    renderTracker();
  }

  function checkAnswer() {
    var level = LEVELS[currentIndex];
    var actual = level.decode(level.ciphertext);
    var guess = cipherGuess.value;
    if (normalize(guess) === normalize(actual)) {
      solved = true;
      cipherResult.textContent = "Correct! The message reads: \"" + actual + "\"";
      cipherResult.className = "demo-result is-success";
      cipherExplanation.style.display = "";
      cipherExplanation.textContent = level.explanation;
      nextLevelBtn.style.display = "";
      nextLevelBtn.textContent = (currentIndex + 1 < LEVELS.length) ? "Next Challenge →" : "Finish";
      checkBtn.disabled = true;
      cipherGuess.disabled = true;

      var completed = loadCompleted();
      if (completed.indexOf(level.id) === -1) {
        completed.push(level.id);
        saveCompleted(completed);
      }
      renderTracker();
    } else {
      cipherResult.textContent = "Not quite -- try again, or use a hint.";
      cipherResult.className = "demo-result is-error";
    }
  }

  checkBtn.addEventListener("click", checkAnswer);
  cipherGuess.addEventListener("keydown", function (e) { if (e.key === "Enter") checkAnswer(); });

  hintBtn.addEventListener("click", function () {
    var level = LEVELS[currentIndex];
    cipherResult.textContent = "Hint: " + level.hint;
    cipherResult.className = "demo-result";
  });

  revealBtn.addEventListener("click", function () {
    var level = LEVELS[currentIndex];
    var actual = level.decode(level.ciphertext);
    cipherGuess.value = actual;
    checkAnswer();
  });

  nextLevelBtn.addEventListener("click", function () {
    currentIndex++;
    renderLevel();
  });

  document.getElementById("restartCipherBtn").addEventListener("click", function () {
    currentIndex = 0;
    renderLevel();
  });

  renderLevel();
})();
