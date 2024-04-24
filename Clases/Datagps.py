import serial
from Controlador import Controlador
from Data import Data
from tokenService import tokenService
from Controlador import Controlador\

import serial
from Controlador import Controlador

from tokenService import tokenService
from Controlador import Controlador
from Carrito import Carrito
from datetime import datetime
import time
import json
import requests  
import platform



class Datagps():
    def _init_(self, latitud=None, longitud=None):
        super()._init_()
        self.isConected= latitud==None and longitud==None 
        if self.isConected:  
            self.arreglo=[]
    
        self.arreglo=None
        codeserv = tokenService()
   
 
    def readgps(self):
        ser = serial.Serial('/dev/ttyUSB0', 19200)

        try:
            while True:
                # Lee datos del puerto serie
                data = ser.readline().decode().strip()
                print(data)
                if data.startswith("|") and data.endswith("|"):
                        # Elimina los caracteres "|" del principio y final de la cadena
                    data = data.strip("|")
                    print(data)
                    # Divide la cadena en elementos utilizando el carácter "|" como delimitador
                    datos_separados = data.split("|")
                    if len(datos_separados) >= 2:
                        latitud, longitud = datos_separados[:2]  # Tomar los dos primeros elementos como latitud y longitud
                        # Realizar el POST con los datos
                        print(latitud,longitud)
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
            response = requests.post(api_url, headers=self.codeserv.get_headers(), json={"data": [{
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
        with open('Clases/json/gps.json', 'a') as file:
            file.write(json.dumps(json_data, indent=4) + '\n')
    
    
if __name__ == "__main__":    
        datagps = Datagps()
        datagps.readgps()
        
    

