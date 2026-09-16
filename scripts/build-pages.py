#!/usr/bin/env python3
"""Generate Hakmi corporate inner pages from shared template."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

HEAD = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="stylesheet" href="assets/fonts/lyon-arabic.css">
  <link rel="stylesheet" href="assets/design-guidelines.css">
  <link rel="stylesheet" href="assets/hakmi.css">
  <link rel="stylesheet" href="assets/hakmi-redesign.css">
  <link rel="stylesheet" href="assets/rtl-overrides.css">
</head>
<body class="hakmi-inner-page" data-page="{page_id}">
  <a class="skip-link" href="#content">تخطي إلى المحتوى</a>
  <div id="hakmi-site-header"></div>
  <main id="content" class="hakmi-page-main">
"""

FOOT = """
  </main>
  <div id="hakmi-site-footer"></div>
  <script src="assets/site-content.js"></script>
  <script src="assets/site-chrome.js"></script>
  <script src="assets/site-enhancements.js"></script>
</body>
</html>
"""

DEFAULT_DESC = (
    "مجموعة الحاكمي القابضة مجموعة استثمارية عائلية خاصة تمتد أعمالها عبر "
    "التطوير العقاري، ومواد البناء، والتصنيع، والغذاء، والزراعة، والتجارة "
    "وسلاسل التوريد في عدد من الأسواق الدولية."
)


def hero(eyebrow, title, lead=""):
    lead_html = f'<p class="hakmi-lead">{lead}</p>' if lead else ""
    return f"""
    <section class="hakmi-page-hero">
      <div class="hakmi-page-hero-inner">
        <p class="hakmi-eyebrow">{eyebrow}</p>
        <h1 class="hakmi-display">{title}</h1>
        {lead_html}
      </div>
    </section>"""


def section(content, alt=False):
    cls = "hakmi-page-section is-alt" if alt else "hakmi-page-section"
    return f"""
    <section class="{cls}">
      <div class="hakmi-page-section-inner">
        {content}
      </div>
    </section>"""


def write_page(filename, page_id, title, description, body):
    html = HEAD.format(title=title, description=description, page_id=page_id)
    html += body
    html += FOOT
    (ROOT / filename).write_text(html, encoding="utf-8")
    print(f"Wrote {filename}")


