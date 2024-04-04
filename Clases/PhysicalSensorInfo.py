from Data import Data

class PhysicalSensorInfo():
    def __init__(self, No_Sensor=None, puertos=None):
        super().__init__()
        self.isConected= No_Sensor==None and puertos==None 
        
        if self.isConected:  
            self.arreglo=[]
            
        self.arreglo=None
        self.tipo= No_Sensor
        self.unidad = puertos
        
    def cargar_desde_archivo(self,nombre_archivo):
            try:

                data = self.readjson(nombre_archivo)
                self.objetos(data)
                print(f"\nDatos cargados desde '{nombre_archivo}'\n")
            except FileNotFoundError:
                print(f"Archivo '{nombre_archivo}' no encontrado. Iniciando con lista vacía.\n")


    def objetos(self,data):  
        self.arreglo=[] 
        if not data:
                print("No hay Informacion del sensor fisico para mostrar")
                return False
        isf_list = []
        for isf_data in data:
                isf_instance = PhysicalSensorInfo(
                No_Sensor=isf_data['No_Sensor'],
                puertos=isf_data['puertos'],
                )
                data =Data()
                data.objetos_data(isf_data["ventas"])
                isf_instance.data=data
                isf_list.append(isf_instance)
                self.arreglo = isf_list 

        for isf_instance in isf_list:
            print(f"\t\tNumero de Sensor {isf_instance.No_Sensor}")
            print(f"\t\tPuertos: {isf_instance.puertos}")
           
            if hasattr(isf_instance, 'data'):
                print("Data:")
                isf_instance.data.ver()

    print("\n")  