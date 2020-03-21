

class ClasseIp:
    
    def __init__(self, ipPartido):
        self._ipPartido = ipPartido
        
    
    def getIpPartido(self):
        return self._ipPartido
    def setIpPartido(self, ipPartido):
        self._ipPartido = ipPartido
        return self._ipPartido
    

    def classeTipo(self):
        if self._ipPartido[0] > 1 and self._ipPartido[0] < 127:
            return 'A'
        elif self._ipPartido[0] > 127 and self._ipPartido[0] < 192:
            return 'B'
        elif self._ipPartido[0] < 128 and self._ipPartido[0] > 126:
            return 'loopback'
        elif self._ipPartido[0] > 191 and self._ipPartido[0] < 224:
            return 'C'
        elif self._ipPartido[0] > 223 and self._ipPartido[0] < 240:
            return 'D'