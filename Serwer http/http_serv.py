import http.server
import socketserver

html = '''<html>
    <head>
        <title>Laboratorium</title>
    </head>
    <body>
        Content
    </body>
</html>'''

IP = input("Podaj adress ip: ")
PORT = input("Podaj numer portu: ")

content = input("Wpisz tresc na stronie: ")

with open('index.html', 'w',-1,'UTF-8') as file:
    file.write(html.replace('Content', content.strip()))

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("127.0.0.1", 9000), Handler) as httpd:
    httpd.serve_forever()
