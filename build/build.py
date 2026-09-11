#!/usr/bin/env python3
"""Regenerate every page of the Kirosys site.

The site is plain static HTML — the generated .html files in the project root are
what gets deployed, and they work on their own. This script exists only so the
shared chrome (top bar, navigation, footer, CTA band, cards) lives in one place
instead of being copy-pasted across a dozen pages.

    cd build && python3 build.py

Edit content in:
    partials.py   site data — contact details, nav, services, industries, work, testimonials, icons
    layout.py     page shell, header, footer, and the reusable section blocks
    build_*.py    the per-page content
"""
import runpy, sys, os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
for mod in ("build_home", "build_a", "build_b", "build_c"):
    runpy.run_module(mod, run_name="__main__")
