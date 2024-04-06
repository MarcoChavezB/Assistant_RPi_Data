import json
import random
import string
import platform
import requests
from codeService import codeService

class Carrito():
    def __init__(self,clave=None, nombre=None, descripcion=None):
        super().__init__()
        self.isConected= clave==None and nombre==None and descripcion==None
        if self.isConected:
            self.arreglo=[]

        self.arreglo=None

        self.clave=clave
        self.nombre = nombre
        self.descripcion = descripcion
        self.codeserv = codeService()

    def gen_code(self):
        with open('Clases/json/UniqueCode.json') as json_file:
            data = json.load(json_file)
            deviceCode = data['deviceCode']
            
        print(deviceCode)

        while True:
            if deviceCode is None or deviceCode == "":
                chars = string.ascii_letters + string.digits
                code = ''.join(random.choice(chars) for _ in range(10))
                response = self.api_request(code)
                if response is not None:
                    data['deviceCode'] = code
                    with open('UniqueCode.json', 'w') as json_file:
                        json.dump(data, json_file)
                    break
            else:
                print("Car already exists")
                break

    def api_request(self, code):

        api_url = "http://backend.mylittleasistant.online:8000/api/store/device"

        print(self.codeserv.get_headers())

        body = {
            "code": code,
            "type": "Car",
            "model": "Assistant",
            "os": platform.system(),
        }

        try:
            response = requests.post(api_url, headers=self.codeserv.get_headers(), json=body)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
            print(f"Response status: {response.status_code}")
            print(f"Response text: {response.text}")


if __name__ == "__main__":
    carrito = Carrito()
    carrito.gen_code()

        
    
    
    