def about_page():
    body = hero(
        "من نحن",
        "مجموعة استثمارية عائلية خاصة",
        "مجموعة استثمارية عائلية خاصة تجمع بين رأس المال والخبرة التشغيلية والرؤية طويلة الأجل.",
    )
    body += section(
        """
        <div class="hakmi-proof-strip">
          <div class="hakmi-proof-item"><strong>منذ 1985</strong><span>مسيرة بدأت في المملكة العربية السعودية.</span></div>
          <div class="hakmi-proof-item"><strong>أسواق متعددة</strong><span>حضور واستثمارات عبر الشرق الأوسط وأوروبا وآسيا.</span></div>
          <div class="hakmi-proof-item"><strong>قطاعات متكاملة</strong><span>عقار، مواد، صناعة، غذاء، زراعة، تجارة وتوريد.</span></div>
        </div>
        <div class="hakmi-split-layout">
          <div class="hakmi-prose-measure">
            <p class="hakmi-p">مجموعة الحاكمي القابضة هي مجموعة استثمارية عائلية أسسها الأستاذ نبيل حاكمي. بدأت مسيرتها من المملكة العربية السعودية عام 1985، ونمت عبر بناء أعمال متخصصة، وتطوير شراكات طويلة الأجل، والدخول المدروس إلى قطاعات وأسواق جديدة.</p>
            <p class="hakmi-p">تغطي خبرات المجموعة اليوم التطوير العقاري، ومواد البناء والإكساء، والتصنيع، وسلاسل التوريد، والخدمات اللوجستية، والصناعات الغذائية، والاستثمار الزراعي، إلى جانب استثمارات وشراكات استراتيجية في عدد من الدول.</p>
            <p class="hakmi-p">لا تعمل المجموعة بوصفها مالكاً مالياً بعيداً عن التشغيل؛ بل تتبنى نموذجاً يجمع بين الاستثمار والإدارة والخبرة الفنية والرقابة على الأداء.</p>
            <ul class="hakmi-timeline">
              <li><time datetime="1985">1985</time><span>انطلاق الأعمال في المملكة العربية السعودية في مواد البناء والتشطيبات.</span></li>
              <li><time datetime="2000">2000s</time><span>توسع عبر قطاعات وأسواق متعددة وبناء شركات متخصصة.</span></li>
              <li><time datetime="2020">اليوم</time><span>منظومة استثمارية متكاملة تربط التطوير والصناعة والتوريد.</span></li>
            </ul>
          </div>
          <div class="hakmi-split-media">
            <div class="hakmi-leadership-slot" role="img" aria-label="موضع صورة قيادية — يُضاف بعد الاعتماد">موضع صورة قيادية<br><small>يُضاف بعد الاعتماد الرسمي</small></div>
          </div>
        </div>
        """
    )
    body += section(
        """
        <div class="hakmi-split-layout is-reverse">
          <div class="hakmi-prose-measure">
            <h2 class="hakmi-h2">ما يميزنا</h2>
            <hr class="hakmi-divider">
            <ul class="hakmi-list">
              <li>منظور مالك طويل الأجل بدلاً من الاستثمار قصير الأجل.</li>
              <li>خبرة تشغيلية مباشرة في قطاعات حقيقية ومنتجة.</li>
              <li>تكامل بين العقار ومواد البناء والتصنيع والتوريد.</li>
              <li>قدرة على العمل عبر أسواق وثقافات تنظيمية مختلفة.</li>
              <li>شبكة علاقات وشراكات وموردين وخبراء دوليين.</li>
              <li>مرونة في تأسيس الشركات الخاصة بالمشروعات والدخول في الشراكات.</li>
              <li>التزام بالثقة والجودة والمسؤولية تجاه الشركاء والمجتمعات.</li>
            </ul>
          </div>
          <div class="hakmi-notice">
            <strong>نبذة من 45 كلمة:</strong> مجموعة الحاكمي القابضة مجموعة استثمارية عائلية خاصة تأسست أعمالها في السعودية عام 1985، وتمتد خبراتها عبر التطوير العقاري ومواد البناء والتصنيع والغذاء والزراعة والتجارة. تبني المجموعة استثمارات طويلة الأجل تجمع بين رأس المال والخبرة التشغيلية والشراكات المتخصصة.
          </div>
        </div>
        """,
        alt=True,
    )
    body += section(
        """
        <h2 class="hakmi-h2">رسالة المؤسس ورئيس مجلس الإدارة</h2>
        <hr class="hakmi-divider">
        <div class="hakmi-founder-block">
          <blockquote class="hakmi-quote">الاستثمار مسؤولية قبل أن يكون فرصة.</blockquote>
          <p class="hakmi-p">بسم الله الرحمن الرحيم</p>
          <p class="hakmi-p">منذ بدايات أعمالنا في المملكة العربية السعودية، كان هدفنا بناء عمل نثق به، ونقدم من خلاله منتجاً نعتز به، ونحفظ به حقوق عملائنا وشركائنا والعاملين معنا. ومع اتساع الأعمال وتنوع القطاعات والدول، بقيت هذه المبادئ هي الأساس الذي نعود إليه في كل قرار.</p>
          <p class="hakmi-p">تقوم مجموعة الحاكمي القابضة على رؤية بسيطة وواضحة: أن نختار الأعمال التي نفهمها، وأن نبني مؤسسات قادرة على الاستمرار، وأن نعمل مع شركاء يشاركوننا الثقة والالتزام، وأن نربط نجاح الاستثمار بقيمة حقيقية للمجتمع والاقتصاد.</p>
          <p class="hakmi-p">ننظر إلى كل مشروع بوصفه أمانة طويلة الأجل. لذلك نستثمر في الجودة، وفي الناس، وفي المعرفة، وفي بناء العلاقات التي تستمر. ونسعى في كل سوق ندخله إلى احترام خصوصيته، والعمل ضمن مؤسساته، ونقل خبراتنا إليه، والاستفادة من قدراته المحلية.</p>
          <p class="hakmi-p">تمثل سورية بالنسبة إلينا مسؤولية خاصة وفرصة للمساهمة في مرحلة جديدة من البناء والإنتاج. ونسعى من خلال استثماراتنا وشراكاتنا فيها إلى إنشاء مشروعات منتجة، وتوفير فرص عمل، ودعم الكفاءات المحلية، وتقديم نماذج تطوير تليق بتاريخ البلاد ومستقبلها.</p>
          <p class="hakmi-p">نسأل الله التوفيق والسداد، وأن يبارك في العمل الصادق النافع.</p>
          <p class="hakmi-founder-signature">نبيل حاكمي<br>المؤسس ورئيس مجلس الإدارة</p>
        </div>
        """
    )
    body += section(
        """
        <h2 class="hakmi-h2">الرؤية والرسالة والقيم</h2>
        <hr class="hakmi-divider">
        <h3 class="hakmi-h3">رؤيتنا</h3>
        <p class="hakmi-p">أن تكون مجموعة الحاكمي منصة استثمارية وتشغيلية موثوقة تبني أصولاً وشركات ومشروعات ذات قيمة مستدامة عبر القطاعات والأسواق والأجيال.</p>
        <h3 class="hakmi-h3">رسالتنا</h3>
        <p class="hakmi-p">توظيف رأس المال والخبرة التشغيلية والشراكات المتخصصة لتطوير استثمارات منتجة، ورفع كفاءة الشركات، وتحويل الفرص إلى مؤسسات وأصول ذات أثر اقتصادي واجتماعي طويل الأجل.</p>
        <h3 class="hakmi-h3">قيمنا</h3>
        <div class="hakmi-values-grid">
          <div class="hakmi-value-item"><h4>الأمانة</h4><p>حفظ الحقوق، والوضوح في الالتزامات، وربط القرار بالمسؤولية.</p></div>
          <div class="hakmi-value-item"><h4>الاستمرارية</h4><p>بناء الأعمال لتبقى وتتطور، لا لتحقيق نتائج مؤقتة.</p></div>
          <div class="hakmi-value-item"><h4>الجودة</h4><p>اعتبار الجودة منظومة تبدأ من القرار والمواصفة وتنتهي بالتشغيل وخدمة العميل.</p></div>
          <div class="hakmi-value-item"><h4>الشراكة</h4><p>اختيار الشركاء على أساس التكامل والثقة والنتائج المشتركة.</p></div>
          <div class="hakmi-value-item"><h4>الانضباط</h4><p>إدارة المخاطر والتكاليف والوقت والأداء بمنهج مؤسسي.</p></div>
          <div class="hakmi-value-item"><h4>الإنسان</h4><p>الاستثمار في الكفاءات، واحترام المجتمع، وخلق فرص ذات معنى.</p></div>
          <div class="hakmi-value-item"><h4>التعلم</h4><p>نقل الخبرات بين القطاعات والدول وتطوير المعرفة باستمرار.</p></div>
        </div>
        """,
        alt=True,
    )
    body += section(
        """
        <h2 class="hakmi-h2">نموذج المجموعة والاستثمار</h2>
        <hr class="hakmi-divider">
        <p class="hakmi-p">تعمل مجموعة الحاكمي القابضة بوصفها المالك الاستراتيجي والمنصة الجامعة لاستثماراتها. وتؤسس أو تستحوذ أو تشارك في شركات متخصصة، وتدعمها برأس المال والخبرة والعلاقات والحوكمة، مع منح فرق الإدارة المساحة اللازمة للتشغيل والمساءلة عن النتائج.</p>
        <h3 class="hakmi-h3">دورة الاستثمار</h3>
        <ol class="hakmi-list-ordered">
          <li>تحديد فرصة ذات أصل أو سوق أو احتياج حقيقي.</li>
          <li>إجراء دراسة تجارية وفنية ومالية وقانونية متكاملة.</li>
          <li>اختيار نموذج الدخول: تأسيس، استحواذ، شراكة، مشروع مشترك، أو شركة مشروع.</li>
          <li>تكوين فريق الإدارة والشركاء الفنيين والتمويليين.</li>
          <li>تطوير الأصل أو الشركة، وتحسين العمليات، وضبط الجودة والحوكمة.</li>
          <li>بناء تدفقات نقدية مستدامة وقدرة مستقلة على النمو.</li>
          <li>الاحتفاظ طويل الأجل أو إعادة تدوير رأس المال عند تحقق المنطق الاستراتيجي.</li>
        </ol>
        """
    )
    body += section(
        """
        <h2 class="hakmi-h2" id="governance">الحوكمة وإدارة المخاطر</h2>
        <hr class="hakmi-divider">
        <p class="hakmi-p">تعمل المجموعة على تطوير إطار حوكمة يوازن بين ملكية العائلة، واستقلالية الإدارة التنفيذية، والرقابة على الاستثمارات، وسرعة القرار. ويقوم الإطار على وضوح الصلاحيات، واعتماد الموازنات، ومتابعة مؤشرات الأداء، وإدارة المخاطر، والتدقيق، وتوثيق التعاملات بين الشركات.</p>
        <ul class="hakmi-list">
          <li>مجلس إدارة أو لجنة استثمار تعتمد الاستراتيجيات والصفقات الجوهرية.</li>
          <li>إدارات تنفيذية متخصصة لكل شركة وقطاع.</li>
          <li>موازنات وخطط سنوية ومؤشرات أداء قابلة للقياس.</li>
          <li>إدارة مركزية للمخاطر القانونية والمالية والسمعة والامتثال.</li>
          <li>سياسات واضحة للمشتريات والعقود والتفويض وتعارض المصالح.</li>
          <li>تدقيق مالي وتقارير دورية على مستوى الشركات والمشروعات.</li>
        </ul>
        """,
        alt=True,
    )
    body += section(
        """
        <h2 class="hakmi-h2">الاستثمار الذي يبقى أثره</h2>
        <hr class="hakmi-divider">
        <p class="hakmi-p">ترى مجموعة الحاكمي القابضة أن دورها لا يقتصر على تمويل المشروعات، بل يشمل بناء القدرات المحلية، ورفع المعايير، وخلق فرص العمل، ودعم الموردين والشركات، وتطوير أصول تخدم الاقتصاد والمجتمع على المدى الطويل.</p>
        <div class="hakmi-page-grid is-3">
          <article class="hakmi-data-card"><h3>العمل والمهارات</h3><p>توظيف وتدريب الكفاءات ونقل الخبرة إلى فرق محلية.</p></article>
          <article class="hakmi-data-card"><h3>الاقتصاد المحلي</h3><p>تحريك الإنشاء والصناعة والخدمات والتجارة وسلاسل التوريد.</p></article>
          <article class="hakmi-data-card"><h3>الجودة العمرانية</h3><p>إنشاء مجتمعات ومبانٍ ومرافق ترفع مستوى الاستخدام والقيمة.</p></article>
          <article class="hakmi-data-card"><h3>الإنتاج</h3><p>دعم الزراعة والصناعة والغذاء وتحويل الموارد إلى منتجات.</p></article>
          <article class="hakmi-data-card"><h3>الاستدامة</h3><p>رفع كفاءة الموارد، واختيار مواد وتقنيات طويلة العمر، وتحسين التشغيل.</p></article>
          <article class="hakmi-data-card"><h3>المبادرات المجتمعية</h3><p>تطوير مبادرات وصناديق مستقلة مرتبطة بالمشروعات عند اعتمادها، مثل التوجه التنموي لمشروع حمص أفينيو.</p></article>
        </div>
        """
    )
    write_page("about.html", "about", "من نحن | مجموعة الحاكمي القابضة", DEFAULT_DESC, body)


