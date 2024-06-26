import serial
import platform

class Controlador:
   def __init__(self):
    self.data = []
    
   def add (self, data):
      self.data.append(data)
      
   def read_serial(self, port="", baud=19200):
        port = "/dev/ttyUSB0"
        with serial.Serial(port, baud) as ser:
            try:
                while True:
                    data = ser.readline().decode().strip()
                    yield self.format_data_serial(data)
            except KeyboardInterrupt:
                pass
            
   def find_port(self):
      os = platform.system()
      initPort = "/dev/ttyUSB"
      
      if(os == "Windows"):
         initPort = "COM"
      
      for number in range(5):
         try:
            with serial.Serial(initPort + str(number), 9600) as ser:
               return initPort + str(number)
         except:
            pass
         

   def format_data_serial(self, data):
      return data.split("|")
   
# if __name__ == "__main__":
#     controlador = Controlador()
#     for data in controlador.read_serial():
#         controlador.add(data)
#         print(data)