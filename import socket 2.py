import socket
import datetime as dt
def InfoArd():
    try:
        serverIP = '192.168.1.100'
        serverPort = 8888
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (serverIP, serverPort)
        sock.connect(server_address)
    
        dado = sock.recv(1024).decode('utf-8').split()

        if dado:
            valorx = int(dado[0].replace(".",""))
            valory = int(dado[1].replace(".",""))
            return [valorx,valory]
    except:
        hora = [dt.datetime.now().hour,dt.datetime.now().min,dt.datetime.now().second]
        print(f"Arduino Desconectado as {hora[0]}h {hora[1]}min {hora[2]}s")
        return [0,0]
    finally:
        sock.close()
def Control():
    if InfoArd[0] >= 300:
        print("Baixo")
        #Comando para Baixo
    if InfoArd[0] <= -300:
        print("Cima")
        #Comando para Cima
    if InfoArd[0] >= 300:
        print('Esquerda')
        #Comando para Esquerda
    if InfoArd[0] <= -300:
        print('direita')
        #Comando para Direita
#codigo