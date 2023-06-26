class Asistencia:
    __fecha = None
    __codigoClase = None
    __asistio = None
    __justificacion = None

    def __init__(self,fecha,codigo,asistio,justificacion):
        self.__fecha = fecha
        self.__codigoClase = codigo
        self.__asistio = asistio
        self.__justificacion = justificacion

    def getFecha(self):
        return self.__fecha
    
    def getCodigoClase(self):
        return self.__codigoClase
    
    def getAsistio(self):
        return self.__asistio
    
    def getJustificacion(self):
        return self.__justificacion
    
    def __str__(self):
        return "Fecha: %s \n Codigo: %s \n Asistió: %s \n Justificacion: %s"%(self.__fecha,self.__codigoClase,self.__asistio,self.__justificacion)
    