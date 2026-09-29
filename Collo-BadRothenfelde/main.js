// Collo – kleine Helfer: "Heute geöffnet?", heutiger Tag in der Tabelle,
// aktive Kategorie in der Speisekarte.
(function () {
  "use strict";

  // Öffnungszeiten laut Collo: Mo, Mi–So 17–23 Uhr, Di Ruhetag.
  var OPEN = 17, CLOSE = 23, REST_DAY = 2;
  var DAYS = ["Sonntag", "Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag"];

  function berlinNow() {
    try {
      var parts = new Intl.DateTimeFormat("en-US", {
        timeZone: "Europe/Berlin", weekday: "short", hour: "numeric", minute: "numeric", hour12: false
      }).formatToParts(new Date());
      var get = function (t) { return parts.find(function (p) { return p.type === t; }).value; };
      var day = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"].indexOf(get("weekday"));
      return { day: day, hour: (+get("hour")) % 24 + (+get("minute")) / 60 };
    } catch (e) {
      var d = new Date();
      return { day: d.getDay(), hour: d.getHours() + d.getMinutes() / 60 };
    }
  }

  function status(now) {
    var tomorrow = (now.day + 1) % 7;
    if (now.day === REST_DAY) return ["Heute Ruhetag · morgen ab 17 Uhr", "is-closed"];
    if (now.hour < OPEN) return ["Heute ab 17 Uhr geöffnet", ""];
    if (now.hour < CLOSE) return ["Jetzt geöffnet · bis 23 Uhr", "is-open"];
    if (tomorrow === REST_DAY) return ["Geschlossen · morgen Ruhetag, " + DAYS[(now.day + 2) % 7] + " ab 17 Uhr", "is-closed"];
    return ["Geschlossen · morgen ab 17 Uhr", "is-closed"];
  }

  var now = berlinNow();
  var el = document.querySelector("[data-status]");
  if (el) {
    var s = status(now);
    el.textContent = s[0];
    if (s[1]) el.classList.add(s[1]);
  }
  var row = document.querySelector('.hours tr[data-day="' + now.day + '"]');
  if (row) row.classList.add("is-today");

  // Höhe der Kopfleiste für die klebende Kategorienleiste
  var top = document.querySelector(".top");
  function setTop() {
    if (top) document.documentElement.style.setProperty("--top-h", top.offsetHeight + "px");
  }
  setTop();
  window.addEventListener("resize", setTop);

  // Aktive Kategorie markieren
  var chips = document.querySelectorAll(".chips a");
  if (!("IntersectionObserver" in window) || !chips.length) return;
  var byId = {};
  chips.forEach(function (a) { byId[a.getAttribute("href").slice(1)] = a; });
  var current = null;
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (!e.isIntersecting) return;
      var a = byId[e.target.id];
      if (!a || a === current) return;
      if (current) current.classList.remove("is-active");
      a.classList.add("is-active");
      current = a;
      var box = a.parentNode;
      box.scrollTo({ left: a.offsetLeft - box.clientWidth / 2 + a.clientWidth / 2, behavior: "smooth" });
    });
  }, { rootMargin: "-35% 0px -60% 0px" });
  document.querySelectorAll(".menu__sec").forEach(function (s) { io.observe(s); });
})();
