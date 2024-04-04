from Clases.Controlador import Controlador
import platform

controlador = Controlador() 
for data in controlador.read_serial():
  print(data)