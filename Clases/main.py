from Controlador import Controlador
from Carrito import Carrito
from Data import Data
from Datagps import Datagps


controlador = Controlador()
carrito = Carrito()
data = Data()
gps = Datagps()
carrito.gen_code()
while True:
    
    
    data.enviar_sensor()
    gps.readgps()
    