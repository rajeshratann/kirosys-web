# -*- coding: utf-8 -*-
"""Shared markup for the Kirosys static site."""

SITE = "https://kirosys.in"
EMAIL = "support@kirosys.in"
PHONE_DISPLAY = "+91 82988 66066"
PHONE_HREF = "+918298866066"
ADDRESS = "New Dariyapur Colony, Suryamandir, Khairatali,<br>Patna &ndash; 804453, Bihar, India"

I = {  # 24x24 lucide-style stroke icons (inner paths only)
 "arrow-right": '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
 "arrow-left": '<path d="M19 12H5"/><path d="m12 19-7-7 7-7"/>',
 "chevron-left": '<path d="m15 18-6-6 6-6"/>',
 "chevron-right": '<path d="m9 18 6-6-6-6"/>',
 "check": '<path d="M20 6 9 17l-5-5"/>',
 "mail": '<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>',
 "phone": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>',
 "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0"/><circle cx="12" cy="10" r="3"/>',
 "bulb": '<path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/>',
 "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
 "shield": '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>',
 "trend": '<path d="M16 7h6v6"/><path d="m22 7-8.5 8.5-5-5L2 17"/>',
 "chart": '<path d="M3 3v16a2 2 0 0 0 2 2h16"/><path d="M7 16v-5"/><path d="M12 16V8"/><path d="M17 16v-3"/>',
 "award": '<circle cx="12" cy="8" r="6"/><path d="m15.48 12.89 1.51 8.53a.5.5 0 0 1-.81.47l-3.58-2.69a1 1 0 0 0-1.2 0l-3.58 2.69a.5.5 0 0 1-.81-.47l1.51-8.53"/>',
 "briefcase": '<path d="M16 20V4a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/><rect width="20" height="14" x="2" y="6" rx="2"/>',
 "code": '<path d="m16 18 6-6-6-6"/><path d="m8 6-6 6 6 6"/>',
 "phone-app": '<rect width="14" height="20" x="5" y="2" rx="2"/><path d="M12 18h.01"/>',
 "cloud": '<path d="M17.5 19H9a7 7 0 1 1 6.71-9h1.79a4.5 4.5 0 1 1 0 9"/>',
 "db": '<ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5v14a9 3 0 0 0 18 0V5"/><path d="M3 12a9 3 0 0 0 18 0"/>',
 "cpu": '<rect width="16" height="16" x="4" y="4" rx="2"/><rect width="6" height="6" x="9" y="9" rx="1"/><path d="M15 2v2"/><path d="M15 20v2"/><path d="M2 15h2"/><path d="M2 9h2"/><path d="M20 15h2"/><path d="M20 9h2"/><path d="M9 2v2"/><path d="M9 20v2"/>',
 "headset": '<path d="M3 14h3a1 1 0 0 1 1 1v4a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1z"/><path d="M18 14h3v5a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1z"/><path d="M3 14a9 9 0 0 1 18 0"/><path d="M21 19v1a3 3 0 0 1-3 3h-3"/>',
 "globe": '<circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/>',
 "gamepad": '<path d="M6 11h4"/><path d="M8 9v4"/><path d="M15 12h.01"/><path d="M18 10h.01"/><path d="M17.32 5H6.68a4 4 0 0 0-3.98 3.59c-.01.05-.01.1-.02.15C2.6 9.42 2 14.46 2 16a3 3 0 0 0 3 3c1 0 1.5-.5 2-1l1.41-1.41A2 2 0 0 1 9.83 16h4.34a2 2 0 0 1 1.41.59L17 18c.5.5 1 1 2 1a3 3 0 0 0 3-3c0-1.54-.6-6.58-.69-7.26 0-.05 0-.1-.01-.15A4 4 0 0 0 17.32 5"/>',
 "heart": '<path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7z"/><path d="M3.22 13H9.5l.5-1 2 4.5 2-7 1.5 3.5h5.27"/>',
 "card": '<rect width="20" height="14" x="2" y="5" rx="2"/><path d="M2 10h20"/>',
 "cap": '<path d="M22 10v6"/><path d="m2 10 10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/>',
 "cart": '<circle cx="8" cy="21" r="1"/><circle cx="19" cy="21" r="1"/><path d="M2 2h2l2.66 12.42a2 2 0 0 0 2 1.58h9.78a2 2 0 0 0 1.95-1.57l1.65-7.43H5.12"/>',
 "landmark": '<path d="M10 18v-7"/><path d="M11.12 2.2a2 2 0 0 1 1.76 0l7.87 3.85c.47.23.31.95-.22.95H3.47c-.53 0-.69-.72-.22-.95z"/><path d="M14 18v-7"/><path d="M18 18v-7"/><path d="M3 22h18"/><path d="M6 18v-7"/>',
 "truck": '<path d="M14 18V6a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2v11a1 1 0 0 0 1 1h2"/><path d="M15 18H9"/><path d="M19 18h2a1 1 0 0 0 1-1v-3.65a1 1 0 0 0-.22-.62l-3.48-4.35A1 1 0 0 0 17.52 8H14"/><circle cx="17" cy="18" r="2"/><circle cx="7" cy="18" r="2"/>',
 "search": '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
 "clipboard": '<rect width="8" height="4" x="8" y="2" rx="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><path d="M12 11h4"/><path d="M12 16h4"/><path d="M8 11h.01"/><path d="M8 16h.01"/>',
 "terminal": '<path d="m4 17 6-6-6-6"/><path d="M12 19h8"/>',
 "rocket": '<path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91 0z"/><path d="m12 15-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z"/><path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0"/><path d="M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5"/>',
 "zap": '<path d="M4 14a1 1 0 0 1-.78-1.63l9.9-10.2a.5.5 0 0 1 .86.46l-1.92 6.02A1 1 0 0 0 13 10h7a1 1 0 0 1 .78 1.63l-9.9 10.2a.5.5 0 0 1-.86-.46l1.92-6.02A1 1 0 0 0 11 14z"/>',
 "buoy": '<circle cx="12" cy="12" r="10"/><path d="m4.93 4.93 4.24 4.24"/><path d="m14.83 9.17 4.24-4.24"/><path d="m14.83 14.83 4.24 4.24"/><path d="m9.17 14.83-4.24 4.24"/><circle cx="12" cy="12" r="4"/>',
 "info": '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/>',
 "external": '<path d="M15 3h6v6"/><path d="M10 14 21 3"/><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>',
 "send": '<path d="M14.54 4.16a2 2 0 0 1 2.72-.73l3.31 1.91a2 2 0 0 1 .73 2.73L12.5 22.5l-2.6-6.4-6.4-2.6z"/>',
 "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
 "building": '<rect width="16" height="20" x="4" y="2" rx="2"/><path d="M9 22v-4h6v4"/><path d="M8 6h.01"/><path d="M16 6h.01"/><path d="M8 10h.01"/><path d="M16 10h.01"/><path d="M8 14h.01"/><path d="M16 14h.01"/>',
 "lock": '<rect width="18" height="11" x="3" y="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
 "file": '<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7z"/><path d="M14 2v5h6"/><path d="M8 13h8"/><path d="M8 17h5"/>',
 "layers": '<path d="M12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.91a2 2 0 0 0 1.66 0l8.58-3.9a1 1 0 0 0 0-1.83z"/><path d="m6.08 10.37-3.5 1.59a1 1 0 0 0 0 1.81l8.6 3.91a2 2 0 0 0 1.65 0l8.58-3.9a1 1 0 0 0 0-1.83l-3.5-1.59"/>',
 "sparkles": '<path d="M9.94 5.33 12 2l2.06 3.33 3.69.86-2.48 2.85.34 3.77L12 11.34l-3.61 1.47.34-3.77L6.25 6.2z"/><path d="M5 16.5 6 14l1 2.5 2.5 1L7 18.5 6 21l-1-2.5L2.5 17.5z"/><path d="M18 14.5 19 12l1 2.5 2.5 1-2.5 1-1 2.5-1-2.5-2.5-1z"/>',
 "linkedin": '<path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-4 0v7h-4v-12h4v1.5A6 6 0 0 1 16 8z"/><rect width="4" height="12" x="2" y="9"/><circle cx="4" cy="4" r="2"/>',
 "github": '<path d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.4 5.4 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4"/><path d="M9 18c-4.51 2-5-2-7-2"/>',
 "youtube": '<path d="M2.5 17a24 24 0 0 1 0-10 2 2 0 0 1 1.4-1.4 49 49 0 0 1 16.2 0A2 2 0 0 1 21.5 7a24 24 0 0 1 0 10 2 2 0 0 1-1.4 1.4 49 49 0 0 1-16.2 0A2 2 0 0 1 2.5 17"/><path d="m10 15 5-3-5-3z"/>',
}

