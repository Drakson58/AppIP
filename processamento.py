import re

class ValidaMsg:
    
    _msgSeparada = list()
    def __init__(self, msgCliente):
        self._msgCliente = msgCliente

    def getMsgCliente(self):
        return self._msgCliente    

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
        return self._msgSeparada
                
        
                
       
ip = ValidaMsg('103.220.220.22')
print(ip.validaCampos())
