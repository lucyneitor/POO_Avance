class Paciente:

    PREVISIONES:set[str] = {"Fonasa","Isapre","Particular"} #tipo de dato llamado conjunto de datos (set)

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
    def edad(self, edad:int)->None:
        self.__edad = edad
    
    @property
    def prevision(self)->str:
        return self.__prevision

    @prevision.setter
    def prevision(self, prevision:str)->None:
        self.__prevision = prevision

    def __repr__(self)->str: #encontrar el objeto enfocado para que el desarrollador lo vea
        return f"Paciente(rut='{self.rut}',nombre='{self.nombre}',edad='{self.edad}',prevision='{self.prevision}')"