def icon(name, cls=""):
    c = ' class="%s"' % cls if cls else ""
    return ('<svg%s viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>' % (c, I[name]))

NAV = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("services.html", "Services"),
    ("industries.html", "Industries"),
    ("work.html", "Our Work"),
    ("careers.html", "Careers"),
    ("blog.html", "Blog"),
    ("contact.html", "Contact"),
]

SERVICES = [
    ("custom-software", "code", "", "Custom Software Development",
     "Tailored software solutions for your unique business needs.",
     ["Web and desktop application engineering", "System software and platform tooling",
      "API design, integrations and automation", "Legacy modernisation and re-platforming"]),
    ("mobile-apps", "phone-app", "violet", "Mobile App Development",
     "High-performance apps for iOS and Android.",
     ["Native Android and iOS development", "Cross-platform apps with Flutter and React Native",
      "Offline-first flows and secure authentication", "Store submission, analytics and release support"]),
    ("cloud-devops", "cloud", "cyan", "Cloud &amp; DevOps",
     "Scalable, secure and cost-efficient cloud solutions.",
     ["AWS, Azure and Google Cloud architecture", "Migration planning and zero-surprise cutovers",
      "CI/CD, containers and infrastructure as code", "Monitoring, hardening and cost optimisation"]),
    ("ai-data", "db", "amber", "AI &amp; Data Solutions",
     "Turning data into smarter decisions.",
     ["LLM workflows, assistants and RAG systems", "Data pipelines, warehousing and reporting",
      "Prediction models and document intelligence", "Evaluation, guardrails and human review loops"]),
    ("it-consulting", "headset", "rose", "IT Consulting &amp; Support",
     "Expert guidance and ongoing support.",
     ["Technology strategy and architecture review", "Managed support and maintenance contracts",
      "Dedicated engineers and team augmentation", "Training programmes and knowledge transfer"]),
    ("web-portals", "globe", "green", "Web &amp; Portal Development",
     "Modern, secure and user-friendly web solutions.",
     ["Corporate websites and content platforms", "Citizen, partner and employee portals",
      "E-commerce and marketplace builds", "Accessibility, SEO and performance engineering"]),
]

