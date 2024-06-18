import socket

ip_serv = '127.0.0.1'
port_serv = 4444

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip_serv, port_serv))

print(f'Połączony do serwera (Adress ip: {ip_serv} i port: {port_serv}) ')

while 1:
    data = input("Wprowadz dane do wyslania")
    client.send(bytes(data.encode('utf-8')))

    if data=="Stop":
        break

client.close()