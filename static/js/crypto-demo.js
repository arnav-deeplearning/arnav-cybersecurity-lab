(function () {
  var secretInput = document.getElementById("demoSecret");
  var masterKeyInput = document.getElementById("demoMasterKey");
  var encryptBtn = document.getElementById("encryptBtn");
  var decryptBtn = document.getElementById("decryptBtn");
  var output = document.getElementById("demoOutput");
  var outSalt = document.getElementById("outSalt");
  var outIv = document.getElementById("outIv");
  var outCiphertext = document.getElementById("outCiphertext");
  var result = document.getElementById("demoResult");
  if (!secretInput || !window.crypto || !window.crypto.subtle) return;

  var PBKDF2_ITERATIONS = 250000; // lighter than the CLI tool's 480k so the browser demo stays snappy

  var state = null; // { salt: Uint8Array, iv: Uint8Array, ciphertext: ArrayBuffer }

  function bufToBase64(buf) {
    var bytes = new Uint8Array(buf);
    var binary = "";
    for (var i = 0; i < bytes.length; i++) binary += String.fromCharCode(bytes[i]);
    return btoa(binary);
  }

  function deriveKey(masterKey, salt, usages) {
    var enc = new TextEncoder();
    return crypto.subtle
      .importKey("raw", enc.encode(masterKey), "PBKDF2", false, ["deriveKey"])
      .then(function (keyMaterial) {
        return crypto.subtle.deriveKey(
          { name: "PBKDF2", salt: salt, iterations: PBKDF2_ITERATIONS, hash: "SHA-256" },
          keyMaterial,
          { name: "AES-GCM", length: 256 },
          false,
          usages
        );
      });
  }

  encryptBtn.addEventListener("click", function () {
    var secret = secretInput.value;
    var masterKey = masterKeyInput.value;
    if (!secret || !masterKey) {
      result.textContent = "Enter both a secret and a master key first.";
      return;
    }

    var salt = crypto.getRandomValues(new Uint8Array(16));
    var iv = crypto.getRandomValues(new Uint8Array(12));

    deriveKey(masterKey, salt, ["encrypt"])
      .then(function (key) {
        var enc = new TextEncoder();
        return crypto.subtle.encrypt({ name: "AES-GCM", iv: iv }, key, enc.encode(secret));
      })
      .then(function (ciphertext) {
        state = { salt: salt, iv: iv, ciphertext: ciphertext };
        outSalt.textContent = bufToBase64(salt);
        outIv.textContent = bufToBase64(iv);
        outCiphertext.textContent = bufToBase64(ciphertext);
        output.style.display = "";
        decryptBtn.disabled = false;
        result.textContent = "Encrypted with AES-256-GCM. Try decrypting with the same master key -- or change it first to see the failure case.";
        result.className = "demo-result";
      })
      .catch(function (err) {
        result.textContent = "Encryption failed: " + err.message;
        result.className = "demo-result is-error";
      });
  });

  decryptBtn.addEventListener("click", function () {
    if (!state) return;
    var masterKey = masterKeyInput.value;

    deriveKey(masterKey, state.salt, ["decrypt"])
      .then(function (key) {
        return crypto.subtle.decrypt({ name: "AES-GCM", iv: state.iv }, key, state.ciphertext);
      })
      .then(function (plaintextBuf) {
        var dec = new TextDecoder();
        result.textContent = "Decrypted: \"" + dec.decode(plaintextBuf) + "\"";
        result.className = "demo-result is-success";
      })
      .catch(function () {
        result.textContent = "Decryption failed: wrong master key, or the data was tampered with. (This is AES-GCM's authentication working correctly.)";
        result.className = "demo-result is-error";
      });
  });
})();
