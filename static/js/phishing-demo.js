(function () {
  var dataEl = document.getElementById("phishing-data");
  var select = document.getElementById("templateSelect");
  if (!dataEl || !select) return;

  var payload = JSON.parse(dataEl.textContent);
  var templates = payload.templates;
  var recipients = payload.recipients;
  var templateById = {};
  templates.forEach(function (t) { templateById[t.id] = t; });

  var emailSender = document.getElementById("emailSender");
  var emailSubject = document.getElementById("emailSubject");
  var emailBody = document.getElementById("emailBody");
  var emailLinkBtn = document.getElementById("emailLinkBtn");
  var linkPreview = document.getElementById("linkPreview");
  var redFlagList = document.getElementById("redFlagList");
  var runCampaignBtn = document.getElementById("runCampaignBtn");
  var campaignResults = document.getElementById("campaignResults");
  var clickRateBanner = document.getElementById("clickRateBanner");
  var personaList = document.getElementById("personaList");

  function renderTemplate(id) {
    var t = templateById[id];
    emailSender.textContent = t.sender_name + " <" + t.sender_address + ">";
    emailSubject.textContent = t.subject;
    emailBody.textContent = t.body;
    emailLinkBtn.textContent = t.link_text;
    linkPreview.textContent = t.link_preview;

    redFlagList.innerHTML = "";
    t.red_flags.forEach(function (flag) {
      var li = document.createElement("li");
      li.textContent = flag;
      redFlagList.appendChild(li);
    });

    campaignResults.style.display = "none";
  }

  function runCampaign() {
    var t = templateById[select.value];
    var results = recipients.map(function (r) {
      var clickChance = Math.min(1, Math.max(0, r.susceptibility * (0.5 + t.difficulty)));
      return { recipient: r, clicked: Math.random() < clickChance };
    });

    var clickedCount = results.filter(function (r) { return r.clicked; }).length;
    var rate = Math.round((clickedCount / results.length) * 100);

    clickRateBanner.textContent = "Click rate: " + rate + "% (" + clickedCount + "/" + results.length + " synthetic personas clicked)";

    personaList.innerHTML = "";
    results.forEach(function (r) {
      var row = document.createElement("div");
      row.className = "persona-row" + (r.clicked ? " is-clicked" : "");
      row.innerHTML =
        '<span class="persona-dot"></span>' +
        '<span class="persona-name">' + r.recipient.name + '</span>' +
        '<span class="persona-role muted">' + r.recipient.role + '</span>' +
        '<span class="persona-outcome">' + (r.clicked ? "Clicked" : "No click") + '</span>';
      personaList.appendChild(row);
    });

    campaignResults.style.display = "";
  }

  select.addEventListener("change", function () { renderTemplate(select.value); });
  runCampaignBtn.addEventListener("click", runCampaign);

  renderTemplate(select.value);
})();
