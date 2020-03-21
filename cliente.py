import socket

host = ''
porta = 5001
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((host, porta)) # Se conecantando ao servidor.

print("Para sair digite: 'sair'\n")
while True:
    # Enviando msg
    msg = input('Digite um Ip:')
    cliente.send(msg.encode())
    if msg == 'sair':   
        cliente.close()
        break
    #Recebendo msg do servidor
    resposta = cliente.recv(1024)
    print(resposta.decode())