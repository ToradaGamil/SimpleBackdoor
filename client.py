import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = input("Type IP : ")
port = int(input("Type port : "))
soc.connect((ip, port))
while 1:
    data = input("")
    if not data:
        break
    soc.sendall(data)
    data = soc.recv(1024)
    print(data)
    data = soc.recv(1024)
    print(data)
soc.close()
