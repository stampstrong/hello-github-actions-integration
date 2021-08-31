import http.server
import socketserver
from urllib.parse import urlparse
from urllib.parse import parse_qs

from generate_hello_html import generate_hello_html


PORT = 8080


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        name = ""
        query_components = parse_qs(urlparse(self.path).query)
        if "name" in query_components:
            name = query_components["name"][0]

        html = generate_hello_html(name)
        self.wfile.write(bytes(html, "utf8"))


my_handler = MyHttpRequestHandler

my_server = socketserver.TCPServer(("", PORT), my_handler)
print("Server started at http://localhost:{PORT}")
my_server.serve_forever()