def sectors_page():
    cards = ""
    icons = [
        '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M3 21h18v-2H3v2zm2-4h14V5H5v12zm2-2h2V7H7v8zm4 0h2V7h-2v8zm4 0h2V7h-2v8z"/></svg>',
        '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 2 2 7v2h20V7L12 2zm8 6H4v11h16V8z"/></svg>',
        '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M2 22V10l10-5 10 5v12H2zm2-2h16v-9.2L12 6.8 4 10.8V20z"/></svg>',
        '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 2C8.5 2 6 4.2 6 7.5c0 2.1 1.1 3.9 2.8 5.1L12 22l3.2-9.4C16.9 11.4 18 9.6 18 7.5 18 4.2 15.5 2 12 2z"/></svg>',
        '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 22c4-3.5 7-7.2 7-11.5C19 5.5 16 3 12 3S5 5.5 5 10.5C5 14.8 8 18.5 12 22z"/></svg>',
        '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M3 6h11v8H3V6zm13 0h5v3h-5V6zM3 16h11v2H3v-2z"/></svg>',
        '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 2l3.1 6.3L22 9.3l-5 4.9 1.2 6.9L12 18.8 5.8 21.1 7 14.2 2 9.3l6.9-1 3.1-6.3z"/></svg>',
    ]
    sectors = [
        ("التطوير العقاري", "تطوير المجتمعات السكنية والمشروعات متعددة الاستخدامات والوجهات الحضرية والسياحية، وإدارة دورة المشروع من دراسة الأرض والتخطيط والتمويل إلى التنفيذ والتسويق والتشغيل."),
        ("مواد البناء والإكساء", "تجارة وتوزيع وتوريد منتجات السيراميك والبورسلان والرخام والجرانيت والأدوات الصحية والخلاطات والمطابخ والأرضيات ومواد التركيب والعزل والتشطيبات."),
        ("التصنيع", "الاستثمار في خطوط ومصانع مرتبطة بمواد البناء والتشطيبات والمنتجات الورقية والخشبية والمنتجات الصناعية التي تخدم الأسواق المحلية والإقليمية."),
        ("الغذاء", "استثمارات في مصانع ومنشآت إنتاج غذائي تركز على الجودة والكفاءة والأمن الغذائي وخدمة أسواق المنطقة."),
        ("الزراعة والإنتاج الحيواني", "مشروعات زراعية واسعة النطاق تستند إلى الإدارة الحديثة للمياه والإنتاج وسلاسل التوريد والتصنيع الزراعي، مع فرص للتكامل مع الصناعات الغذائية."),
        ("التجارة وسلاسل التوريد", "شبكات شراء وتوريد وتخزين ونقل دولية تربط المنتجين والأسواق وتدعم شركات المجموعة ومشروعاتها في تركيا والصين وإيطاليا ودول أخرى."),
        ("الاستثمارات الاستراتيجية", "شراكات وحصص في شركات ومشروعات ذات قيمة طويلة الأجل، مع مرونة للدخول في قطاعات مالية أو صحية أو خدمية بعد استكمال التقييم والاعتماد."),
    ]
    for i, (name, summary) in enumerate(sectors):
        cards += f"""
        <article class="hakmi-sector-card hakmi-data-card" id="{name.replace(' ', '-')}">
          <div class="hakmi-sector-icon" aria-hidden="true">{icons[i]}</div>
          <h3>{name}</h3>
          <p>{summary}</p>
        </article>"""

    body = hero("قطاعاتنا", "قطاعات الأعمال", "صفحة رئيسية للقطاعات مع صفحات تفصيلية قابلة للإضافة.")
    body += section(f'<div class="hakmi-page-grid is-3 hakmi-sectors-grid">{cards}</div>')
    write_page("sectors.html", "sectors", "قطاعاتنا | مجموعة الحاكمي القابضة", DEFAULT_DESC, body)


