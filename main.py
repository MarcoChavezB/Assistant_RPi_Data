from Clases.Controlador import Controlador
from Clases.Carrito import Carrito
import platform

controlador = Controlador()
carrito = Carrito()

carrito.gen_code()

for data in controlador.read_serial():
  print(data[0])
  