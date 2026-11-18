"""UNO Q Piano: serve the browser piano UI from the UNO Q Linux processor."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import os


WEB_DIR = Path(__file__).resolve().parent.parent / "web"
PORT = int(os.environ.get("PORT", "8000"))


class PianoHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(WEB_DIR), **kwargs)

    def log_message(self, fmt, *args):
        print("[web] " + (fmt % args))


if __name__ == "__main__":
    server = ThreadingHTTPServer(("0.0.0.0", PORT), PianoHandler)
    print(f"UNO Q Piano is ready on port {PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
