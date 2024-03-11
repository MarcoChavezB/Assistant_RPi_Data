from Metodos.Controlador import Controlador

class SensorVelocidad(Controlador):
  def __init__(self, id, date, valor):
    super().__init__()
    self.id = id
    self.date = date
    self.valor = valor

    def __str__(self):
        return f"SensorVelocidad_data: {self.id} {self.date} {self.valor}"
