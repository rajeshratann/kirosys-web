# -*- coding: utf-8 -*-
from layout import *

# ───────────────────────── ABOUT ─────────────────────────
VALUES = [
    ("users", "", "Client Centric Approach",
     "We start from your goals and constraints, not from a template. Scope, trade-offs and progress stay visible throughout."),
    ("zap", "violet", "Agile &amp; Flexible",
     "Short delivery cycles, working software early, and room to change direction as what you learn changes the plan."),
    ("bulb", "cyan", "Innovation Driven",
     "We invest in modern tooling and research so the systems we hand over are ready for what comes next, not just for launch."),
    ("buoy", "green", "Reliable Support",
     "Delivery is the beginning. Monitoring, maintenance and improvement keep the product healthy long after go-live."),
    ("shield", "rose", "Security &amp; Quality First",
     "Access control, data handling and testing are designed in from the first sprint rather than retrofitted before launch."),
    ("trend", "amber", "Long-Term Value",
     "We optimise for maintainability and total cost of ownership so your team can own and extend the system confidently."),
]

FACTS = [
    ("Legal name", "Kirosys Technologies Private Limited"),
    ("Entity type", "Private company limited by shares"),
    ("Incorporated", "13 July 2023, under the Companies Act, 2013"),
    ("Registered office", "Patna, Bihar, India"),
    ("Share capital", "&#8377;10,00,000 &mdash; 1,00,000 equity shares of &#8377;10 each"),
    ("Constitution", "Memorandum of Association (Table A) and Articles of Association (Table F)"),
    ("Principal objects", "Publishing of operating systems and system software; development and "
                          "distribution of applications, mobile and web software; IT-enabled services"),
]

DIRECTORS = ["Rajesh Kumar", "Amarjeet Kumar", "Rakesh Kumar"]

about_body = page_hero(
    "About", "About Kirosys",
    "A technology partner built for the long term.",
    "Kirosys Technologies Private Limited is a software development and IT services company "
    "incorporated in Bihar in 2023. We build secure, scalable and future-ready digital solutions "
    "for businesses, institutions and government teams.",
    '<div class="hero-actions"><a class="btn btn-primary" href="contact.html">Work With Us %s</a>'
    '<a class="btn btn-outline" href="work.html">See Our Work</a></div>' % icon("arrow-right"))

