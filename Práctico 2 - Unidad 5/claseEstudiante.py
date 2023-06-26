class Estudiante:
    __identificador = None
    __nombre = None
    __apellido = None
    __dni = None
    
    def __init__(self,identificador,nombre,apellido,dni):
        self.__identificador = identificador
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni

    def getId(self):
        return self.__identificador
    
    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getDNI(self):
        return self.__dni