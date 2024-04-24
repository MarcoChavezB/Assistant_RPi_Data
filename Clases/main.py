from Controlador import Controlador
from Carrito import Carrito
from Data import Data


controlador = Controlador()
carrito = Carrito()
data = Data()

carrito.gen_code()
data.enviar_sensor()
    
    