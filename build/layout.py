# -*- coding: utf-8 -*-
import re

from partials import *

DOC = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<meta name="description" content="__DESC__">
<link rel="canonical" href="https://kirosys.in/__SLUG__">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Kirosys Technology">
<meta property="og:title" content="__TITLE__">
<meta property="og:description" content="__DESC__">
<meta property="og:url" content="https://kirosys.in/__SLUG__">
<meta property="og:image" content="https://kirosys.in/assets/img/og-cover.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#020D1C">
<link rel="icon" href="assets/img/icon-32.png" sizes="32x32" type="image/png">
<link rel="icon" href="assets/img/icon-512.png" sizes="512x512" type="image/png">
<link rel="apple-touch-icon" href="assets/img/icon-180.png">
<link rel="manifest" href="site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&amp;display=swap">
<link rel="stylesheet" href="assets/site.css">
<script>document.documentElement.classList.add("js");</script>
__EXTRAHEAD__
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
__TOPBAR__
__HEADER__
<main id="main">
__BODY__
</main>
__FOOTER__
<script src="assets/site.js" defer></script>
</body>
</html>
"""

JSONLD = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Kirosys Technology",
  "legalName": "Kirosys Technology",
  "url": "https://kirosys.in/",
  "logo": "https://kirosys.in/assets/img/logo-720.png",
  "image": "https://kirosys.in/assets/img/og-cover.jpg",
  "description": "Kirosys Technology is a software development and IT services company building secure, scalable and future-ready digital solutions.",
  "foundingDate": "2023-07-13",
  "email": "support@kirosys.in",
  "telephone": "+91-82988-66066",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "New Dariyapur Colony, Suryamandir, Khairatali",
    "addressLocality": "Patna",
    "postalCode": "804453",
    "addressRegion": "Bihar",
    "addressCountry": "IN"
  },
  "areaServed": "IN",
  "knowsAbout": ["Custom software development","Mobile app development","Cloud and DevOps","AI and data solutions","IT consulting","Web and portal development"]
}
</script>"""


def topbar():
    return ('<div class="topbar">\n  <div class="container topbar-inner">\n'
            '    <span class="topbar-tag">Building secure, scalable and future-ready solutions</span>\n'
            '    <div class="topbar-right">\n'
            '      <a href="mailto:%s">%s<span>%s</span></a>\n'
            '      <a href="tel:%s">%s<span>%s</span></a>\n'
            '      <!-- Social profiles: add the real URLs, then delete these comment markers.\n'
            '      <span class="topbar-social">\n'
            '        <a href="" aria-label="Kirosys on LinkedIn">%s</a>\n'
            '        <a href="" aria-label="Kirosys on GitHub">%s</a>\n'
            '        <a href="" aria-label="Kirosys on YouTube">%s</a>\n'
            '      </span>\n      -->\n'
            '    </div>\n  </div>\n</div>\n'
            % (EMAIL, icon("mail"), EMAIL, PHONE_HREF, icon("phone"), PHONE_DISPLAY,
               icon("linkedin"), icon("github"), icon("youtube")))


def header(active):
    links = "".join(
        '<a href="%s"%s>%s</a>' % (href, ' aria-current="page"' if href == active else "", label)
        for href, label in NAV)
    mob = "".join(
        '<a href="%s"%s>%s</a>' % (href, ' aria-current="page"' if href == active else "", label)
        for href, label in NAV)
    return """<header class="site-header">
  <div class="container nav">
    <a class="brand" href="index.html" aria-label="Kirosys Technology &mdash; home">
      <img src="assets/img/mark-128.png" alt="" width="38" height="38" decoding="async">
      <span class="brand-text"><span class="brand-name">KIROSYS</span><span class="brand-sub">Technology</span></span>
    </a>
    <nav class="nav-links" aria-label="Primary">%s</nav>
    <div class="nav-actions">
      <a class="btn btn-primary btn-sm" href="contact.html">Let&rsquo;s Talk %s</a>
      <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="mobile-nav" aria-label="Open menu"><span></span></button>
    </div>
  </div>
  <div class="mobile-nav" id="mobile-nav">
    <nav aria-label="Mobile">%s</nav>
    <a class="btn btn-primary btn-block" href="contact.html">Let&rsquo;s Talk</a>
  </div>
</header>
""" % (links, icon("arrow-right"), mob)


