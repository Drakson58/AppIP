import re

class ValidaMsg:
    
    _msgSeparada = list()
    
    def __init__(self, msgCliente):
        self._msgCliente = msgCliente
        

    def getMsgCliente(self):
        return self._msgCliente
    def getMsgSeparada(self):
        return self._msgSeparada
    
    def setMsgCliente(self, msgCliente):
        self._msgCliente = msgCliente
        return self._msgCliente
    def setMsgSeparada(self, _msgSeparada):
        self._msgSeparada = _msgSeparada
        return self._msgSeparada
    

    def validaPontos(self):
        if self._msgCliente.count('.') == 3:
            return 'PontosValidos'
        else:
            return 'PontosInvalidos'
        
    
    def validaCampos(self):
        # Se todos os campos são números.
        campos = self._msgCliente.split('.')
        for i in range(0, 4):
            if campos[i].isdigit():
                self._msgSeparada.append(int(campos[i]))
            else:
                return 'CamposInvalidos'
        # Se os campos não ultrapassa o tamanho de 3 caracteres.
        for i in range(0, 4):
            if len(str(self._msgSeparada[i])) < 4:
                self._msgSeparada[i] = self._msgSeparada[i]
            else:
                return 'CamposInvalidos'
        # Verifica se os campos não passam de 255.
        for i in range(0, 4):    
            if self._msgSeparada[i]/2 > 127.5:
                return 'CamposInvalidos'
        return self._msgSeparada

msg = ValidaMsg('127.0.0.1')
print(msg.validaCampos())
print(msg.validaPontos())
msg = msg.validaCampos()
print(msg[0])