EXTRA_SERVICES = [
    ("game-development", "gamepad", "violet", "Game Development",
     "Playable products built end to end &mdash; from gameplay systems to store launch.",
     ["2D and 3D gameplay engineering", "Progression, scoring and leaderboard systems",
      "Live operations and seasonal content", "Publishing and post-launch support"]),
    ("electronics", "cpu", "cyan", "Electronics &amp; Hardware Solutions",
     "Sourcing, assembly, servicing and support for computing and electronic devices.",
     ["Computer systems, parts and accessories", "Device assembly, servicing and repair",
      "Procurement and lifecycle consulting", "Hardware and software integration"]),
    ("outsourcing", "layers", "amber", "Technology Process Outsourcing",
     "Back-office and IT-enabled operations run as a dependable extension of your team.",
     ["Back-office and data operations", "Content, transcription and data services",
      "Information systems maintenance", "Support desks and training centres"]),
]

INDUSTRIES = [
    ("healthcare", "heart", "Healthcare", "#0A3EA8", "#041A33",
     "Patient platforms, clinic operations and records systems built for privacy, uptime and clarity.",
     ["Practice and clinic management", "Patient portals and appointment flows",
      "Health records and document handling", "Compliance-conscious data design"]),
    ("fintech", "card", "FinTech", "#00348F", "#031428",
     "Money movement, records and reporting engineered for accuracy, auditability and trust.",
     ["Personal and business finance tools", "Secure document and record vaults",
      "Payments, billing and reconciliation", "Audit trails and access control"]),
    ("education", "cap", "Education", "#0B4BB8", "#04182F",
     "Learning, assessment and placement products that scale from a classroom to a cohort.",
     ["Learning and assessment platforms", "Interview and exam preparation systems",
      "Progress analytics and reporting", "Content delivery at scale"]),
    ("ecommerce", "cart", "E-Commerce", "#063C9E", "#02122A",
     "Storefronts, marketplaces and order systems designed to convert and to keep running.",
     ["Storefronts and marketplace platforms", "Catalogue, cart and checkout engineering",
      "Order, inventory and logistics integration", "Performance and conversion tuning"]),
    ("government", "landmark", "Government", "#0A3EA8", "#020D1C",
     "Citizen-facing portals and departmental systems built for accessibility and accountability.",
     ["Citizen service portals", "Departmental workflow systems",
      "Accessibility and multi-language support", "Reporting and transparency dashboards"]),
    ("logistics", "truck", "Logistics", "#004AC6", "#03152C",
     "Tracking, dispatch and fleet visibility with the reliability field operations demand.",
     ["Shipment and consignment tracking", "Dispatch, routing and fleet tools",
      "Warehouse and inventory systems", "Driver and field mobile apps"]),
]

