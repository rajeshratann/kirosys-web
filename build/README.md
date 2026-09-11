# Build scripts

The deployed site is the plain HTML in the project root — nothing here is needed to serve it.

These scripts only exist so the repeated chrome (top bar, nav, footer, CTA band, cards) is
defined once. Run them after editing shared content:

```sh
cd build
python3 build.py          # rewrites every .html page in the project root
```

| File | What lives there |
| --- | --- |
| `partials.py` | Contact details, navigation, services, industries, work items, testimonials, icon set |
| `layout.py` | Page shell (`<head>`, topbar, header, footer) and reusable section blocks |
| `build_home.py` | Home page |
| `build_a.py` | About, Services, Industries |
| `build_b.py` | Our Work, Careers, Blog |
| `build_c.py` | Contact, Privacy, Terms, Thank you, 404, redirect stubs |

| `serve.py` | Local preview server that resolves extensionless URLs like GitHub Pages |

Requires Python 3 only — no packages.

Links are written without `.html` (see the root README). `layout.clean_urls()` strips the
extension on generation, so keep writing `about.html` in the generator source — the
transform handles it.

If you prefer to edit the HTML directly, that is fine too: just be aware that re-running
these scripts will overwrite the generated pages.