def companies_page():
    companies = [
        ("akzirve", "Akzirve - تركيا", "assets/wp-content/uploads/logos/akzirve.png", "Akzirve", "تركيا", "التطوير والاستثمار العقاري",
         "تمثل Akzirve خبرة المجموعة في التطوير العقاري بمدينة إسطنبول، من خلال مشروعات سكنية ومختلطة الاستخدام تجمع التصميم المعاصر بالخدمات والمساحات الخضراء والمرافق الاجتماعية. وتشمل محفظتها مشروعات مثل Topkapı 29 وStrada Bahçeşehir وPega Kartal، بما يعكس خبرة في إدارة المشروعات متعددة المراحل وتطوير المنتجات السكنية والتجارية والضيافة."),
        ("bayt-alibaa", "بيت الإباء - المملكة العربية السعودية", "assets/wp-content/uploads/logos/bayt%20alibaa.jpg", "بيت الإباء", "المملكة العربية السعودية", "مواد البناء والتشطيبات",
         "بيت الإباء من شركات المجموعة ذات الخبرة الطويلة في مواد البناء والإكساء والتشطيبات. يرتكز نشاطها على تقديم منتجات وحلول متكاملة تخدم العملاء والمشروعات، مع خبرة في المعارض والتوزيع والتوريد وإدارة المنتجات والعلاقات مع المصنعين."),
        ("qimam", "قمم - المملكة العربية السعودية", "assets/wp-content/uploads/logos/qimam.png", "قمم", "المملكة العربية السعودية", "استشارات وتصنيع ولوجستيات",
         "تدعم قمم منظومة المجموعة في مواد البناء والتصنيع والتخزين والتوريد والخدمات اللوجستية. وتساهم خبراتها في رفع كفاءة سلسلة الإمداد، وضبط المواصفات، وربط الأسواق بالمصادر الصناعية المحلية والدولية."),
        ("other", "شركات واستثمارات أخرى", "assets/logo.svg", "استثمارات أخرى", "متعدد", "استثمارات عابرة للحدود",
         "تضم محفظة المجموعة شركات واستثمارات ومشروعات أخرى في التطوير العقاري بدبي، وصناعة وتجارة مواد البناء في الصين وإيطاليا وتركيا، والصناعات الغذائية في البحرين، والاستثمار الزراعي في مصر، وغيرها من الفرص والاستثمارات حول العالم. تنشر أسماء الكيانات وتفاصيلها تدريجياً بعد استكمال التوثيق القانوني والإعلامي لكل منها."),
    ]
    cards = ""
    for cid, title, logo, name, country, sector, desc in companies:
        cards += f"""
        <article class="hakmi-company-card hakmi-data-card" data-filter-card="country" data-filter-value="{country}" id="{cid}">
          <div class="hakmi-company-logo"><img src="{logo}" alt="{name}" onerror="this.src='assets/logo-gold.svg';this.alt='{name}'"></div>
          <h3>{title}</h3>
          <p>{desc}</p>
          <div class="hakmi-card-meta"><span class="hakmi-badge">{sector}</span><span class="hakmi-badge hakmi-badge-navy">{country}</span></div>
          <a class="hakmi-card-link" href="companies.html#{cid}">عرض التفاصيل <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8.59 16.59 13.17 12 8.59 7.41 10 6l6 6-6 6z"/></svg></a>
        </article>"""

    body = hero("شركاتنا", "شركات المجموعة", "المحتوى المتاح عند الإطلاق، مع ضرورة تدقيق الهيكل القانوني ونسب الملكية.")
    body += section(
        """
        <div class="hakmi-notice" style="margin-bottom:1.5rem">لا تُستخدم عبارة «شركة تابعة» إلا بعد التحقق من الملكية القانونية. عند عدم اكتمال التوثيق تستخدم صياغات: استثمار للمجموعة، شركة مرتبطة، شراكة، أو مشروع ضمن المحفظة بحسب الوضع الفعلي.</div>
        <div class="hakmi-filter-bar" data-filter-group="country" role="group" aria-label="تصفية حسب الدولة">
          <button type="button" class="hakmi-filter-btn is-active" data-filter-value="all" aria-pressed="true">الكل</button>
          <button type="button" class="hakmi-filter-btn" data-filter-value="تركيا" aria-pressed="false">تركيا</button>
          <button type="button" class="hakmi-filter-btn" data-filter-value="المملكة العربية السعودية" aria-pressed="false">السعودية</button>
          <button type="button" class="hakmi-filter-btn" data-filter-value="متعدد" aria-pressed="false">متعدد</button>
        </div>
        <div class="hakmi-page-grid is-2 hakmi-companies-grid">""" + cards + "</div>"
    )
    write_page("companies.html", "companies", "شركاتنا | مجموعة الحاكمي القابضة", DEFAULT_DESC, body)


