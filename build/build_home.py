# -*- coding: utf-8 -*-
from layout import *

HERO_POINTS = [("bulb", "Innovative Solutions"), ("users", "Trusted Partnership"),
               ("shield", "Quality Delivery"), ("trend", "Long-term Value")]
STATS = [("briefcase", "50", "+", "Projects Delivered"), ("users", "30", "+", "Happy Clients"),
         ("chart", "5", "+", "Industries Served"), ("award", "100", "%", "Commitment to Quality")]
ABOUT_MINI = [("users", "Client Centric Approach"), ("zap", "Agile &amp; Flexible"),
              ("bulb", "Innovation Driven"), ("buoy", "Reliable Support")]
SHOWCASE = [("code", "Software &amp; Web Solutions"), ("phone-app", "Mobile Applications"),
            ("cloud", "Cloud &amp; DevOps"), ("headset", "IT Consulting &amp; Support"),
            ("landmark", "Government &amp; Enterprise Solutions")]

hero = """<section class="hero on-dark">
  <div class="container hero-inner">
    <div class="reveal">
      <p class="eyebrow">Engineering Better Possibilities</p>
      <h1>Technology<br>for a Smarter,<br><span class="grad">More Connected Tomorrow</span></h1>
      <p class="hero-lead">We design, develop and deliver digital solutions that help businesses
        innovate, operate efficiently and create lasting impact.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="contact.html">Get in Touch %s</a>
        <a class="btn btn-outline" href="services.html">Explore Our Services</a>
      </div>
      <div class="hero-points">%s</div>
    </div>
    <div class="hero-visual reveal" data-delay="2">
      <p class="hero-words" aria-hidden="true"><span>Ideas</span><span>Technology</span><span>People</span><span>Impact</span></p>
      <div class="hero-console">
        <div class="console-bar"><span class="console-dot"></span><span class="console-dot"></span><span class="console-dot"></span><span class="console-title">kirosys / delivery</span></div>
        <div class="console-body" aria-hidden="true">
          <div class="code-line"><span class="code-num">1</span><span><span class="c-key">service</span> <span class="c-fn">kirosys</span> {</span></div>
          <div class="code-line"><span class="code-num">2</span><span>&nbsp;&nbsp;<span class="c-key">build</span>: <span class="c-str">"web, mobile, cloud"</span>,</span></div>
          <div class="code-line"><span class="code-num">3</span><span>&nbsp;&nbsp;<span class="c-key">secure</span>: <span class="c-val">true</span>,</span></div>
          <div class="code-line"><span class="code-num">4</span><span>&nbsp;&nbsp;<span class="c-key">scale</span>: <span class="c-str">"future-ready"</span>,</span></div>
          <div class="code-line"><span class="code-num">5</span><span>&nbsp;&nbsp;<span class="c-com">// from idea to impact</span></span></div>
          <div class="code-line"><span class="code-num">6</span><span>}</span></div>
        </div>
        <div class="console-foot" aria-hidden="true">
          <span class="chip">Discover</span><span class="chip">Plan</span><span class="chip">Build</span><span class="chip">Deliver</span>
        </div>
      </div>
      <div class="hero-float">
        <span class="bar" aria-hidden="true"></span>
        <strong>Turning Ideas into Real-World Solutions</strong>
        <span>Software &middot; Cloud &middot; AI &middot; Support</span>
      </div>
    </div>
  </div>
</section>
""" % (icon("arrow-right"),
       "".join('<span class="hero-point">%s<span>%s</span></span>' % (icon(i), t) for i, t in HERO_POINTS))

stats = """<section class="section section--tight">
  <div class="container">
    <div class="stats reveal">%s</div>
  </div>
</section>
""" % "".join("""<div class="stat"><span class="stat-ico">%s</span><div>
  <div class="stat-num"><span data-count="%s" data-suffix="%s">%s%s</span></div>
  <div class="stat-label">%s</div></div></div>""" % (icon(i), n, sfx, n, sfx, label)
      for i, n, sfx, label in STATS)

