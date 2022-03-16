import http.server
import socketserver
from darknetInterface import findObjects
import urllib.parse
import json

PORT = 80

class MyCustomRequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        queryString = urllib.parse.urlparse(self.path).query
        
        query = urllib.parse.parse_qs(queryString)
        
        print("Query: ", query)
        
        if 'image' in query:
            imageUrl = query.get('image')[0]
            print(imageUrl)
            
            concept = findObjects(imageUrl)
                                                
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            payload = concept.encode("utf8")
            self.wfile.write(payload)
        else:
            self.send_response(400)
            self.send_header("Content-type", "text/plain")
            self.end_headers()       
            payload = "No image URL specified"
            payload = payload.encode("utf8")
            self.wfile.write(payload)
                
httpd = socketserver.TCPServer(("", PORT), MyCustomRequestHandler)
print("serving at port", PORT)
httpd.serve_forever()