about_body += """<section class="section">
  <div class="container split split--wide-left">
    <div class="reveal">
      <p class="eyebrow">Our story</p>
      <h2>Technology that earns its place in the business</h2>
      <p class="lead">Kirosys was formed around a simple belief: software should reduce friction, not add
        to it. That means asking what the work actually looks like before writing code, choosing
        architecture that a small team can maintain, and staying accountable after launch.</p>
      <p class="lead">Our charter is deliberately broad &mdash; system software and applications, mobile
        and web products, cloud platforms, data and AI, electronics and IT-enabled services &mdash; because
        most real problems do not stop neatly at one discipline. What stays constant is how we work:
        senior people close to the problem, short feedback loops, and honest reporting.</p>
      <div class="feature-row">%s</div>
    </div>
    <div class="showcase reveal" data-delay="2">
      <div class="showcase-panel">
        <img class="mark" src="assets/img/mark-256.png" alt="" width="56" height="56" loading="lazy">
        <h3>What we do, end to end</h3>
        <p>Engage us for one focused capability or for the whole delivery.</p>
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

<section class="section section--tint">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">What we value</p>
      <h2>How we work with clients</h2>
      <p class="lead">Six commitments that shape every engagement, from a two-week discovery to a
        multi-year support relationship.</p>
    </div>
    <div class="grid grid-3">%s</div>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div class="reveal">
      <p class="eyebrow">Company information</p>
      <h2>Registered and accountable</h2>
      <p class="lead">Kirosys Technologies Private Limited is a company limited by shares, constituted
        under the Companies Act, 2013. The details below are drawn from our incorporation documents.</p>
      <!-- TODO: add CIN, GSTIN and Udyam registration number here when you want them published. -->
      <table class="fact-table">
        <caption class="form-note" style="caption-side:bottom;text-align:left;padding-top:.75rem">
          Statutory particulars as filed at incorporation.
        </caption>
        <tbody>%s</tbody>
      </table>
    </div>
    <div class="reveal" data-delay="2">
      <p class="eyebrow">Leadership</p>
      <h2>Directors</h2>
      <p class="lead">Kirosys was founded by three directors who remain involved in delivery and
        client relationships day to day.</p>
      <div class="grid grid-2" style="margin-top:1.5rem">%s</div>
      <div class="callout" style="margin-top:1.5rem">%s
        <p>Looking for company documents, a vendor form or a compliance detail for onboarding?
          Email <a href="mailto:%s">%s</a> and we will send it across.</p>
      </div>
    </div>
  </div>
</section>
""" % (
    "".join('<span class="feature-mini">%s<span>%s</span></span>' % (icon(i), t) for i, t in
            [("users", "Client Centric"), ("zap", "Agile &amp; Flexible"),
             ("bulb", "Innovation Driven"), ("buoy", "Reliable Support")]),
    "".join('<li>%s<span>%s</span></li>' % (icon("check"), t) for t in
            ["Software &amp; Web Solutions", "Mobile Applications", "Cloud &amp; DevOps",
             "AI &amp; Data Solutions", "IT Consulting &amp; Support", "Government &amp; Enterprise Solutions"]),
    "".join("""<article class="card reveal" data-delay="%d"><span class="card-ico %s">%s</span>
  <h3>%s</h3><p>%s</p></article>""" % (min(n, 5), tone, icon(ic), name, desc)
        for n, (ic, tone, name, desc) in enumerate(VALUES)),
    "".join("<tr><th scope=\"row\">%s</th><td>%s</td></tr>" % (k, v) for k, v in FACTS),
    "".join("""<article class="card"><span class="card-ico">%s</span><h3>%s</h3>
  <p>Director</p></article>""" % (icon("users"), d) for d in DIRECTORS),
    icon("info"), EMAIL, EMAIL,
)

about_body += """<section class="section section--tint">
  <div class="container">%s</div>
</section>
""" % testimonials_block()
about_body += cta_band("Let&rsquo;s talk about what you are building",
                       "Tell us the problem, the timeline and the constraints. We will come back with a practical path.")

page("about.html", "About Kirosys Technologies &mdash; Company, Values &amp; Leadership",
     "Kirosys Technologies Private Limited is a software and IT services company incorporated in Bihar in 2023, "
     "building secure and scalable digital solutions for business, institutional and government clients.",
     about_body, extrahead=JSONLD)
print("about.html")

# ───────────────────────── SERVICES ─────────────────────────
def detail_block(slug, ic, tone, name, blurb, bullets, extra=""):
    return """<article class="detail" id="%s">
  <div class="detail-head reveal">
    <span class="card-ico %s">%s</span>
    <h2>%s</h2>
    <p>%s</p>
    %s
  </div>
  <ul class="detail-list reveal" data-delay="1">%s</ul>
</article>""" % (slug, tone, icon(ic), name, blurb, extra,
                 "".join('<li>%s<span>%s</span></li>' % (icon("check"), b) for b in bullets))

services_body = page_hero(
    "Services", "Our Services",
    "End-to-end technology solutions.",
    "From idea to execution, we design, build, integrate and support the systems your organisation "
    "runs on &mdash; software, mobile, cloud, data and the people to keep it all healthy.",
    '<div class="hero-actions"><a class="btn btn-primary" href="contact.html">Request a Quote %s</a>'
    '<a class="btn btn-outline" href="work.html">See Our Work</a></div>' % icon("arrow-right"))

