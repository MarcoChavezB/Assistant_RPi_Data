import json
from datetime import datetime
from Controlador import Controlador
import time
import requests  
import platform

class pruebas:
    def read_serial():
        controlador = Controlador() 
        serial_data = []
        for data in controlador.read_serial():
            serial_data.append(data)
        return serial_data

def enviar_data(sensor_tipo, unidad, sensor_id, valor):
    json_data = {
        "Device": "kksi82o",
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
        response = requests.post('url_de_tu_api', json=json_data)
        print("Data enviada:", json_data)
        print("Respuesta de la API:", response.text)
    except Exception as e:
        print("Error al enviar los datos:", e)
        guardar_localmente(json_data)


def guardar_localmente(json_data):
    with open('data.json', 'a') as file:
        file.write(json.dumps(json_data) + '\n')


controlador = Controlador()

sensores_a_enviar_cada_10_segundos = ['Temp', 'Peso']
ultimo_envio = {sensor: 0 for sensor in sensores_a_enviar_cada_10_segundos}

while True:
    for data in controlador.read_serial():
        sensor_tipo, unidad, sensor_id, valor = data

        if sensor_tipo in sensores_a_enviar_cada_10_segundos:
            if (time.time() - ultimo_envio[sensor_tipo]) >= 20:
                enviar_data(sensor_tipo, unidad, sensor_id, valor)
                ultimo_envio[sensor_tipo] = time.time()
        else:
            enviar_data(sensor_tipo, unidad, sensor_id, valor)

    time.sleep(2)
