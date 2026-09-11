# -*- coding: utf-8 -*-
from layout import *

TODAY = "11 September 2026"

# ───────────────────────── OUR WORK ─────────────────────────
work_body = page_hero(
    "Our Work", "Featured Work",
    "Real solutions. Real impact.",
    "Products we have designed, built and shipped &mdash; and continue to support. Each one started "
    "as a conversation about a problem worth solving.")

work_cards_full = []
for n, (slug, tag, name, sub, blurb, visual, link, label) in enumerate(WORK):
    ext = ' target="_blank" rel="noopener"' if link.startswith("http") else ""
    action = ('<a class="link-more" href="%s"%s>%s %s</a>' % (link, ext, label, icon("external" if link.startswith("http") else "arrow-right"))
              if link else '<a class="link-more" href="contact.html">Ask about %s %s</a>' % (name, icon("arrow-right")))
    work_cards_full.append("""<article class="card reveal" data-delay="%d" id="%s">
  <div class="work-visual" style="border-radius:10px;margin:-.25rem 0 .9rem;aspect-ratio:16/9">
    <span class="work-tag">%s</span>%s
  </div>
  <h3>%s</h3>
  <p style="color:var(--ink-300);font-size:.8125rem;font-weight:600;margin-top:-.35rem">%s</p>
  <p>%s</p>
  %s
</article>""" % (min(n, 5), slug, tag, mini_ui("abc"[n % 3]) if visual == "ui" else MINI_PHONE,
                 name, sub, blurb, action))

work_body += """<section class="section">
  <div class="container">
    <div class="grid grid-3">%s</div>
  </div>
</section>

<section class="section section--tint">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">How we deliver</p>
      <h2>What a Kirosys engagement looks like</h2>
      <p class="lead">Whether it is a product of our own or a client platform, the shape of the work is the same.</p>
    </div>
    %s
  </div>
</section>

<section class="section">
  <div class="container">%s</div>
</section>
""" % ("\n".join(work_cards_full), process_block(), testimonials_block())
work_body += cta_band("Have something you want built?",
                      "Bring us the brief, the backlog or the broken system. We will help you find the shortest useful path.")

page("work.html", "Our Work &mdash; Products &amp; Platforms by Kirosys Technologies",
     "JiVault, JiQuest, Kitty Gaming, Battle Brain and custom client platforms &mdash; products designed, "
     "built and supported by Kirosys Technologies Private Limited.",
     work_body)
print("work.html")

# ───────────────────────── CAREERS ─────────────────────────
ROLES = [
    ("Full Stack Engineer", "Engineering", ["React", "Node.js", "APIs", "Databases", "Testing"],
     "Product-minded implementation across the stack, from API design to deployment."),
    ("Mobile Developer", "Mobile", ["Android", "iOS", "Flutter", "React Native"],
     "Native or cross-platform apps with performance, polish and production discipline."),
    ("AI / ML Engineer", "AI &amp; Data", ["Python", "LLM workflows", "RAG", "Evaluation", "Pipelines"],
     "Practical AI features with evaluation and guardrails, not demos."),
    ("DevOps / Cloud Engineer", "Cloud", ["Kubernetes", "Terraform", "CI/CD", "Monitoring", "Security"],
     "Reliable delivery pipelines and infrastructure that teams can own."),
    ("Game Developer", "Games", ["Unity", "Gameplay systems", "Multiplayer", "Tooling"],
     "Gameplay engineering, live content and platform publishing."),
    ("Product Designer", "Design", ["UX systems", "Interface design", "Prototyping", "Research"],
     "Interface and system design with developer-friendly specifications."),
]

careers_body = page_hero(
    "Careers", "Careers at Kirosys",
    "Build serious systems with people who care about craft.",
    "We look for thoughtful engineers, designers and operators who enjoy solving real problems with "
    "clarity and ownership &mdash; and who want their work used, not shelved.",
    '<div class="hero-actions"><a class="btn btn-primary" href="mailto:%s?subject=Application%%20%%E2%%80%%94%%20Kirosys">Send Your Profile %s</a>'
    '<a class="btn btn-outline" href="about.html">About Kirosys</a></div>' % (EMAIL, icon("arrow-right")))

