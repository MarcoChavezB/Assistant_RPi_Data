from Controlador import Controlador
from Carrito import Carrito
from Data import Data


import platform

controlador = Controlador()
carrito = Carrito()
data = Data()
carrito.gen_code()
data.enviar_sensor()
  