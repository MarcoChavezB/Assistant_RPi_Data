from Clases.Controlador import Controlador
from Clases.Carrito import Carrito
from Clases.Data import Data


import platform

controlador = Controlador()
carrito = Carrito()
data = Data()
carrito.gen_code()
data.enviar_sensor()
  