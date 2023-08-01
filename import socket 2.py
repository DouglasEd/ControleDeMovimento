import socket

serverIP = '192.168.1.100'
serverPort = 8888

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (serverIP, serverPort)
sock.connect(server_address)

try:
    while True:
        dado = sock.recv(1024).decode('utf-8').split()

        if dado:
            valorx = int(dado[0].replace(".",""))
            valory = int(dado[1].replace(".",""))
            if valorx >= 300:
                print("Baixo")
            if valorx <= -300:
                print("Cima")
            if valory >= 300:
                print('Esquerda')
            if valory <= -300:
                print('direita')
except KeyboardInterrupt:
    pass
finally:
    sock.close()