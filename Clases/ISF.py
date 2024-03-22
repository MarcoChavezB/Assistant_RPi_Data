class   ISF():
    def __init__(self, No_Sensor=None, puertos=None):
        super().__init__()
        self.isConected= No_Sensor==None and puertos==None 
        
        if self.isConected:  
            self.arreglo=[]
            
        self.arreglo=None
        self.tipo= No_Sensor
        self.unidad = puertos
        
        
    