about = """<section class="section">
  <div class="container split split--wide-left">
    <div class="reveal">
      <p class="eyebrow">About Kirosys</p>
      <h2>Building Technology for a Better Tomorrow</h2>
      <p class="lead">Kirosys Technologies is a software development and IT services company focused on
        creating scalable, secure and future-ready digital solutions. We combine domain expertise with
        modern technology to help businesses, organisations and government entities solve real problems
        and unlock new opportunities.</p>
      <div class="feature-row">%s</div>
      <div class="hero-actions"><a class="btn btn-primary" href="about.html">More About Us %s</a></div>
    </div>
    <div class="showcase reveal" data-delay="2">
      <div class="showcase-panel">
        <img class="mark" src="assets/img/mark-256.png" alt="" width="56" height="56" loading="lazy">
        <h3>One partner across the full stack</h3>
        <p>From the first workshop to long-term support, the same team stays with your product.</p>
        <ul class="showcase-list">%s</ul>
      </div>
      <figure class="quote-card">
        <span class="quote-mark" aria-hidden="true">&ldquo;</span>
        <p>We believe in using technology as a force for good &mdash; empowering businesses and people to achieve more.</p>
        <cite>&mdash; Kirosys Technologies</cite>
      </figure>
    </div>
  </div>
</section>
""" % ("".join('<span class="feature-mini">%s<span>%s</span></span>' % (icon(i), t) for i, t in ABOUT_MINI),
       icon("arrow-right"),
       "".join('<li>%s<span>%s</span></li>' % (icon("check"), t) for i, t in SHOWCASE))

services = """<section class="section section--tint">
  <div class="container">
    <div class="section-head section-head--split">
      <div class="reveal">
        <p class="eyebrow">Our Services</p>
        <h2>End-to-End Technology Solutions</h2>
        <p class="lead">From idea to execution, we deliver solutions that create real business value.</p>
      </div>
      <a class="link-more reveal" href="services.html">View All Services %s</a>
    </div>
    <div class="grid grid-6">%s</div>
  </div>
</section>
""" % (icon("arrow-right"), service_cards())

industries = """<section class="section">
  <div class="container">
    <div class="section-head section-head--split">
      <div class="reveal">
        <p class="eyebrow">Industries We Serve</p>
        <h2>Powering Progress Across Industries</h2>
        <p class="lead">Sector context shapes every decision &mdash; from data design to the way people use what we ship.</p>
      </div>
      <a class="link-more reveal" href="industries.html">View All Industries %s</a>
    </div>
    <div class="grid grid-6">%s</div>
  </div>
</section>
""" % (icon("arrow-right"), industry_tiles())

process = """<section class="section section--tint">
  <div class="container">%s</div>
</section>
""" % process_block()

work = """<section class="section">
  <div class="container">
    <div class="section-head section-head--split">
      <div class="reveal">
        <p class="eyebrow">Featured Work</p>
        <h2>Real Solutions. Real Impact.</h2>
        <p class="lead">Products we have designed, built and shipped &mdash; and continue to support.</p>
      </div>
      <a class="link-more reveal" href="work.html">View All Projects %s</a>
    </div>
    <div class="grid grid-4">%s</div>
  </div>
</section>
""" % (icon("arrow-right"), work_cards(WORK[:4]))

testimonials = """<section class="section section--tint">
  <div class="container">%s</div>
</section>
""" % testimonials_block()

page("index.html",
     "Kirosys Technologies &mdash; Software, Cloud &amp; IT Services Company",
     "Kirosys Technologies Private Limited designs, develops and delivers custom software, mobile apps, "
     "cloud, AI and IT consulting solutions for businesses, institutions and government teams.",
     hero + stats + about + services + industries + process + work + testimonials + cta_band(),
     extrahead=JSONLD)
print("index.html")
