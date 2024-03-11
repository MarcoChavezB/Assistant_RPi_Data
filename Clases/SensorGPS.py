from Metodos.Controlador import Controlador
class SensorGPS(Controlador):
  def __init__(self, date, valor):
      super().__init__()
      self.date = date
      self.valor = valor


  def __str__(self):
        if not self.informacion:
            return (
                f"\ndate: {self.date}\n"
                f"valor: {self.valor}\n"
            )
        else:
            elementos_str = [str(elemento) for elemento in self.informacion]
            return "\n".join(elementos_str)