def footer():
    quick = "".join('<a href="%s">%s</a>' % (h, l) for h, l in NAV if h != "index.html")
    servs = "".join('<a href="services.html#%s">%s</a>' % (s[0], s[3]) for s in SERVICES)
    return """<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <img src="assets/img/logo-dark-720.png" alt="Kirosys Technology" width="186" height="47" loading="lazy">
        <p>Engineering better possibilities through technology, innovation and people.</p>
        <!-- Social profiles: add the real URLs, then delete these comment markers.
        <div class="socials">
          <a href="" aria-label="Kirosys on LinkedIn">%s</a>
          <a href="" aria-label="Kirosys on GitHub">%s</a>
          <a href="" aria-label="Kirosys on YouTube">%s</a>
        </div>
        -->
      </div>
      <div>
        <h4>Quick Links</h4>
        <nav class="footer-links" aria-label="Footer">%s</nav>
      </div>
      <div>
        <h4>Our Services</h4>
        <nav class="footer-links" aria-label="Services">%s</nav>
      </div>
      <div>
        <h4>Contact Us</h4>
        <ul class="footer-contact">
          <li>%s<span>%s</span></li>
          <li>%s<a href="mailto:%s">%s</a></li>
          <li>%s<a href="tel:%s">%s</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span data-year>2026</span> Kirosys Technology. All rights reserved.</span>
      <nav aria-label="Legal">
        <a href="privacy.html">Privacy Policy</a>
        <a href="terms.html">Terms &amp; Conditions</a>
      </nav>
    </div>
  </div>
</footer>
""" % (icon("linkedin"), icon("github"), icon("youtube"), quick, servs,
       icon("pin"), ADDRESS, icon("mail"), EMAIL, EMAIL, icon("phone"), PHONE_HREF, PHONE_DISPLAY)


def clean_urls(markup):
    """GitHub Pages serves /about from about.html, so links drop the extension.
    Files keep their .html names; only the hrefs change."""
    def swap(m):
        path, frag = m.group(1), m.group(2) or ""
        if path == "index.html":
            return 'href="/%s"' % frag
        return 'href="%s%s"' % (path[:-5], frag)
    return re.sub(r'href="([A-Za-z0-9._/-]+\.html)(#[A-Za-z0-9_-]+)?"', swap, markup)


def page(slug, title, desc, body, extrahead=""):
    html = (DOC.replace("__TITLE__", title)
               .replace("__DESC__", desc)
               .replace("__SLUG__", "" if slug == "index.html" else slug[:-5])
               .replace("__EXTRAHEAD__", extrahead)
               .replace("__TOPBAR__", topbar())
               .replace("__HEADER__", header(slug))
               .replace("__FOOTER__", footer())
               .replace("__BODY__", body))
    html = clean_urls(html)
    html = html.replace("https://kirosys.in/thanks.html", "https://kirosys.in/thanks")
    with open("/Volumes/MyDrive/Apps/kirosys-web/" + slug, "w") as f:
        f.write(html)
    return slug


def page_hero(crumb, eyebrow, h1, lead, actions=""):
    return """<section class="page-hero on-dark">
  <div class="container reveal">
    <div class="breadcrumb"><a href="index.html">Home</a> <span>/</span> <span>%s</span></div>
    <p class="eyebrow">%s</p>
    <h1>%s</h1>
    <p class="lead">%s</p>
    %s
  </div>
</section>
""" % (crumb, eyebrow, h1, lead, actions)


def cta_band(h2="Ready to Build a Smarter Tomorrow?",
             p="Partner with Kirosys Technology and turn your ideas into real-world solutions.",
             primary=("contact.html", "Get in Touch"), secondary=("contact.html#quote", "Request a Quote")):
    return """<section class="cta-band on-dark">
  <div class="container cta-inner reveal">
    <div>
      <p class="eyebrow">Let&rsquo;s create what&rsquo;s next</p>
      <h2>%s</h2>
      <p>%s</p>
    </div>
    <div class="cta-actions">
      <a class="btn btn-primary" href="%s">%s %s</a>
      <a class="btn btn-outline" href="%s">%s</a>
    </div>
  </div>
</section>
""" % (h2, p, primary[0], primary[1], icon("arrow-right"), secondary[0], secondary[1])


