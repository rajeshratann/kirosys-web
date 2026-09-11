#!/usr/bin/env python3
"""Local preview that mimics GitHub Pages URL resolution.

The site links to /about rather than /about.html, which neither file:// nor
python -m http.server resolves. This serves the project root the way Pages does.

    python3 build/serve.py          # http://localhost:8000
"""
import functools, http.server, os, socketserver, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Handler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        local = super().translate_path(path)
        if not os.path.exists(local) and not local.endswith(("/", ".html")):
            if os.path.exists(local + ".html"):
                return local + ".html"
        return local

    def send_error(self, code, message=None, explain=None):
        if code == 404:
            page = os.path.join(ROOT, "404.html")
            if os.path.exists(page):
                body = open(page, "rb").read()
                self.send_response(404)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                return
        super().send_error(code, message, explain)


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", port), functools.partial(Handler, directory=ROOT)) as httpd:
        print("Serving %s at http://localhost:%d (Ctrl+C to stop)" % (ROOT, port))
        httpd.serve_forever()
