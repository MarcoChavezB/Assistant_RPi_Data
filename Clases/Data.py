import json
from datetime import datetime
from Controlador import Controlador
from Carrito import Carrito
from tokenService import tokenService
from Datagps import Datagps
import time
import requests  
import platform
class Data(Carrito):
    def __init__(self, valor=None, fecha_hora=None):
        super().__init__()
        self.isConected= valor==None and fecha_hora==None 
        if self.isConected:  
            self.arreglo=[]
    
        self.arreglo=None
        self.tipo= valor
        self.unidad = fecha_hora
        codeserv = tokenService()
            
    def sinarduino(self):
        return [
            ['Peso', 'gr', '00', '20.00'],
            ['Gps', ' lat ', ' 02 ', '00'],
            ['Peso', 'gr', '00', '20.00'],
            ['Incli', 'grd', '01', '-0.15'],
            ['Vel', 'm/s', '02', '10.00'],
            ['Temp', 'C', '03', ' NAN'],
            ['Gps', ' lat ', ' 02 ', '00'],
        ]
    def enviar_data(self,sensor_tipo, unidad, sensor_id, valor, deviceCode, api_url):
            json_data = { "data":
                         [
                             {
                "Device": deviceCode,
                "Tipo": sensor_tipo,
                "Unidad": unidad,
                "NoSensor": sensor_id,
                "Valor": valor,
                "Datetime": datetime.now().strftime("%d/%m/%Y %H:%M")
            }
                ]
                    }
            
            try:
                
                if self.arreglo==None:
                    self.arreglo=json_data
                else:
                   if self.arreglo["data"][0]["Valor"]==json_data["data"][0]["Valor"]:
                       print("no se envio el dato porque es el mismo")
                       return
                   else:
                        self.arreglo=json_data
                response = requests.post(api_url, headers = self.codeserv.get_headers(), json=json_data)
                response.raise_for_status()
                print(response.json())
                print("sensor enviado:" , sensor_tipo, valor)
                return response.json()
            except requests.exceptions.HTTPError as err:
                    print(f"HTTP error occurred: {err}")
                    print(f"Response status: {response.status_code}")
                    print(f"Response text: {response.text}")
            except Exception as e:
                        print("Error al enviar los datos:", e, "guardando en local")
                        
                        self.guardar_localmente(json_data)


    def guardar_localmente(self,json_data):
            with open('Clases/json/data.json', 'a') as file:
                file.write(json.dumps(json_data, indent=4) + '\n')


    def enviar_sensor(self):
        controlador = Controlador()
        carrito = Carrito()

        sensores_tiempo = {
            'Peso': 1,
            
            'Incli': 1,
            'Temp': 1,
            'Vel': 1
        }
        ultimo_envio = {sensor: 0 for sensor in sensores_tiempo}
        ultimo_valor = {sensor: None for sensor in sensores_tiempo}
        gps = Datagps()
        while True:
                     for sensor_data in self.sinarduino():
                        sensor_tipo, unidad, sensor_id, valor = sensor_data
                        if sensor_tipo in sensores_tiempo:
                                if (time.time() - ultimo_envio[sensor_tipo]) >= sensores_tiempo[sensor_tipo]:
                                    if valor != ultimo_valor[sensor_tipo]:    
                                        device_code = carrito.device_code()
                                        api_url = f"http://backend.mylittleasistant.online:8000/api/device/{sensor_tipo}/store"
                                        self.enviar_data(sensor_tipo, unidad, sensor_id, valor, device_code, api_url )
                                        ultimo_valor[sensor_tipo] = valor
                                        ultimo_envio[sensor_tipo] = time.time()
                                        #gps.readgps()
                        else:
                                print("Hola, este sensor no esta en la lista de sensores " + sensor_tipo)
                                
                        
                        time.sleep(1)         
                        
                   
      
if __name__ == "__main__":    
    data = Data()
    data.enviar_sensor()
