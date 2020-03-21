
class TipoIp:
    
    def __init__(self, ipSeparado):
        self._ipSeparado = ipSeparado
        
    
    def getTipoIp(self):
        return self._ipSeparado
    def setTipoIp(self, ipSeparado):
        self._ipSeparado = ipSeparado
        return self._ipSeparado
    

    def qualIp(self):
        if self._ipSeparado[0] == 127 and self._ipSeparado[3] == 1:
            return 'loopback'
        else:
            return 'local'
