from Metodos.Controlador import Controlador
class SensorGPS(Controlador):
  def __init__(self, id, date, latitud, longitud):
      super().__init__()
      self.id = id
      self.date = date
      self.latitud = latitud
      self.longitud = longitud

      def __str__(self):
            return f"SensorGPS_data: {self.id} {self.date} {self.latitud} {self.longitud}"

