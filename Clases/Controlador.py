import serial
import json

class Controlador:
  def __init__(self):
    self.data = []
    
  """
  Agrega un dato a la lista de datos
  """
  def addData(self, data):
    self.data.append(data)
  
  
  """
  Muestra la pocision de un dato en la lista
  """
  def getIndex(self, index):
    if 0 <= index < len(self.data):
      return self.data[index]
    else:
      return None
    
  """
  Muestra la lista de datos
  """
  def showData(self):
    for i in self.data:
      print(i)
      
  """
  Modifica un dato de la lista
  """

  def updateData(self, index, instance):
    if 0 <= index < len(self.data):
      self.data[index] = instance
      return True
    else:
      return False
    
    
  """
  Elimina un dato de la lista
  """
  def deleteData(self, index):
    if 0 <= index < len(self.data):
      self.data.pop(index)
      return True
    else:
      return False


  """
  Convierte la lista de datos a un diccionario
  """
  def to_dictionary(self):
    if len(self.data) == 0:
      return []
    else:
      dict_list = []
      
      for elemento in self.data:
        if hasattr(elemento, 'to_dictionary'):
          dict_list.append(elemento.to_dictionary())
        else:
          dict_list.append(vars(elemento))
          
      return dict_list
    
    
    """
    Lee el archivo json
    """
  def read_json(self, file):
    try:
      with open(file, 'r') as file:
        data = json.load(file)
        return data
    except:
      return []

  """
  recibe un objeto para trabajarlo mas comodamente
  self.populate_object(funcion, dataFuncion, ["Nfuncion", "hora_inicio", "pelicula", "fecha_estreno", "hora_fin", "costo_boleto"])
  """  
  def populate_object(self, obj, data, attributes):
    for attribute in attributes:
      setattr(obj, attribute, data.get(attribute, None))


  """
  Guarda los datos a un json conservando los cambios realizados 
  """  
  def save_json(self, archivo="json/test.json", data=None):
      try:
          with open(archivo, "r") as file:
              existing_data = json.load(file)

      except:
          existing_data = []

      existing_data_set = set(json.dumps(item) for item in existing_data)

      for item in data:
          item_json = json.dumps(item)
          if item_json not in existing_data_set:
              existing_data.append(item)
              existing_data_set.add(item_json)
      with open(archivo, "w") as file:
          json.dump(existing_data, file, indent=4, default=lambda x: 
              x.to_dict() if hasattr(x, 'to_dict') else x)

  def read_serial(self):
      ser = serial.Serial("/dev/ttyUSB0", 9600)
      try:
            while True:
                  data = ser.readline().decode().strip()
                  print(data)
      except KeyboardInterrupt:
            ser.close()
            print("Conexion cerrada")
            return data

if __name__ == "__main__":
   c = Controlador()
   c.read_serial()
   