def projects_page():
    projects = [
        ("homs-avenue", "حمص أفينيو - حمص", "سورية", "development", "قيد التطوير والتصميم والاعتمادات",
         "مشروع حضري متكامل متعدد الاستخدامات تقوده مجموعة الحاكمي القابضة بالشراكة مع الصندوق السيادي السوري، ويجمع السكن والحدائق والتعليم والمساجد والتجارة والمكاتب والضيافة والمرافق الاجتماعية ضمن مخطط واحد. يمثل المشروع نقطة انطلاق استراتيجية للمجموعة في سورية ونموذجاً للتطوير المرتبط بالأثر الاقتصادي والاجتماعي."),
        ("madinat-al-salam", "مدينة السلام - حمص", "سورية", "future", "مشروع مستقبلي قيد الدراسة والتعاقد",
         "رؤية لتطوير عمراني واسع في مدينة حمص، ضمن محفظة المجموعة المستقبلية للمشروعات السكنية والتنموية. ينشر الوصف التفصيلي والمساحة والشراكات بعد اعتماد الاتفاقات والمخططات الرسمية."),
        ("sham-heights", "شام هايتس - ريف دمشق", "سورية", "negotiation", "قيد الدراسة والتفاوض",
         "مقترح شراكة لتطوير أرض واسعة في ضاحية دوما ضمن نموذج يجمع الأرض العامة بخبرة المطور وتمويله وإدارته، ويستهدف إنشاء مجتمع عمراني متكامل على مراحل. لا ينشر بوصفه مشروعاً معتمداً إلا بعد توقيع الاتفاقات الرسمية."),
        ("ain-hur-resort", "منتجع عين حور - ريف دمشق", "سورية", "development", "قيد التطوير والدراسة الفنية والتنظيمية",
         "مشروع منتجع عقاري اصطيافي جبلي منظم يضم فللاً وأكواخاً وشققاً فندقية ومرافق خدمية ومجتمعية، ويقوم على تخطيط متدرج يحترم طبيعة الموقع ويجمع التملك بالاستخدام الموسمي والإدارة المركزية."),
    ]
    cards = ""
    for pid, title, country, status, status_label, desc in projects:
        location = title.split(" - ")[-1] if " - " in title else country
        cards += f"""
        <article class="hakmi-data-card hakmi-project-card" data-filter-card="status" data-filter-value="{status}" id="{pid}">
          <div class="hakmi-project-visual"><p class="hakmi-project-location">{location} · {country}</p></div>
          <div class="hakmi-card-meta"><span class="hakmi-status hakmi-status-{status}">{status_label}</span><span class="hakmi-badge">التطوير العقاري</span></div>
          <h3>{title}</h3>
          <p>{desc}</p>
          <a class="hakmi-card-link" href="projects.html#{pid}">تفاصيل المشروع <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8.59 16.59 13.17 12 8.59 7.41 10 6l6 6-6 6z"/></svg></a>
        </article>"""

    body = hero("المشروعات والاستثمارات", "محفظة المشروعات", "المشروعات السورية تظهر حسب حالة معتمدة: قائم، قيد التنفيذ، قيد التطوير، قيد التفاوض، أو قيد الدراسة.")
    body += section(
        """
        <div class="hakmi-filter-bar" data-filter-group="status" role="group" aria-label="تصفية حسب الحالة">
          <button type="button" class="hakmi-filter-btn is-active" data-filter-value="all" aria-pressed="true">الكل</button>
          <button type="button" class="hakmi-filter-btn" data-filter-value="development" aria-pressed="false">قيد التطوير</button>
          <button type="button" class="hakmi-filter-btn" data-filter-value="future" aria-pressed="false">مستقبلي</button>
          <button type="button" class="hakmi-filter-btn" data-filter-value="negotiation" aria-pressed="false">قيد التفاوض</button>
        </div>
        <div class="hakmi-page-grid is-2">""" + cards + """</div>
        """
    )
    write_page("projects.html", "projects", "المشروعات والاستثمارات | مجموعة الحاكمي القابضة", DEFAULT_DESC, body)


