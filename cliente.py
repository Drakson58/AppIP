import socket
import json
import threading
import tratamentoiarquivo

class cliente:
    def tipo(self):
        host = '127.0.0.1'
        porta = 5001
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        orig = (host,porta)
        cliente.connect(orig) # Se conecantando ao servidor.

        print("Para sair digite: 'sair'\n")


        with open('iarquivo.json', 'r') as f:
            msg = json.load(f)
        msg = str(msg)
        msg = tratamentoiarquivo.tratamento(msg)
        print(msg)
        #msg = input('Digite o ip:')

        cliente.send(msg.encode())

        #Recebendo msg do servidor
        resposta = cliente.recv(1024)
        print(resposta.decode())
        resposta = resposta.decode()
        cliente.close()
        return resposta