PROCESS = [
    ("01", "search", "Discover", "Understand your goals, users, constraints and the systems already in place."),
    ("02", "clipboard", "Plan", "Agree a clear roadmap, architecture, milestones and success criteria."),
    ("03", "terminal", "Build", "Develop, test and iterate in short cycles with visible progress throughout."),
    ("04", "rocket", "Deliver", "Deploy, hand over and support the product for long-term success."),
]

TESTIMONIALS = [
    ("Kirosys delivered a clean, fast and secure product experience. Communication was direct, "
     "timelines were realistic, and every release felt carefully tested.",
     "Priya Sharma", "Product Founder &middot; Product Engineering"),
    ("Our cloud migration was handled with a lot of discipline. Kirosys reduced deployment friction, "
     "improved monitoring, and gave us a setup our internal team can actually own.",
     "Siddharth Rao", "CTO &middot; Cloud Services"),
    ("JiQuest made interview practice feel structured instead of stressful. The mock sessions and "
     "progress feedback helped me focus on the exact areas I needed to improve.",
     "Aarav Mehta", "Software Engineer &middot; JiQuest"),
    ("The finance and document workflow felt thoughtfully designed. It gave our team one place to "
     "organise sensitive records without making the experience complicated.",
     "Ananya Iyer", "Operations Lead &middot; JiVault"),
]

# slug, tag, name, subtitle, blurb, visual(ui|phone), link, link label
WORK = [
    ("jivault", "FinTech", "JiVault", "Secure Finance &amp; Document Vault",
     "A secure vault for sensitive financial records, contracts and identity documents, with "
     "encrypted storage, role-based access and finance-first workflows.", "ui", "", ""),
    ("jiquest", "EdTech", "JiQuest", "Interview Preparation Platform",
     "A preparation system with curated question banks, mock sessions, scoring and personalised "
     "learning guidance, backed by practice analytics.", "ui", "https://www.jiquest.com/", "Visit JiQuest"),
    ("kitty-gaming", "Mobile Game", "Kitty Gaming", "Physics-Driven Mobile Game",
     "Quick-session arcade play with progression systems, global leaderboards and replayable "
     "challenge design.", "phone",
     "https://play.google.com/store/apps/details?id=com.kittygaming.kitty_gaming", "View on Play Store"),
    ("battle-brain", "Strategy", "Battle Brain", "Real-Time Strategy Game",
     "Competitive gameplay built around fast decisions, tactical depth, ranked progression and "
     "seasonal events.", "phone",
     "https://play.google.com/store/apps/details?id=com.brainbattle.brain_battle", "View on Play Store"),
    ("arkade", "Arcade", "Arkade", "Modern Arcade Experience",
     "Multiple modes, unlockable content, co-op mechanics and a playful visual language.", "phone",
     "https://play.google.com/store/apps/details?id=com.myappscart.gamevault", "View on Play Store"),
    ("client-platforms", "Client Work", "Client Platforms", "Custom Builds for Client Teams",
     "SaaS dashboards, enterprise portals, AI copilots, marketplace apps and internal platforms "
     "built to order for client teams.", "ui", "contact.html", "Discuss a project"),
]

_BARS = {
 "a": (38, 62, 46, 78, 58, 88),
 "b": (72, 44, 86, 52, 68, 40),
 "c": (46, 54, 40, 92, 62, 74),
}

def mini_ui(variant="a"):
    bars = "".join('<i style="height:%d%%"></i>' % h for h in _BARS.get(variant, _BARS["a"]))
    return ('<div class="mini-ui" aria-hidden="true"><div class="mini-bar"><i></i><i></i><i></i></div>'
            '<div class="mini-body"><div class="mini-side"><i></i><i></i><i></i><i></i></div>'
            '<div class="mini-main"><div class="mini-kpis"><i></i><i></i><i></i></div>'
            '<div class="mini-chart">' + bars + '</div></div></div></div>')

MINI_UI = mini_ui("a")

MINI_PHONE = ('<div class="mini-phone" aria-hidden="true"><div class="mini-hd"></div>'
              '<div class="mini-rows"><i></i><i></i><i></i><i></i><i></i></div></div>')
