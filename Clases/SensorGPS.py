from Metodos.Controlador import Controlador

class SensorGPS(Controlador):
<<<<<<< HEAD
  def __init__(self, date=None, valor=None):
=======
  def __init__(self, id, date, latitud, longitud):
>>>>>>> 8e7732f7ca3c843e0f6f7062c3a657448a45c2df
      super().__init__()
      self.id = id
      self.date = date
      self.latitud = latitud
      self.longitud = longitud

      def __str__(self):
            return f"SensorGPS_data: {self.id} {self.date} {self.latitud} {self.longitud}"

