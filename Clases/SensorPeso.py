from Metodos.Controlador import Controlador

class SensorPeso(Controlador):
  def __init__(self, date=None, valor=None):
    super().__init__()
    self.id = id
    self.date = date
    self.valor = valor

    def __str__(self):
        return f"SensorPeso_data: {self.id} {self.date} {self.valor}"
