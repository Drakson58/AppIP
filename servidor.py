import socket
from Classes.validaMsg import ValidaMsg
from Classes.classeIp import ClasseIp
from Classes.tipoIP import TipoIp
import threading

def servidor():
    host = ''
    port = 5001
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    orig = (host, port)
    servidor.bind(orig)
    servidor.listen(1)
    servidor.listen(5)


    while True:
        conexaoCliente, ipCliente = servidor.accept()
        print('Conectado por: ', ipCliente)

        #Recebendo msg
        msg = conexaoCliente.recv(1024)
        msg = msg.decode()
        if msg == 'sair':
            print('Conexão fechada por: ', ipCliente)
            conexaoCliente.close()
            break
        else:
            # Enviando para a validação.
            ipSeparado = ValidaMsg(msg)
            if(ipSeparado.validaPontos()) == 'PontosValidos':
                if(ipSeparado.validaCampos()) == 'CamposInvalidos': # Erro de campos invalidos.
                    print('Campos invalidos')
                else:
                    classeIP = ClasseIp(ipSeparado.getMsgSeparada())
                    if classeIP.classeTipo() == 'A':
                        #print('Classe A Tipo: local')
                        respostaServidor = 'Classe: A\nTipo: local'
                    elif classeIP.classeTipo() == 'B':
                        #print('Classe B Tipo: local')
                        respostaServidor = 'Classe: B\nTipo: local'
                    elif classeIP.classeTipo() == 'loopback':
                        #print('Classe: loopback')
                        respostaServidor = 'Classe: Loopback'
                    elif classeIP.classeTipo() == 'C':
                        #print('Classe C Tipo: local')
                        respostaServidor = 'Classe: C\nTipo: local'
                    elif classeIP.classeTipo() == 'D':
                        #print('Classe D Tipo: local')
                        respostaServidor = 'Classe D\nTipo: local'
            else:
                print('ERRO!')
                respostaServidor = 'ERRO! Verifique todos os campos digitados.'
            ipSeparado.getMsgSeparada().clear() # Limpando a lista.
        conexaoCliente.send(respostaServidor.encode()) # Enviando resposta do servidor.

x = threading.Thread(target=servidor,args=())
x.start()