from claseAsistencia import Asistencia
class Manejador:
    __lista = []

    def __init__(self):
        self.__lista = []

    def agregarAsistencia(self,asistencia):
        self.__lista.append(asistencia)

    def obtenerInforme(self):
        for i in range(len(self.__lista)):
            print(self.__lista[i])