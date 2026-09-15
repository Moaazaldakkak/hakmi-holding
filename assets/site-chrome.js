(function () {
  "use strict";

  var nav = (window.HAKMI && window.HAKMI.nav) || [];
  var pageId = document.body.getAttribute("data-page") || "";

  function isActive(item) {
    if (item.id === pageId) return true;
    if (item.children) {
      return item.children.some(function (child) {
        return child.id === pageId;
      });
    }
    return false;
  }

  function renderNavItems(items, onDark) {
    return items
      .map(function (item) {
        var active = isActive(item);
        var linkClass = onDark ? "hakmi-link-on-dark" : "hakmi-link-nav";
        if (item.children) {
          var sub = item.children
            .map(function (child) {
              return (
                '<li><a href="' +
                child.href +
                '"' +
                (child.id === pageId ? ' aria-current="page"' : "") +
                ">" +
                child.label +
                "</a></li>"
              );
            })
            .join("");
          return (
            '<li class="hakmi-nav-item' +
            (active ? " is-active" : "") +
            '">' +
            '<a class="' +
            linkClass +
            '" href="#" aria-haspopup="true">' +
            item.label +
            "</a>" +
            '<ul class="hakmi-nav-sub">' +
            sub +
            "</ul></li>"
          );
        }
        return (
          '<li class="hakmi-nav-item' +
          (active ? " is-active" : "") +
          '">' +
          '<a class="' +
          linkClass +
          '" href="' +
          item.href +
          '"' +
          (item.id === pageId ? ' aria-current="page"' : "") +
          ">" +
          item.label +
          "</a></li>"
        );
      })
      .join("");
  }

  function renderHeader() {
    var mount = document.getElementById("hakmi-site-header");
    if (!mount) return;

    var inner = document.body.classList.contains("hakmi-inner-page");
    mount.innerHTML =
      '<header class="hakmi-header' +
      (inner ? " hakmi-header-inner-page" : "") +
      '" id="hakmi-header">' +
      '<div class="hakmi-header-inner">' +
      '<a class="hakmi-header-logo" href="index.html">' +
      '<img src="assets/logo_white.svg" width="423" height="284" alt="مجموعة الحاكمي القابضة">' +
      "</a>" +
      '<button class="hakmi-nav-toggle" type="button" aria-expanded="false" aria-controls="hakmi-nav" aria-label="القائمة">' +
      "<span></span><span></span><span></span>" +
      "</button>" +
      '<nav aria-label="التنقل الرئيسي">' +
      '<ul class="hakmi-nav" id="hakmi-nav">' +
      renderNavItems(nav, true) +
      "</ul></nav>" +
      '<div class="hakmi-header-actions">' +
      '<a class="hakmi-btn hakmi-btn-light hakmi-btn-sm" href="contact.html">تواصل معنا</a>' +
      "</div></div></header>";

    var header = document.getElementById("hakmi-header");
    var toggle = header.querySelector(".hakmi-nav-toggle");
    var more = header.querySelector(".hakmi-nav-item:has(.hakmi-nav-sub) > a");

    if (toggle) {
      toggle.addEventListener("click", function () {
        var open = header.classList.toggle("is-open");
        toggle.setAttribute("aria-expanded", open ? "true" : "false");
      });
    }
    if (more) {
      more.addEventListener("click", function (e) {
        if (window.matchMedia("(max-width: 1024px)").matches) {
          e.preventDefault();
          more.parentElement.classList.toggle("is-open");
        }
      });
    }
  }

  function renderFooter() {
    var mount = document.getElementById("hakmi-site-footer");
    if (!mount) return;

    mount.innerHTML =
      '<footer class="hakmi-site-footer">' +
      '<div class="hakmi-footer-inner">' +
      '<div class="hakmi-footer-grid">' +
      '<div class="hakmi-footer-col hakmi-footer-brand">' +
      '<a class="hakmi-footer-logo" href="index.html">' +
      '<img src="assets/logo_white.svg" alt="مجموعة الحاكمي القابضة">' +
      "</a>" +
      '<p class="hakmi-footer-slogan">شراكات قوية. أصول منتجة. قيمة تستمر.</p>' +
      "</div>" +
      '<div class="hakmi-footer-col">' +
      "<h3>الملاحة السريعة</h3>" +
      "<ul>" +
      '<li><a href="about.html">من نحن</a></li>' +
      '<li><a href="sectors.html">قطاعاتنا</a></li>' +
      '<li><a href="companies.html">شركاتنا</a></li>' +
      '<li><a href="projects.html">المشروعات</a></li>' +
      '<li><a href="presence.html">الانتشار</a></li>' +
      "</ul></div>" +
      '<div class="hakmi-footer-col">' +
      "<h3>الامتثال والشفافية</h3>" +
      "<ul>" +
      '<li><a href="legal.html#privacy">سياسة الخصوصية</a></li>' +
      '<li><a href="legal.html#disclaimer">إخلاء المسؤولية</a></li>' +
      '<li><a href="legal.html#cookies">ملفات الارتباط</a></li>' +
      '<li><a href="partnerships.html">الشراكات</a></li>' +
      "</ul></div>" +
      '<div class="hakmi-footer-col">' +
      "<h3>التواصل</h3>" +
      "<p>يسر المجموعة استقبال الاستفسارات المؤسسية عبر القنوات الرسمية.</p>" +
      '<p><a href="contact.html">تواصل معنا</a></p>' +
      "</div></div>" +
      '<div class="hakmi-footer-bar">' +
      "<p>© 2026 مجموعة الحاكمي القابضة – جميع الحقوق محفوظة</p>" +
      "</div></div></footer>";
  }

  function initFilters() {
    document.querySelectorAll("[data-filter-group]").forEach(function (group) {
      var key = group.getAttribute("data-filter-group");
      var buttons = group.querySelectorAll("[data-filter-value]");
      var cards = document.querySelectorAll('[data-filter-card="' + key + '"]');
      if (!buttons.length || !cards.length) return;

      buttons.forEach(function (btn) {
        btn.addEventListener("click", function () {
          var value = btn.getAttribute("data-filter-value");
          buttons.forEach(function (b) {
            b.classList.toggle("is-active", b === btn);
            b.setAttribute("aria-pressed", b === btn ? "true" : "false");
          });
          cards.forEach(function (card) {
            var match = value === "all" || card.getAttribute("data-filter-value") === value;
            card.hidden = !match;
          });
        });
      });
    });
  }

  renderHeader();
  renderFooter();
  initFilters();
})();
