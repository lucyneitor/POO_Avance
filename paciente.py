class Paciente:
    def __init__(self, rut:str, nombre:str, edad:int, prevision:str): #constructor
        self.rut = rut
        self.nombre = nombre
        self.edad = edad
        self.prevision = prevision

    @property #obtener
    def rut(self) -> str:
        return self.__rut

    @rut.setter #guardar rut
    def rut(self, rut:str)->None:
        self.__rut = rut

    @property 
    def nombre(self)->str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre:str)->None:
        self.__nombre = nombre

    @property
    def edad(self)->int:
        return self.__edad

    @edad.setter
    def (self, edad:int)->None:
        self.__edad = edad
    
    @property
    def prevision(self)->str:
        return self.___prevision

    @prevision.setter
    def (self, prevision:str)->None:
        self.__prevision = prevision