def presence_page():
    countries = [
        ("saudi", "المملكة العربية السعودية", "بداية الأعمال، ومواد البناء والإكساء والتشطيبات والتصنيع والتوريد والخدمات اللوجستية."),
        ("turkey", "تركيا", "التطوير العقاري عبر Akzirve، إلى جانب أنشطة شراء وتوريد وتصنيع مرتبطة بمواد البناء."),
        ("syria", "سورية", "منصة استثمار وتطوير جديدة تشمل مشروعات عقارية وعمرانية وصناعية قيد التطوير والدراسة والشراكة."),
        ("uae", "الإمارات العربية المتحدة", "استثمارات ومشروعات في التطوير العقاري، خصوصاً في دبي، وفق تفاصيل تعتمد قبل النشر."),
        ("bahrain", "البحرين", "استثمارات في منشآت ومصانع غذائية."),
        ("egypt", "مصر", "مشروعات واستثمارات واسعة في القطاع الزراعي والإنتاج المرتبط به."),
        ("china", "الصين", "مصادر صناعية وتجارة وتصنيع وتوريد لمواد البناء والمنتجات ذات الصلة."),
        ("italy", "إيطاليا", "علاقات واستثمارات وتجارة مرتبطة بمواد البناء والتشطيبات والمصادر الصناعية."),
    ]
    cards = "".join(
        f'<article class="hakmi-country-card" id="{cid}"><h3>{name}</h3><p>{desc}</p></article>'
        for cid, name, desc in countries
    )
    map_nodes = "".join(
        f'<span class="hakmi-map-node{" is-primary" if cid == "saudi" else ""}">{name}</span>'
        for cid, name, _ in countries
    )
    body = hero("الانتشار", "الانتشار الجغرافي", "خريطة تربط كل دولة بالقطاع والشركة أو الاستثمار المرتبط بها.")
    body += section(
        f"""
        <div class="hakmi-presence-map" aria-hidden="true">
          <p class="hakmi-presence-map-label">شبكة الأسواق</p>
          <div class="hakmi-presence-map-nodes">{map_nodes}</div>
        </div>
        <p class="hakmi-lead hakmi-prose-measure">تربط المجموعة بين أسواق الاستهلاك ومصادر الصناعة وفرص التطوير والإنتاج. ويتيح هذا الانتشار نقل الخبرة والمنتج والشريك والتمويل بين الدول، مع الحفاظ على إدارة محلية تفهم خصوصية كل سوق.</p>
        <div class="hakmi-page-grid is-4">{cards}</div>
        """
    )
    write_page("presence.html", "presence", "الانتشار | مجموعة الحاكمي القابضة", DEFAULT_DESC, body)


def news_page():
    posts = [
        ("launch-portal", "أخبار المجموعة", "2026", "إطلاق البوابة المؤسسية لمجموعة الحاكمي القابضة",
         "تعمل المجموعة على إطلاق مرجعها الرقمي الرسمي الذي يعرّف بهويتها الاستثمارية وقطاعاتها وشركاتها ومشروعاتها وانتشارها الجغرافي."),
        ("homs-avenue-update", "تطورات المشروعات", "2026", "حمص أفينيو: مشروع حضري متكامل في مرحلة التطوير والاعتمادات",
         "مشروع متعدد الاستخدامات يجمع السكن والمرافق والخدمات ضمن مخطط واحد، ويمثل نقطة انطلاق استراتيجية للمجموعة في سورية."),
        ("partnerships-open", "الشراكات والاتفاقات", "2026", "فتح قنوات استقبال فرص الشراكة والاستثمار",
         "تستقبل المجموعة استفسارات الجهات العامة وملاك الأراضي والمستثمرين والمشغلين عبر القنوات المؤسسية الرسمية."),
    ]
    cat_keys = {
        "أخبار المجموعة": "group",
        "تطورات المشروعات": "projects",
        "الشراكات والاتفاقات": "partnerships",
    }
    cards = "".join(
        f"""<article class="hakmi-data-card hakmi-news-card" id="{pid}" data-news-category="{cat_keys.get(cat, "all")}">
          <div class="hakmi-news-thumb"><time datetime="{date}">{date}</time></div>
          <span class="hakmi-badge">{cat}</span>
          <h3>{title}</h3>
          <p>{summary}</p>
          <div class="hakmi-news-meta"><span>مجموعة الحاكمي القابضة</span></div>
        </article>"""
        for pid, cat, date, title, summary in posts
    )
    filters = (
        '<button type="button" class="is-active" data-news-filter="all" aria-pressed="true">جميع الأخبار</button>'
        + '<button type="button" data-news-filter="group" aria-pressed="false">أخبار المجموعة</button>'
        + '<button type="button" data-news-filter="projects" aria-pressed="false">تطورات المشروعات</button>'
        + '<button type="button" data-news-filter="partnerships" aria-pressed="false">الشراكات والاتفاقات</button>'
    )
    body = hero("الأخبار", "الأخبار والمركز الإعلامي", "مركز واحد لجميع أخبار المجموعة والشركات والمشروعات.")
    body += section(
        f"""
        <div class="hakmi-news-layout">
          <div class="hakmi-page-grid is-2">{cards}</div>
          <aside>
            <h2 class="hakmi-h3">التصنيفات</h2>
            <div class="hakmi-news-filters" role="group" aria-label="تصفية الأخبار">{filters}</div>
            <p class="hakmi-p-muted" style="margin-top:1.25rem;font-size:0.88rem;line-height:1.75">مجموعة الحاكمي القابضة مجموعة استثمارية عائلية خاصة أسسها نبيل حاكمي، وبدأت أعمالها في المملكة العربية السعودية عام 1985. تمتد خبراتها عبر التطوير العقاري ومواد البناء والتصنيع والغذاء والزراعة والتجارة، وتدير استثمارات وشراكات في عدد من الأسواق الإقليمية والدولية.</p>
          </aside>
        </div>
        """,
        alt=True,
    )
    write_page("news.html", "news", "الأخبار | مجموعة الحاكمي القابضة", DEFAULT_DESC, body)


