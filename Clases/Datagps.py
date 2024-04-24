import serial
from Controlador import Controlador
from Data import Data
from tokenService import tokenService
from Controlador import Controlador
from Carrito import Carrito
from datetime import datetime
import time
import json
import requests  
import platform



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
        
    #    
                        
    def readgps(self):
        ser = serial.Serial('COM4', 19200)

        try:
            while True:
                # Lee datos del puerto serie
                data = ser.readline().decode().strip()
                print(data)
                # Extraer números de la cadena "gps-873829,6743428" usando expresiones regulares
                numeros = re.findall(r'\d+', data)
                if len(numeros) >= 2:
                    latitud, longitud = numeros[:2]  # Tomar los dos primeros números como latitud y longitud
                    # Realizar el POST con los números
                    self.enviar_sensor(latitud, longitud)
                    
        except KeyboardInterrupt:
            ser.close() # Cierra el puerto serie cuando se interrumpe el programa
        
    def enviar_sensor(self, latitud, longitud):
        controlador = Controlador()
        carrito = Carrito()

        sensor_tipo = 'Gps'
        unidad = 'lat,long'  # Unidad para las coordenadas
        sensor_id = '00'  # Id del sensor (podrías cambiarlo según tu necesidad)
        valor = f'{latitud},{longitud}'  # Concatenar latitud y longitud
        
        device_code = carrito.device_code()
        api_url = f"http://backend.mylittleasistant.online:8000/api/device/{sensor_tipo}/store"
        
        try:
            response = requests.post(api_url, headers=codeserv.get_headers(), json={"data": [{
                "Device": device_code,
                "Tipo": sensor_tipo,
                "Unidad": unidad,
                "NoSensor": sensor_id,
                "Valor": valor,
                "Datetime": datetime.now().strftime("%d/%m/%Y %H:%M")
            }]})
            response.raise_for_status()
            print(response.json())
            print("Sensor enviado:", sensor_tipo, valor)
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
        except Exception as e:
            print("Error al enviar los datos:", e, "guardando en local")
            self.guardar_localmente({"data": [{
                "Device": device_code,
                "Tipo": sensor_tipo,
                "Unidad": unidad,
                "NoSensor": sensor_id,
                "Valor": valor,
                "Datetime": datetime.now().strftime("%d/%m/%Y %H:%M")
            }]})

    def guardar_localmente(self, json_data):
        with open('Clases/json/data.json', 'a') as file:
            file.write(json.dumps(json_data, indent=4) + '\n')

    
    
if __name__ == "__main__":    
        datagps = Datagps()
        datagps.readgps()
        
    

