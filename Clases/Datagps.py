from Controlador import Controlador
from Data import Data
from tokenService import tokenService
from Controlador import Controlador


class Datagps(Data):
    def __init__(self, latitud=None, longitud=None):
        super().__init__()
        self.isConected= latitud==None and longitud==None 
        if self.isConected:  
            self.arreglo=[]
    
        self.arreglo=None
        codeserv = tokenService()
    
    
if __name__ == "__main__":    
        datagps = Datagps()
        Controlador.read_serial()
        
    

