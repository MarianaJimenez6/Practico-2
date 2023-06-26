class Preceptor:
    __id = None
    __nombre = None
    __apellido = None
    __correo = None
    __clave = None

    def __init__(self,identificador,nombre,apellido,correo,clave):
        self.__id = identificador
        self.__nombre = nombre
        self.__apellido = apellido
        self.__correo = correo
        self.__clave = clave

    def getId(self):
        return self.__id
    
    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getCorreo(self):
        return self.__correo
    
    def getClave(self):
        return self.__clave