careers_body += """<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">Why Kirosys</p>
      <h2>Small teams, real ownership</h2>
      <p class="lead">You will see your work reach production, and you will still be around to improve it.</p>
    </div>
    <div class="grid grid-4">%s</div>
  </div>
</section>

<section class="section section--tint">
  <div class="container">
    <div class="section-head reveal">
      <p class="eyebrow">Open tracks</p>
      <h2>Roles we hire for</h2>
      <p class="lead">Even when a specific role is not open, a strong portfolio is always worth sending.</p>
    </div>
    <div class="grid" style="gap:.9rem">%s</div>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div class="reveal">
      <p class="eyebrow">How to apply</p>
      <h2>Send your profile, portfolio or GitHub</h2>
      <p class="lead">Email <a href="mailto:%s">%s</a> with the track you are interested in, links to
        your work, and a short note about the kind of problems you enjoy solving. We read everything and
        reply to everyone we can take further.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="mailto:%s?subject=Application%%20%%E2%%80%%94%%20Kirosys">Email Your Application %s</a>
      </div>
    </div>
    <div class="callout reveal" data-delay="2">%s
      <p><strong>Applying from outside Patna?</strong> Several of our tracks are open to remote and
        hybrid arrangements. Mention your preferred setup in your first email so we can be upfront
        about what is possible for that role.</p>
    </div>
  </div>
</section>
""" % (
    "".join("""<article class="card reveal" data-delay="%d"><span class="card-ico %s">%s</span>
  <h3>%s</h3><p>%s</p></article>""" % (n, tone, icon(ic), name, desc) for n, (ic, tone, name, desc) in enumerate([
        ("layers", "", "Work that ships", "Products with real users, not slideware or indefinite pilots."),
        ("users", "violet", "Direct access", "Small teams, short decision chains and no layers to route around."),
        ("bulb", "cyan", "Room to learn", "New stacks, new domains and time set aside to go deep on both."),
        ("buoy", "green", "Support that lasts", "Onboarding, review and mentoring that continues past week one."),
    ])),
    "".join("""<article class="job reveal">
  <div>
    <h3>%s</h3>
    <p style="font-size:.875rem;margin-top:.25rem">%s</p>
    <div class="job-tags"><span>%s</span>%s</div>
  </div>
  <a class="btn btn-outline btn-sm" href="mailto:%s?subject=%s%%20%%E2%%80%%94%%20Kirosys%%20application">Apply %s</a>
</article>""" % (title, desc, track, "".join("<span>%s</span>" % t for t in tags), EMAIL,
                 title.replace(" ", "%20").replace("&amp;", "and"), icon("arrow-right"))
        for title, track, tags, desc in ROLES),
    EMAIL, EMAIL, EMAIL, icon("arrow-right"), icon("info"),
)
careers_body += cta_band("Not looking, but curious?",
                         "Introduce yourself anyway. We keep good profiles on file and come back to them when a track opens.",
                         ("mailto:%s" % EMAIL, "Email Us"), ("about.html", "Learn About Kirosys"))

page("careers.html", "Careers &mdash; Engineering, Design &amp; Cloud Roles | Kirosys Technologies",
     "Open engineering, mobile, AI, cloud, game development and design tracks at Kirosys Technologies "
     "Private Limited, Patna.", careers_body)
print("careers.html")

# ───────────────────────── BLOG ─────────────────────────
TOPICS = [
    ("Engineering", "Choosing an architecture a small team can actually maintain",
     "Why the most scalable choice is often the one your team can debug at 2am."),
    ("Cloud", "A practical cloud cost review, step by step",
     "The checks we run before recommending a migration, a rebuild or simply a better-sized instance."),
    ("AI &amp; Data", "Putting an LLM feature into production responsibly",
     "Evaluation, guardrails and the human review loop that keeps a useful feature from becoming a liability."),
    ("Delivery", "What a good discovery phase produces",
     "The artefacts we hand over before a line of production code is written."),
]

blog_body = page_hero(
    "Blog", "Insights",
    "Notes from the build.",
    "Practical write-ups on architecture, cloud, delivery and applied AI &mdash; drawn from the systems "
    "we are building right now. The first articles are being written; here is what is coming.")

blog_body += """<section class="section">
  <div class="container">
    <div class="callout reveal" style="margin-bottom:2.5rem">%s
      <p><strong>Our first articles are on the way.</strong> Want to be told when they are published,
        or have a topic you would like covered? Email <a href="mailto:%s">%s</a> and we will add you
        to the list.</p>
    </div>
    <div class="grid grid-2">%s</div>
  </div>
</section>
""" % (icon("info"), EMAIL, EMAIL,
       "".join("""<article class="post reveal" data-delay="%d">
  <div class="post-meta"><span class="tag">%s</span><span>Coming soon</span></div>
  <h3>%s</h3>
  <p>%s</p>
</article>""" % (min(n, 5), cat, title, blurb) for n, (cat, title, blurb) in enumerate(TOPICS)))
blog_body += cta_band("Would rather just talk it through?",
                      "Our team is happy to share how we would approach your problem &mdash; no article required.")

page("blog.html", "Insights &amp; Engineering Notes | Kirosys Technologies",
     "Practical write-ups on software architecture, cloud, delivery and applied AI from the Kirosys "
     "Technologies engineering team.", blog_body)
print("blog.html")