def partnerships_page():
    models = [
        ("تطوير عقاري", "تطوير الأراضي والمشروعات العقارية بالشراكة مع الجهات العامة أو الخاصة."),
        ("استحواذ وتوسع", "الاستحواذ أو المشاركة في شركات قائمة تحتاج إلى رأس مال وخبرة وتوسّع."),
        ("صناعة وإنتاج", "إقامة مصانع وخطوط إنتاج جديدة أو إعادة تأهيل منشآت قائمة."),
        ("زراعة وغذاء", "شراكات زراعية وغذائية متكاملة من الإنتاج إلى التصنيع والتوزيع."),
        ("توريد دولي", "اتفاقات توريد وتصنيع وتمثيل تجاري مع مصنعين دوليين."),
        ("تشغيل وتمويل", "شراكات تشغيل وإدارة وتمويل لمشروعات محددة."),
    ]
    offers = [
        "رأس مال مرن بحسب هيكل الصفقة.",
        "خبرة في تطوير المشروعات وإدارة التنفيذ والمبيعات والتشغيل.",
        "قدرات في المواد والمواصفات والمشتريات وسلاسل التوريد.",
        "شبكة دولية من الشركاء والمستشارين والمصنعين والموردين.",
        "حوكمة ومتابعة مالية وتشغيلية وربط واضح للمسؤولية بالنتائج.",
    ]
    body = hero("الشراكات", "شراكات تحول الأصول والفرص إلى مشروعات قابلة للتنفيذ.", "تبحث مجموعة الحاكمي القابضة عن شراكات تحقق تكاملاً حقيقياً في الأرض، ورأس المال، والخبرة، والتقنية، والتشغيل، والوصول إلى الأسواق.")
    body += section(
        """
        <h2 class="hakmi-h2">مجالات الشراكة</h2>
        <div class="hakmi-partnership-models">"""
        + "".join(f'<article class="hakmi-model-card"><h3>{t}</h3><p>{d}</p></article>' for t, d in models)
        + """</div>
        <h2 class="hakmi-h2">ما تقدمه المجموعة</h2>
        <div class="hakmi-offer-grid">"""
        + "".join(f'<div class="hakmi-offer-item">{o}</div>' for o in offers)
        + """</div>
        <div class="hakmi-cta-panel">
          <p>للاستفسارات المؤسسية وفرص الشراكة، تواصل عبر القنوات الرسمية.</p>
          <a class="hakmi-btn hakmi-btn-primary" href="contact.html">قدّم فرصة استثمارية</a>
        </div>
        """
    )
    write_page("partnerships.html", "partnerships", "الشراكات | مجموعة الحاكمي القابضة", DEFAULT_DESC, body)


def careers_page():
    body = hero("الوظائف", "العمل معنا والموردون", "مساران منفصلان لتقليل الرسائل العامة وتحويل التواصل إلى بيانات قابلة للمعالجة.")
    body += section(
        """
        <h2 class="hakmi-h2">العمل معنا</h2>
        <p class="hakmi-p">نبني فرقاً تجمع الخبرة والانضباط وروح المبادرة. تنشر الفرص حسب الشركة والدولة والقطاع، مع وصف واضح للمسؤوليات والمتطلبات وموقع العمل وآلية التقديم.</p>
        <form class="hakmi-form-section" action="#" method="post">
          <div class="hakmi-form-grid">
            <label><span>الاسم</span><input type="text" name="name" required></label>
            <label><span>الدولة والمدينة</span><input type="text" name="location" required></label>
            <label><span>مجال الخبرة</span><input type="text" name="field" required></label>
            <label><span>سنوات الخبرة</span><input type="text" name="experience" required></label>
            <label><span>الوظيفة المطلوبة</span><input type="text" name="role" required></label>
            <label><span>رابط LinkedIn</span><input type="url" name="linkedin"></label>
            <label class="hakmi-form-full"><span>السيرة الذاتية</span><input type="file" name="cv" accept=".pdf,.doc,.docx"></label>
            <label class="hakmi-form-full hakmi-form-check"><input type="checkbox" name="consent" required><span>الموافقة على معالجة البيانات</span></label>
          </div>
          <button type="submit" class="hakmi-btn hakmi-btn-primary" style="margin-top:1rem">إرسال الطلب</button>
        </form>
        """
    )
    body += section(
        """
        <h2 class="hakmi-h2">التسجيل كمورد أو مقاول</h2>
        <p class="hakmi-p">ترحب المجموعة بالتعاون مع الموردين والمقاولين والمكاتب الاستشارية والمصنعين المؤهلين. يخضع التسجيل للمراجعة الفنية والمالية والقانونية ولا يمثل قبولاً أو التزاماً تعاقدياً.</p>
        <form class="hakmi-form-section" action="#" method="post">
          <div class="hakmi-form-grid">
            <label><span>اسم الشركة القانوني</span><input type="text" name="company" required></label>
            <label><span>الدولة</span><input type="text" name="country" required></label>
            <label><span>القطاع والتخصص</span><input type="text" name="specialty" required></label>
            <label><span>سنوات العمل</span><input type="text" name="years" required></label>
            <label class="hakmi-form-full"><span>المشروعات المرجعية</span><textarea name="references" rows="3"></textarea></label>
            <label class="hakmi-form-full"><span>الشهادات والتراخيص</span><textarea name="certificates" rows="2"></textarea></label>
            <label class="hakmi-form-full"><span>القدرة التشغيلية</span><textarea name="capacity" rows="2"></textarea></label>
            <label class="hakmi-form-full"><span>ملف الشركة</span><input type="file" name="profile" accept=".pdf"></label>
            <label><span>بيانات التواصل</span><input type="text" name="contact" required></label>
          </div>
          <button type="submit" class="hakmi-btn hakmi-btn-secondary" style="margin-top:1rem">تسجيل كمورد</button>
        </form>
        """,
        alt=True,
    )
    write_page("careers.html", "careers", "الوظائف | مجموعة الحاكمي القابضة", DEFAULT_DESC, body)


