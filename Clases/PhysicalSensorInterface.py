from Clases.PhysicalSensorInfo import PhysicalSensorInfo
class PhysicalSensorInterface():
    def __init__(self, ISF =None ):
        if ISF is None:
                self.ISFisico = ISF()
                self.isConected = True 
                self.ISFisico.cargar_desde_archivo("InfoSensorFisico.json")
        self.ISFisico = ISF()
        self.isConected = False
        