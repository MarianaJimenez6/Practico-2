class Curso:
    __identificador = None
    __anio = None
    __division = None

    def __init__(self,identificacion,anio,division):
        self.__identificador = identificacion
        self.__anio = anio
        self.__division = division

    def getId(self):
        return self.__identificador
    
    def getAnio(self):
        return self.__anio
    
    def getDivision(self):
        return self.__division