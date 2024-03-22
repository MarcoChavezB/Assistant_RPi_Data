class IGS():
    def __init__(self, tipo=None, unidad=None, descripcion_sensor=None):
        super().__init__()
        self.isConected= tipo==None and unidad==None and descripcion_sensor==None 
        
        if self.isConected:  
            self.arreglo=[]
            
        self.arreglo=None
        self.tipo= tipo
        self.unidad = unidad
        self.descripcion_sensor = descripcion_sensor
        
    
    
    