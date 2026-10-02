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
        if not isinstance(rut, str) or not rut.strip():
            raise ValueError("El RUT no puede estar vacío")
        self.__rut = rut.strip().upper()

    @property 
    def nombre(self)->str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre:str)->None:
        if not isinstance(nombre, str) or len(nombre.strip())<2:
            raise ValueError("El nombre debe tener al menos 2 caracteres.")
        self.__nombre = nombre

    @property
    def edad(self)->int:
        return self.__edad

    @edad.setter
    def edad(self, edad:int)->None:
        if not isinstance(edad, int): #isinstance: funcion integrada para verificaer si objeto pertenece al tipo de dato o clase
            raise ValueError("La edad debe ser un número entero")
        elif edad<0 or edad>125:
            raise ValueError("La edad debe ser un valor biológicamente válido (entre 0 y 125)")
        self.__edad = edad
    
    @property
    def prevision(self)->str:
        return self.__prevision

    @prevision.setter
    def prevision(self, prevision:str)->None:
        if not isinstance(prevision, str):
            raise
        elif prevision.strip().capitalize() not in self.PREVISIONES:
            opciones = ", ".join(self.PREVISIONES) #muestra las opciones validas
            raise ValueError(f"Previsión '{prevision}' no valida. Opciones permitidas: {opciones}.")
        self.__prevision = prevision

    def __repr__(self)->str: #encontrar el objeto enfocado para que el desarrollador lo vea
        return f"Paciente(rut='{self.rut}',nombre='{self.nombre}',edad='{self.edad}',prevision='{self.prevision}')"