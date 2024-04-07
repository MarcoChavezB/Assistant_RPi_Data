import json
import random
import string
import platform
import requests
from tokenService import tokenService

class Carrito():
    def __init__(self,nombre=None ,clave=None, type=None, model=None):
        super().__init__()
        self.isConected= nombre = nombre and clave==None and type==None and model==None
        if self.isConected:
            self.arreglo=[]
        self.nombre=nombre
        self.clave=clave
        self.type = "Car"
        self.model = "Assistant"
        self.codeserv = tokenService()

    def gen_code(self):
        with open('Clases/json/UniqueCode.json') as json_file:
            data = json.load(json_file)
            deviceCode = data['deviceCode']

        while True:
            if deviceCode is None or deviceCode == "":
                chars = string.ascii_letters + string.digits
                code = ''.join(random.choice(chars) for _ in range(10))     
                response = self.api_request_device(code,self.type ,self.model)
                if response is not None:
                    data['deviceCode'] = code
                    with open('Clases/json/UniqueCode.json', 'w') as json_file:
                        json.dump(data, json_file)
                    break
            else:
                print("Car already exists")
                break

    def device_code(self):
        with open('Clases/json/UniqueCode.json') as json_file:
            data = json.load(json_file)
            self.clave = data['deviceCode']
            return data['deviceCode']


    def api_request_device(self, code, type,model):

        api_url = "http://backend.mylittleasistant.online:8000/api/device/store"

        body = {
            "code": code,
            "type": type,
            "model": model,
            "os": platform.system(),
        }
    
        try:
            response = requests.post(api_url, headers=self.codeserv.get_headers(), json=body)
            response.raise_for_status()
            print(response.json())
            return response.json()
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occurred: {err}")
            print(f"Response status: {response.status_code}")
            print(f"Response text: {response.text}")


if __name__ == "__main__":
    carrito = Carrito()
    carrito.gen_code()
    print(carrito.device_code())
    print(carrito.nombre)
    print(carrito.type)
    print(carrito.model)
    

        
    
    
    