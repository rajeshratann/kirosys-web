# Kirosys Technologies — website

Static marketing site for **Kirosys Technologies Private Limited** (kirosys.in),
served by GitHub Pages from the `main` branch root.
No framework, no build step required to deploy: push and Pages publishes the root as-is.

## URLs

Pages are linked without the `.html` extension — `/about`, `/services`, `/work` — because
GitHub Pages resolves `/about` to `about.html` directly (200, no redirect). The files keep
their `.html` names; only the links are clean. Canonical tags and `sitemap.xml` use the
extensionless form.

Because of this, `file://` and `python -m http.server` will not resolve the links. Use the
included preview server, which mimics Pages:

```sh
python3 build/serve.py        # http://localhost:8000
```

## Structure

```
index.html            Home — hero, stats, about, services, industries, process, work, testimonials
about.html            Company story, values, statutory details, directors
services.html         Six core services (#anchors) + additional capabilities + engagement models
industries.html       Healthcare, FinTech, Education, E-Commerce, Government, Logistics
work.html             JiVault, JiQuest, Kitty Gaming, Battle Brain, Arkade, client platforms
careers.html          Why Kirosys, open tracks, how to apply
blog.html             Insights (topics queued, first articles pending)
contact.html          Contact details + enquiry form (#quote)
privacy.html          Privacy policy
terms.html            Terms & conditions
thanks.html           Form success page
404.html              Not found
products.html         → redirects to /work (kept for old inbound links)
cloud.html            → redirects to /services#cloud-devops
robots.txt            Search engine directives
sitemap.xml           Sitemap (update lastmod when content changes)

assets/site.css       Design system — tokens, components, responsive rules
assets/site.js        Progressive enhancement — nav, reveal, counters, carousel
assets/img/           Logo, brand mark, favicons, Open Graph cover (served)
assets/brand/         High-resolution logo masters (not served — for print/press)
build/                Optional page generator + local preview server (see build/README.md)
```

## Brand

Palette is sampled from the Kirosys logo mark:

| Token | Value | Use |
| --- | --- | --- |
| `--blue-600` | `#0057FD` | Primary actions, links, accents |
| `--cyan-400` | `#12D5FD` | Gradient tips, on-dark eyebrows |
| `--navy-950` | `#020D1C` | Hero, CTA band, footer |
| `--ink-900` | `#0A1726` | Headings |
| `--tint` | `#F4F8FD` | Alternating section background |

Logo files: `assets/img/logo-720.png` (light backgrounds), `logo-dark-720.png` (dark
backgrounds), `mark-{128,256}.png` (square mark). High-resolution masters are in `assets/brand/`.

## Editing

Shared chrome (top bar, nav, footer) is repeated in every page. To change it in one
place, edit `build/partials.py` / `build/layout.py` and run:

```sh
cd build && python3 build.py
```

Otherwise edit the HTML directly — but then avoid re-running the generator, which overwrites it.

## Contact form

`contact.html` posts to formsubmit.co, which forwards submissions to `support@kirosys.in`
and redirects to `thanks.html`. No server-side code is needed.