def contact_page():
    inquiry_radios = "".join(
        f'<label class="hakmi-form-check"><input type="radio" name="inquiry" value="{t}"{" required" if i==0 else ""}> {t}</label>'
        for i, t in enumerate([
            "فرصة استثمارية", "شراكة أو أرض", "مورد أو مقاول", "إعلام",
            "توظيف", "استفسار عن شركة", "استفسار عن مشروع", "استفسار عام"
        ])
    )
    office_cards = """
          <div class="hakmi-office-cards">
            <article class="hakmi-office-card"><h3>المقر القانوني</h3><p>يضاف بعد اعتماد الكيان والعنوان الرسمي.</p></article>
            <article class="hakmi-office-card"><h3>مكتب السعودية</h3><p>يضاف العنوان والهاتف والبريد الرسمي.</p></article>
            <article class="hakmi-office-card"><h3>مكتب تركيا</h3><p>يضاف العنوان والهاتف والبريد الرسمي.</p></article>
            <article class="hakmi-office-card"><h3>مكتب سورية</h3><p>يضاف بعد تسجيل واعتماد المقر.</p></article>
          </div>
          <h2 class="hakmi-h3" style="margin-top:1.5rem">البريد المؤسسي</h2>
          <ul class="hakmi-email-list">
            <li><span>البريد العام</span><a href="mailto:info@hakmiholding.com">info@hakmiholding.com</a></li>
            <li><span>الشراكات</span><a href="mailto:investments@hakmiholding.com">investments@hakmiholding.com</a></li>
            <li><span>الإعلام</span><a href="mailto:media@hakmiholding.com">media@hakmiholding.com</a></li>
            <li><span>الوظائف</span><a href="mailto:careers@hakmiholding.com">careers@hakmiholding.com</a></li>
          </ul>"""
    body = hero("تواصل معنا", "تواصل معنا", "يسر مجموعة الحاكمي القابضة استقبال الاستفسارات المؤسسية وفرص الشراكة والاستثمار والتواصل الإعلامي وطلبات الموردين والوظائف عبر القنوات الرسمية.")
    body += section(
        f"""
        <div class="hakmi-contact-page-grid">
          <form class="hakmi-form-section" action="#" method="post">
            <h2 class="hakmi-h2">نموذج الاستفسار</h2>
            <div class="hakmi-form-grid">
              <label><span>الاسم الكامل</span><input type="text" name="name" required></label>
              <label><span>المسمى الوظيفي والجهة</span><input type="text" name="role" required></label>
              <label><span>البريد الإلكتروني</span><input type="email" name="email" required></label>
              <label><span>رقم الهاتف</span><input type="tel" name="phone" required></label>
              <fieldset class="hakmi-form-full"><legend>نوع الاستفسار</legend>{inquiry_radios}</fieldset>
              <label class="hakmi-form-full"><span>تفاصيل الاستفسار</span><textarea name="details" rows="5" required></textarea></label>
            </div>
            <button type="submit" class="hakmi-btn hakmi-btn-primary" style="margin-top:1rem">إرسال</button>
          </form>
          <div>
            <h2 class="hakmi-h2">معلومات التواصل</h2>
            {office_cards}
          </div>
        </div>
        """
    )
    write_page("contact.html", "contact", "تواصل معنا | مجموعة الحاكمي القابضة", DEFAULT_DESC, body)


def legal_page():
    body = hero("القانونية", "النصوص القانونية وسياسات الموقع", "مسودات أولية تحتاج مراجعة محامٍ وفق دولة الكيان المشغل للموقع.")
    body += section(
        """
        <div class="hakmi-legal-block" id="disclaimer">
          <h2 class="hakmi-h2">إخلاء المسؤولية</h2>
          <p class="hakmi-p">المعلومات الواردة في هذا الموقع لأغراض تعريفية عامة، ولا تشكل عرضاً للبيع أو دعوة للاستثمار أو التزاماً تعاقدياً. تخضع المشروعات والفرص والأرقام والمواعيد للاعتمادات والاتفاقات والأنظمة المعمول بها، وقد يتم تحديثها أو تعديلها دون إشعار مسبق. لا يعتمد أي قرار استثماري إلا على المستندات الرسمية الموقعة والمراجعة القانونية والمالية المستقلة.</p>
        </div>
        <div class="hakmi-legal-block" id="ip">
          <h2 class="hakmi-h2">حقوق الملكية</h2>
          <p class="hakmi-p">جميع النصوص والشعارات والصور والتصاميم والمواد المنشورة مملوكة لمجموعة الحاكمي القابضة أو مستخدمة بموجب ترخيص. لا يجوز نسخها أو إعادة استخدامها أو تعديلها أو نشرها لأغراض تجارية دون موافقة خطية مسبقة.</p>
        </div>
        <div class="hakmi-legal-block" id="privacy">
          <h2 class="hakmi-h2">الخصوصية</h2>
          <p class="hakmi-p">نجمع البيانات التي يرسلها المستخدم طوعاً عبر النماذج بهدف الرد على الاستفسارات وإدارة طلبات الشراكة والتوظيف والموردين والتواصل الإعلامي. تحفظ البيانات وفق الضوابط المعمول بها، ولا تستخدم خارج الغرض المعلن إلا بموافقة أو مسوغ قانوني.</p>
        </div>
        <div class="hakmi-legal-block" id="cookies">
          <h2 class="hakmi-h2">ملفات الارتباط</h2>
          <p class="hakmi-p">يستخدم الموقع ملفات ارتباط ضرورية للتشغيل، وقد يستخدم أدوات تحليل وقياس بعد موافقة المستخدم بحسب المتطلبات القانونية للدولة. يجب إعداد لائحة تفصيلية بالأدوات الفعلية قبل الإطلاق.</p>
        </div>
        """
    )
    write_page("legal.html", "legal", "القانونية | مجموعة الحاكمي القابضة", DEFAULT_DESC, body)


def main():
    about_page()
    sectors_page()
    companies_page()
    projects_page()
    presence_page()
    news_page()
    partnerships_page()
    careers_page()
    contact_page()
    legal_page()


if __name__ == "__main__":
    main()
