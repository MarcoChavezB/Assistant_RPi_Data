from Metodos.Controlador import Controlador

class SensorInclincacion(Controlador):
<<<<<<< HEAD
  def __init__(self, date=None, valor=None):
=======
  def __init__(self, id, date, valor):
>>>>>>> 8e7732f7ca3c843e0f6f7062c3a657448a45c2df
    super().__init__()
    self.id = id
    self.date = date
    self.valor = valor

    def __str__(self):
        return f"SensorInclinacion_data: {self.id} {self.date} {self.valor}"
  