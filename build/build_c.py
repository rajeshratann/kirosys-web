# -*- coding: utf-8 -*-
from layout import *

TODAY = "11 September 2026"

# ───────────────────────── CONTACT ─────────────────────────
OPTIONS = ["Custom Software Development", "Mobile App Development", "Cloud &amp; DevOps",
           "AI &amp; Data Solutions", "IT Consulting &amp; Support", "Web &amp; Portal Development",
           "Game Development", "Electronics &amp; Hardware", "Something else"]

contact_body = page_hero(
    "Contact", "Contact Us",
    "Tell us what you want to build.",
    "Share a project brief, a technical problem, a hiring need or a rough idea. We will come back "
    "with the most useful next step &mdash; even if that step is not with us.")

contact_body += """<section class="section">
  <div class="container split split--wide-left">
    <div class="reveal">
      <p class="eyebrow">Reach us</p>
      <h2>Direct communication from day one</h2>
      <p class="lead">You can contact us for discovery and estimates, cloud and architecture reviews,
        product rescue, dedicated engineers or a long-term engineering partnership.</p>
      <ul class="footer-contact" style="margin-top:1.75rem;gap:1.1rem">
        <li style="color:var(--ink-500)">%s<span><strong style="display:block">Registered office</strong>%s</span></li>
        <li style="color:var(--ink-500)">%s<span><strong style="display:block">Email</strong><a href="mailto:%s" style="color:var(--blue-600)">%s</a></span></li>
        <li style="color:var(--ink-500)">%s<span><strong style="display:block">Phone</strong><a href="tel:%s" style="color:var(--blue-600)">%s</a></span></li>
        <li style="color:var(--ink-500)">%s<span><strong style="display:block">Working hours</strong>Monday to Saturday, 10:00 &ndash; 19:00 IST</span></li>
      </ul>
      <div class="callout" style="margin-top:1.75rem">%s
        <p><strong>Hiring enquiry?</strong> Send your profile and portfolio to
          <a href="mailto:%s">%s</a> &mdash; see <a href="careers.html">open tracks</a> first.</p>
      </div>
    </div>

    <form class="form reveal" data-delay="2" id="quote" action="https://formsubmit.co/%s" method="POST">
      <input type="hidden" name="_subject" value="New Kirosys website enquiry">
      <input type="hidden" name="_template" value="table">
      <input type="hidden" name="_captcha" value="false">
      <input type="hidden" name="_next" value="https://kirosys.in/thanks.html">
      <input type="text" name="_honey" tabindex="-1" autocomplete="off" class="form-honey" aria-hidden="true">
      <div class="form-row">
        <div class="field">
          <label for="first_name">First name</label>
          <input id="first_name" type="text" name="first_name" placeholder="Your first name" autocomplete="given-name" required>
        </div>
        <div class="field">
          <label for="last_name">Last name</label>
          <input id="last_name" type="text" name="last_name" placeholder="Your last name" autocomplete="family-name" required>
        </div>
      </div>
      <div class="form-row">
        <div class="field">
          <label for="email">Work email</label>
          <input id="email" type="email" name="email" placeholder="you@company.com" autocomplete="email" required>
        </div>
        <div class="field">
          <label for="phone">Phone <span style="font-weight:400;color:var(--ink-300)">(optional)</span></label>
          <input id="phone" type="tel" name="phone" placeholder="+91" autocomplete="tel">
        </div>
      </div>
      <div class="field">
        <label for="service">What can we help with?</label>
        <select id="service" name="service" required>
          <option value="">Select a service&hellip;</option>
          %s
        </select>
      </div>
      <div class="field">
        <label for="message">Project details</label>
        <textarea id="message" name="message" placeholder="A brief overview, your goals, timeline and any technical context&hellip;" required></textarea>
      </div>
      <button class="btn btn-primary btn-block" type="submit">Send Message %s</button>
      <p class="form-note">We reply to every genuine enquiry, usually within one working day. Your
        details are used only to respond to this message &mdash; see our
        <a href="privacy.html">privacy policy</a>.</p>
    </form>
  </div>
</section>
""" % (icon("pin"), ADDRESS, icon("mail"), EMAIL, EMAIL, icon("phone"), PHONE_HREF, PHONE_DISPLAY,
       icon("clock"), icon("info"), EMAIL, EMAIL, EMAIL,
       "".join("<option>%s</option>" % o for o in OPTIONS), icon("send"))