services_body += """<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">Core capabilities</p>
      <h2>Six services, one accountable team</h2>
      <p class="lead">Engage a single capability or bring us in as your full delivery partner.</p>
    </div>
    %s
  </div>
</section>

<section class="section section--tint">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">Also from Kirosys</p>
      <h2>Additional capabilities</h2>
      <p class="lead">Our charter extends beyond conventional software delivery.</p>
    </div>
    <div class="grid grid-3">%s</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">Engagement models</p>
      <h2>Work with us the way that fits</h2>
    </div>
    <div class="grid grid-3">%s</div>
  </div>
</section>

<section class="section section--tint">
  <div class="container">%s</div>
</section>
""" % (
    "\n".join(detail_block(*s) for s in SERVICES),
    "".join("""<article class="card reveal" data-delay="%d" id="%s"><span class="card-ico %s">%s</span>
  <h3>%s</h3><p>%s</p><ul class="card-list">%s</ul></article>""" %
        (n, slug, tone, icon(ic), name, blurb, "".join("<li>%s</li>" % b for b in bullets))
        for n, (slug, ic, tone, name, blurb, bullets) in enumerate(EXTRA_SERVICES)),
    "".join("""<article class="card reveal" data-delay="%d"><span class="card-ico %s">%s</span>
  <h3>%s</h3><p>%s</p></article>""" % (n, tone, icon(ic), name, desc) for n, (ic, tone, name, desc) in enumerate([
        ("layers", "", "Project delivery",
         "A defined scope, a fixed team and an agreed milestone plan &mdash; best when the outcome is clear and the timeline matters."),
        ("users", "violet", "Dedicated team",
         "Engineers, designers, QA and DevOps embedded into your delivery rhythm, reporting the way your own team does."),
        ("buoy", "cyan", "Managed support",
         "Ongoing maintenance, monitoring, enhancements and an agreed response commitment for systems already in production."),
    ])),
    process_block(),
)
services_body += cta_band()

page("services.html", "Services &mdash; Software, Mobile, Cloud, AI &amp; IT Consulting | Kirosys",
     "Custom software development, mobile apps, cloud and DevOps, AI and data solutions, IT consulting "
     "and web portal development from Kirosys Technologies Private Limited.",
     services_body)
print("services.html")

# ───────────────────────── INDUSTRIES ─────────────────────────
industries_body = page_hero(
    "Industries", "Industries We Serve",
    "Powering progress across industries.",
    "Sector context changes everything &mdash; the data you can hold, the people who use the system and "
    "the rules you answer to. Here is how that shapes what we build.")

industries_body += """<section class="section">
  <div class="container">
    %s
  </div>
</section>

<section class="section section--tint">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">Not on the list?</p>
      <h2>We start by learning your domain</h2>
      <p class="lead">Most of our work begins with a discovery phase where we map your process, users and
        constraints before proposing a build. If your sector is not shown here, that process is the same.</p>
    </div>
    <div class="grid grid-4">%s</div>
  </div>
</section>
""" % (
    "\n".join(detail_block(slug, ic, ["", "violet", "cyan", "amber", "rose", "green"][n % 6], name, blurb, bullets,
                           '<a class="link-more" href="contact.html">Discuss a %s project %s</a>'
                           % (name.lower(), icon("arrow-right")))
            for n, (slug, ic, name, _t1, _t2, blurb, bullets) in enumerate(INDUSTRIES)),
    "".join("""<article class="card reveal" data-delay="%d"><span class="card-ico %s">%s</span>
  <h3>%s</h3><p>%s</p></article>""" % (n, tone, icon(ic), name, desc) for n, (ic, tone, name, desc) in enumerate([
        ("search", "", "Domain discovery", "Interviews, process mapping and a written summary of what the system must do."),
        ("shield", "violet", "Risk and compliance", "Data handling, access control and audit requirements identified early."),
        ("layers", "cyan", "Integration review", "Where the new system meets the tools and records you already keep."),
        ("rocket", "amber", "Delivery plan", "Milestones, costs and a first release you can put in front of real users."),
    ]))
)
industries_body += cta_band()

page("industries.html", "Industries &mdash; Healthcare, FinTech, Education, Government | Kirosys",
     "Kirosys Technologies builds software for healthcare, fintech, education, e-commerce, government "
     "and logistics teams &mdash; with sector context shaping every design decision.",
     industries_body)
print("industries.html")
