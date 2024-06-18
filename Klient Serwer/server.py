import socket

ip = '127.0.0.1'
port = 4444

serwer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serwer.bind((ip, port))
serwer.listen(2)

client, addr = serwer.accept()

print('Połączenie z ', addr)

while 1:
    data=client.recv(1024)
    print(data)
    client.send(data)