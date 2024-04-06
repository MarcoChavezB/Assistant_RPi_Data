import json
from datetime import datetime
from Controlador import Controlador
import time
import requests  
import platform
class   Data():
    def __init__(self, valor=None, fecha_hora=None):
        super().__init__()
        self.isConected= valor==None and fecha_hora==None 
        if self.isConected:  
            self.arreglo=[]
    
        self.arreglo=None
        self.tipo= valor
        self.unidad = fecha_hora
        
        
    