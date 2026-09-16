(function () {
  "use strict";

  var reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function initNav() {
    var header = document.getElementById("hakmi-header");
    if (!header) return;

    var toggle = header.querySelector(".hakmi-nav-toggle");
    var dropdownItems = header.querySelectorAll(".hakmi-nav-item:has(.hakmi-nav-sub)");

    if (toggle) {
      toggle.addEventListener("click", function () {
        var open = header.classList.toggle("is-open");
        toggle.setAttribute("aria-expanded", open ? "true" : "false");
      });
    }

    dropdownItems.forEach(function (item) {
      var trigger = item.querySelector(":scope > a");
      if (!trigger) return;

      trigger.addEventListener("click", function (e) {
        e.preventDefault();
        var isOpen = item.classList.toggle("is-open");
        trigger.setAttribute("aria-expanded", isOpen ? "true" : "false");
        dropdownItems.forEach(function (other) {
          if (other !== item) {
            other.classList.remove("is-open");
            var otherTrigger = other.querySelector(":scope > a");
            if (otherTrigger) otherTrigger.setAttribute("aria-expanded", "false");
          }
        });
      });

      document.addEventListener("click", function (e) {
        if (!item.contains(e.target)) {
          item.classList.remove("is-open");
          trigger.setAttribute("aria-expanded", "false");
        }
      });
    });
  }

  function initReveal() {
    document.documentElement.classList.add("hakmi-js");
    var items = document.querySelectorAll(".hakmi-reveal");
    if (!items.length) return;

    if (reducedMotion) {
      items.forEach(function (el) {
        el.classList.add("is-visible");
      });
      return;
    }

    if (!("IntersectionObserver" in window)) {
      items.forEach(function (el) {
        el.classList.add("is-visible");
      });
      return;
    }

    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        });
      },
      { rootMargin: "0px 0px -60px 0px", threshold: 0.08 }
    );

    items.forEach(function (el) {
      observer.observe(el);
    });
  }

  function initForms() {
    document.querySelectorAll(".hakmi-contact-form, .hakmi-form-section").forEach(function (form) {
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        form.reset();
        var note = form.querySelector(".hakmi-contact-note");
        if (note) {
          note.textContent = "تم استلام طلبكم. سيتواصل الفريق خلال يوم عمل واحد.";
        }
      });
    });
  }

  function initNewsFilters() {
    document.querySelectorAll("[data-news-filter]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var value = btn.getAttribute("data-news-filter");
        var buttons = btn.closest(".hakmi-news-filters").querySelectorAll("[data-news-filter]");
        var cards = document.querySelectorAll(".hakmi-news-card[data-news-category]");
        buttons.forEach(function (b) {
          b.classList.toggle("is-active", b === btn);
          b.setAttribute("aria-pressed", b === btn ? "true" : "false");
        });
        cards.forEach(function (card) {
          var match = value === "all" || card.getAttribute("data-news-category") === value;
          card.hidden = !match;
        });
      });
    });
  }

  initNav();
  initReveal();
  initForms();
  initNewsFilters();
})();
