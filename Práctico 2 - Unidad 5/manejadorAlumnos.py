from claseAsistencia import Asistencia
class Manejador:
    __lista = []

    def __init__(self):
        self.__lista = []

    def ordenar(self):
        self.__lista.sort()
        return self.__lista