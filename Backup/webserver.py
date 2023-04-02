import base64
import http.server
import json

class BasicAuthHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.is_authenticated():
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Authenticated!')
        else:
            self.send_response(401)
            self.send_header('WWW-Authenticate', 'Basic realm="My Realm"')
            self.end_headers()

    def is_authenticated(self):
        auth = self.headers.get('Authorization')
        if auth is None:
            return False
        auth = auth.split()
        if len(auth) != 2:
            return False
        if auth[0].lower() != "basic":
            return False
        uname, passwd = base64.b64decode(auth[1]).decode("utf-8").split(":")
        return uname == "admin" and passwd == "CtCyB3R_is_c00l"

httpd = http.server.HTTPServer(('172.25.30.153', 8080), BasicAuthHandler)
httpd.serve_forever()
