import socket

#print(dir(socket))

def przyklad1():
    name = socket.gethostbyname('python.org')
    print(name)
    port = socket.getservbyname('http')
    print(port)

def przyklad2():
    adres_ip = '8.8.4.4'
    name = socket.gethostbyaddr(adres_ip)

    print(f'Nazwa domeny dla adresu ip: {adres_ip} to: {name[0]}')

przyklad2()