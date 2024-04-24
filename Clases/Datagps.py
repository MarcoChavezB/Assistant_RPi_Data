import serial
from Controlador import Controlador
from Data import Data
from tokenService import tokenService
from Controlador import Controlador\



class Datagps(Data):
    def __init__(self, latitud=None, longitud=None):
        super().__init__()
        self.isConected= latitud==None and longitud==None 
        if self.isConected:  
            self.arreglo=[]
    
        self.arreglo=None
        codeserv = tokenService()
   
    def readgps(self):
            ser = serial.Serial('COM4', 19200)
            #

            try:
                    while True:
                        # Lee datos del puerto serie
                        data = ser.readline().decode().strip()
                        print( data)

            except KeyboardInterrupt:
                ser.close() # Cierra el puerto serie cuando se interrumpe el programa
        

    
    
if __name__ == "__main__":    
        datagps = Datagps()
        datagps.readgps()
        
    

