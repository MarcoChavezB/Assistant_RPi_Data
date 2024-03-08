from Metodos.Controlador import Controlador

class SensorLuz(Controlador):
  def __init__(self, date, valor):
    super().__init__()
    self.date = date
    self.valor = valor    
      