def service_cards(limit=None, link_prefix="services.html#"):
    out = []
    for n, (slug, ic, tone, name, blurb, _bul) in enumerate(SERVICES[:limit] if limit else SERVICES):
        out.append("""<a class="card reveal" data-delay="%d" href="%s%s">
  <span class="card-ico %s">%s</span>
  <h3>%s</h3>
  <p>%s</p>
  <span class="card-go">Learn more %s</span>
</a>""" % (min(n, 5), link_prefix, slug, tone, icon(ic), name, blurb, icon("arrow-right")))
    return "\n".join(out)


def industry_tiles(link_prefix="industries.html#"):
    out = []
    for n, (slug, ic, name, t1, t2, _b, _l) in enumerate(INDUSTRIES):
        out.append("""<a class="tile reveal" data-delay="%d" style="--t1:%s;--t2:%s" href="%s%s">
  <span class="tile-ico">%s</span>
  <span class="tile-name">%s %s</span>
</a>""" % (min(n, 5), t1, t2, link_prefix, slug, icon(ic), name, icon("arrow-right")))
    return "\n".join(out)


def process_block():
    steps = "".join("""<article class="step reveal" data-delay="%d">
  <span class="step-num">%s</span>
  %s
  <h3>%s</h3>
  <p>%s</p>
</article>""" % (n, num, icon(ic, "step-ico"), name, desc)
        for n, (num, ic, name, desc) in enumerate(PROCESS))
    return """<div class="process">
  <div class="process-intro reveal">
    <p class="eyebrow">Our process</p>
    <h2>A Clear Path from Vision to Value</h2>
    <p>We follow a structured, collaborative approach so delivery stays predictable &mdash; every time.</p>
    <a class="btn btn-primary" href="contact.html">Let&rsquo;s Work Together %s</a>
  </div>
  <div class="steps">%s</div>
</div>""" % (icon("arrow-right"), steps)


def work_cards(items):
    out = []
    for n, (slug, tag, name, sub, blurb, visual, link, label) in enumerate(items):
        href = link if link else "work.html#" + slug
        ext = ' target="_blank" rel="noopener"' if href.startswith("http") else ""
        out.append("""<a class="work-card reveal" data-delay="%d" href="%s"%s>
  <div class="work-visual"><span class="work-tag">%s</span>%s</div>
  <div class="work-meta">
    <div><h3>%s</h3><span>%s</span></div>
    <span class="go">%s</span>
  </div>
</a>""" % (min(n, 5), href, ext, tag, (mini_ui("abc"[n % 3]) if visual == "ui" else MINI_PHONE),
           name, sub, icon("arrow-right")))
    return "\n".join(out)


def testimonials_block():
    slides = "".join("""<figure class="t-slide%s" aria-hidden="%s">
  <span class="quote-mark" aria-hidden="true">&ldquo;</span>
  <div>
    <blockquote>%s</blockquote>
    <cite><b>%s</b><span>%s</span></cite>
  </div>
</figure>""" % (" is-active" if n == 0 else "", "false" if n == 0 else "true", q, who, role)
        for n, (q, who, role) in enumerate(TESTIMONIALS))
    dots = "".join('<button class="t-dot%s" type="button" role="tab" aria-selected="%s" aria-label="Testimonial %d"></button>'
                   % (" is-active" if n == 0 else "", "true" if n == 0 else "false", n + 1)
                   for n in range(len(TESTIMONIALS)))
    return """<div class="testimonials" data-carousel>
  <div class="reveal">
    <p class="eyebrow">Testimonials</p>
    <h2>What Our Clients Say</h2>
    <p class="lead">Feedback from client teams and users across product, cloud and game engagements.</p>
    <div class="t-controls">
      <button class="t-btn" type="button" data-prev aria-label="Previous testimonial">%s</button>
      <button class="t-btn" type="button" data-next aria-label="Next testimonial">%s</button>
    </div>
  </div>
  <div class="reveal">
    <div class="t-viewport">%s</div>
    <div class="t-dots" role="tablist" aria-label="Choose testimonial">%s</div>
  </div>
</div>""" % (icon("chevron-left"), icon("chevron-right"), slides, dots)
