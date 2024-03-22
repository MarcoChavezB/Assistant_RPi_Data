class Carrito():
    def __init__(self,clave=None, nombre=None, descripcion=None):
        super().__init__()
        self.isConected= clave==None and nombre==None and descripcion==None 
        if self.isConected:  
            self.arreglo=[]
        else:
            self.arreglo=None

            self.clave=clave
            self.nombre = nombre
            self.descripcion = descripcion
            
        
        
       