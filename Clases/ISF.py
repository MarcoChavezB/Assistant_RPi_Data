from Controlador import Controlador
from Carrito import Carrito

class   ISF():
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
        fun_list = []
        for funcion_data in data:
                funcion_instance = Funciones(
                nf=funcion_data['nf'],
                hora_inicio=funcion_data['hora_inicio'],
                duracion=funcion_data['duracion'],
                tipo_proyeccion=funcion_data['tipo_proyeccion'],
                precio_entrada=funcion_data['precio_entrada'],
                pelicula=funcion_data['pelicula'],
                total_ganancias=funcion_data['total_ganancias']
                )
                ventas=Ventas()
                ventas.objetos_ventas(funcion_data["ventas"])
                funcion_instance.ventas=ventas
                fun_list.append(funcion_instance)
                self.arreglo = fun_list 

        for funcion_instance in fun_list:
            print(f"\t\tFunción {funcion_instance.nf}")
            print(f"\t\tHora de inicio: {funcion_instance.hora_inicio}")
            print(f"\t\tDuración: {funcion_instance.duracion}")
            print(f"\t\tTipo de proyección: {funcion_instance.tipo_proyeccion}")
            print(f"\t\tPrecio de entrada: {funcion_instance.precio_entrada}")
            print(f"\t\tPelícula: {funcion_instance.pelicula}")
            print(f"\t\tTotal de ganancias: {funcion_instance.total_ganancias}")

            if hasattr(funcion_instance, 'ventas'):
                print("Ventas:")
                funcion_instance.ventas.ver()

    print("\n")  