import socket
import os
import platform

srv_addr = input("Type the server IP address: ")
srv_port = int(input("Type the server port: "))
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.bind((srv_addr, srv_port))
soc.listen(1)
print("Server started!!!")
connection, address = soc.accept()
print("Client connected with address:", address)
while 1:
    data = connection.recv(1024)
    if not data:
        break
    print(data.decode('utf-8'))
    connection.sendall(b'-- Message Received --\n')
    res = ""
    if data == "Get Info":
        data = platform.uname()
        for d in data:
            res += d + "\n"
        connection.sendall(res)
    elif data[0:2] == "ls":
        path = data.split()[1]
        for f in os.listdir(path):
            res += f + "\n"
        connection.sendall(res)
    else:
        connnection.sendall("""Menu:
        Get Info
        ls <path>
        """)
connection.close()
