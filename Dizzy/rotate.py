import time
from http.server import HTTPServer, BaseHTTPRequestHandler

# Create a string of characters to rotate through
flag = "ctcyber{w0w_i_r3ally_h0p3_y0u_didnt_do_th1s_manually}"
index = 0
# Create a custom class to handle the request
class RequestHandler(BaseHTTPRequestHandler):
    
    # Create function to handle the GET request
    def do_GET(self):
        # Set the response code and message
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        
        ptr = index % len(flag)
        # Get the character to display
        character = flag[ptr]
        
        # Create the message to send
        #message = f'<html><body><h1>{character}</h1></body></html>'
        message = character
        # Encode the message and write
        self.wfile.write(message.encode())
        
        # Rotate the string
        #string = string[1:] + string[0]

# Create a web server with the handler
print(f"Listening on port 8081")
server = HTTPServer(('0.0.0.0', 8081), RequestHandler)

# Run the server
while True:
    server.handle_request()
    time.sleep(0.5)
    index += 1