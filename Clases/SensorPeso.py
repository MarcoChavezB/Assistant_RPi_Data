from Metodos.Controlador import Controlador

class SensorPeso(Controlador):
  def __init__(self, date=None, valor=None):
    super().__init__()
    self.date = date
    self.valor = valor