contact_body += """<section class="section section--tint">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">Before you write</p>
      <h2>Useful things to include</h2>
      <p class="lead">None of this is required &mdash; but the more of it we have, the more concrete our first reply can be.</p>
    </div>
    <div class="grid grid-4">%s</div>
  </div>
</section>
""" % "".join("""<article class="card reveal" data-delay="%d"><span class="card-ico %s">%s</span>
  <h3>%s</h3><p>%s</p></article>""" % (n, tone, icon(ic), name, desc) for n, (ic, tone, name, desc) in enumerate([
    ("search", "", "The problem", "What is not working today, and who feels it."),
    ("clipboard", "violet", "The constraints", "Deadlines, budget range, compliance or existing systems."),
    ("users", "cyan", "The people", "Who will use it, and who will own it after launch."),
    ("rocket", "amber", "The outcome", "What has to be true for this to have been worth doing."),
]))

page("contact.html", "Contact Kirosys Technology &mdash; Start a Project",
     "Contact Kirosys Technology for software development, mobile apps, cloud, AI, "
     "IT consulting and support. Patna, Bihar, India.", contact_body)
print("contact.html")

# ───────────────────────── LEGAL ─────────────────────────
def legal(slug, crumb, eyebrow, h1, lead, sections, title, desc):
    body = page_hero(crumb, eyebrow, h1, lead)
    blocks = "".join("<h2>%s</h2>%s" % (h, "".join("<p>%s</p>" % p if isinstance(p, str) else
                                                   "<ul>%s</ul>" % "".join("<li>%s</li>" % li for li in p)
                                                   for p in ps)) for h, ps in sections)
    body += """<section class="section">
  <div class="container">
    <div class="prose reveal">
      <p class="form-note">Last updated: %s</p>
      %s
      <h2>Contact</h2>
      <p>Questions about this page can be sent to <a href="mailto:%s">%s</a>, or by post to
        Kirosys Technology, New Dariyapur Colony, Suryamandir, Khairatali,
        Patna &ndash; 804453, Bihar, India.</p>
    </div>
  </div>
</section>
""" % (TODAY, blocks, EMAIL, EMAIL)
    page(slug, title, desc, body)
    print(slug)


legal("privacy.html", "Privacy Policy", "Legal", "Privacy Policy",
      "How Kirosys Technology handles information submitted through this website.",
      [
        ("Information we collect",
         ["We collect the information you choose to submit through forms on this website &mdash; typically "
          "your name, email address, phone number, company details, the service you are interested in and "
          "the project information you describe.",
          "We do not use advertising trackers or third-party analytics profiling on this site."]),
        ("How we use information",
         ["Submitted information is used to respond to your enquiry, prepare project discussions, deliver "
          "services you engage us for, improve how we communicate on this website, and maintain ordinary "
          "business records."]),
        ("Form processing",
         ["Enquiry forms on this website are delivered to us by a third-party form-handling service, which "
          "processes the submission solely to pass it on to our team. Your message reaches "
          "<a href=\"mailto:support@kirosys.in\">support@kirosys.in</a>."]),
        ("Data sharing",
         ["We do not sell personal information. We share information with service providers or partners only "
          "where it is needed to operate this website, respond to your request or deliver contracted services, "
          "and where the law requires it."]),
        ("Retention and security",
         ["We keep enquiry records for as long as they remain relevant to an ongoing or prospective engagement, "
          "or as long as the law requires. We apply reasonable administrative and technical safeguards, though "
          "no method of transmission or storage can be guaranteed completely secure."]),
        ("Your choices",
         ["You may request access to, correction of, or deletion of the information you have submitted by "
          "contacting us. We will respond within a reasonable period."]),
      ],
      "Privacy Policy | Kirosys Technology",
      "How Kirosys Technology collects, uses, shares and protects information submitted through this website.")

legal("terms.html", "Terms &amp; Conditions", "Legal", "Terms &amp; Conditions",
      "These terms govern use of the Kirosys Technology website. Project work is governed by separate written agreements.",
      [
        ("Website use",
         ["You may use this website to learn about Kirosys Technology and to contact us. "
          "You agree not to misuse the website, attempt unauthorised access, or interfere with its normal operation."]),
        ("No engagement by itself",
         ["The content of this website is informational. Submitting a form does not create a client engagement, "
          "guarantee acceptance of a project, or form a service agreement. We may decline enquiries at our discretion. "
          "Any engagement is governed by a separate written agreement signed by both parties."]),
        ("Content and intellectual property",
         ["Website text, visuals, branding, product names and layouts are owned by Kirosys Technology Private "
          "Limited or used with permission. You may not copy, republish or reuse them without written approval."]),
        ("Third-party services",
         ["This website references external platforms, app stores and technologies. We are not responsible for "
          "third-party sites, tools or their policies."]),
        ("Limitation of liability",
         ["This website is provided on an &ldquo;as is&rdquo; basis. To the maximum extent permitted by law, "
          "Kirosys Technology is not liable for any damages arising from use of this website."]),
        ("Governing law",
         ["These terms are governed by the laws of India, and the courts at Patna, Bihar have jurisdiction over "
          "any dispute arising from use of this website."]),
      ],
      "Terms &amp; Conditions | Kirosys Technology",
      "Terms governing the use of the Kirosys Technology website.")

