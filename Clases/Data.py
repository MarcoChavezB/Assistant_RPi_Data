import json
from datetime import datetime
from Controlador import Controlador
from Carrito import Carrito
from codeService import codeService
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
        codeserv = codeService()
    
    def read_serial():
                controlador = Controlador() 
                serial_data = []
                for data in controlador.read_serial():
                    serial_data.append(data)
                return serial_data

    def enviar_data(self,sensor_tipo, unidad, sensor_id, valor, deviceCode):
            json_data = {
                "Device": deviceCode,
                "GenericSensorInfo": {
                    "Tipo": sensor_tipo,
                    "Unidad": unidad
                },
                "PhysicalSensorInfo": {
                    "No.Sensor": sensor_id
                },
                "Data": {
                    "valor": valor,
                    "datetime": datetime.now().strftime("%d/%m/%Y %H:%M")
                }
            }

            try:
                api_url = requests.post('http://backend.mylittleasistant.online:8000/api/device/store', json=json_data)     
                
                response = requests.post(api_url, headers = self.codeserv.get_headers(), json=json_data)
                response.raise_for_status()
                print(response.json())
                return response.json()
            except requests.exceptions.HTTPError as err:
                    print(f"HTTP error occurred: {err}")
                    print(f"Response status: {response.status_code}")
                    print(f"Response text: {response.text}")
            except Exception as e:
                        print("Error al enviar los datos:", e)
                        self.guardar_localmente(json_data)


    def guardar_localmente(self,json_data):
            with open('data.json', 'a') as file:
                file.write(json.dumps(json_data, indent=4) + '\n')


    def enviar_sensor(self):
        controlador = Controlador()
        carrito = Carrito()

        sensores_lento = ['Temp', 'Peso']
        ultimo_envio = {sensor: 0 for sensor in sensores_lento}

        while True:
                    for data in controlador.read_serial():
                        sensor_tipo, unidad, sensor_id, valor = data

                        if sensor_tipo in sensores_lento:
                            if (time.time() - ultimo_envio[sensor_tipo]) >= 15:
                                device_code = carrito.device_code()
                                self.enviar_data(sensor_tipo, unidad, sensor_id, valor, device_code )
                                ultimo_envio[sensor_tipo] = time.time()
                        else:
                            self.enviar_data(sensor_tipo, unidad, sensor_id, valor, device_code)
                    
                    time.sleep(2)               
if __name__ == "__main__":    
    data = Data()
    data.enviar_sensor()