# ───────────────────────── THANKS / 404 ─────────────────────────
thanks_body = page_hero(
    "Thank You", "Message sent",
    "Thank you for reaching out.",
    "Your message has reached the Kirosys team. We read every enquiry and usually reply within one "
    "working day &mdash; sooner if it looks time-sensitive.",
    '<div class="hero-actions"><a class="btn btn-primary" href="index.html">Back to Home %s</a>'
    '<a class="btn btn-outline" href="work.html">See Our Work</a></div>' % icon("arrow-right"))
thanks_body += """<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">While you wait</p>
      <h2>A few things worth a look</h2>
    </div>
    <div class="grid grid-3">%s</div>
  </div>
</section>
""" % "".join("""<a class="card reveal" data-delay="%d" href="%s"><span class="card-ico %s">%s</span>
  <h3>%s</h3><p>%s</p><span class="card-go">Open %s</span></a>""" %
    (n, href, tone, icon(ic), name, desc, icon("arrow-right"))
    for n, (ic, tone, name, desc, href) in enumerate([
        ("layers", "", "Our services", "The full range of what we design, build and support.", "services.html"),
        ("briefcase", "violet", "Our work", "Products we have shipped and continue to run.", "work.html"),
        ("users", "cyan", "About Kirosys", "Who we are, how we work and our company details.", "about.html"),
    ]))
page("thanks.html", "Thank You | Kirosys Technology",
     "Your message has been sent to the Kirosys Technology team.", thanks_body)
print("thanks.html")

nf_body = page_hero(
    "404", "Error 404",
    "This page is off the grid.",
    "The page may have moved, or the link may be incorrect. Head back home, or tell us what you were "
    "looking for and we will point you to it.",
    '<div class="hero-actions"><a class="btn btn-primary" href="index.html">Back Home %s</a>'
    '<a class="btn btn-outline" href="contact.html">Contact Kirosys</a></div>' % icon("arrow-right"))
nf_body += """<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">Popular pages</p>
      <h2>Try one of these instead</h2>
    </div>
    <div class="grid grid-4">%s</div>
  </div>
</section>
""" % "".join("""<a class="card reveal" data-delay="%d" href="%s"><span class="card-ico %s">%s</span>
  <h3>%s</h3><p>%s</p></a>""" % (n, href, tone, icon(ic), name, desc)
    for n, (ic, tone, name, desc, href) in enumerate([
        ("layers", "", "Services", "Software, mobile, cloud, AI and support.", "services.html"),
        ("chart", "violet", "Industries", "Sectors we build for.", "industries.html"),
        ("briefcase", "cyan", "Our work", "Products we have shipped.", "work.html"),
        ("send", "amber", "Contact", "Start a conversation.", "contact.html"),
    ]))
page("404.html", "Page Not Found | Kirosys Technology",
     "The page you were looking for could not be found on the Kirosys Technology website.", nf_body)
print("404.html")

# ───────────────────────── REDIRECT STUBS ─────────────────────────
REDIRECT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s | Kirosys Technology</title>
<link rel="canonical" href="https://kirosys.in/%s">
<meta name="robots" content="noindex">
<meta http-equiv="refresh" content="0; url=%s">
<link rel="icon" href="assets/img/icon-32.png" sizes="32x32" type="image/png">
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
<section class="page-hero on-dark">
  <div class="container">
    <p class="eyebrow">Page moved</p>
    <h1>%s</h1>
    <p class="lead">This page now lives at <a href="%s" style="color:#fff;border-bottom:1px solid rgba(255,255,255,.5)">%s</a>.
      You should be redirected automatically.</p>
    <div class="hero-actions"><a class="btn btn-primary" href="%s">Continue</a>
    <a class="btn btn-outline" href="/">Back to Home</a></div>
  </div>
</section>
<script>location.replace("%s");</script>
</body>
</html>
"""
for src, dest, label, heading in [
    ("products.html", "work", "Products", "Our products are now under Our Work"),
    ("cloud.html", "services#cloud-devops", "Cloud Services", "Cloud services are now part of our Services page"),
]:
    with open("/Volumes/MyDrive/Apps/kirosys-web/" + src, "w") as f:
        f.write(REDIRECT % (label, dest, dest, heading, dest, dest, dest, dest))
    print(src, "->", dest)
