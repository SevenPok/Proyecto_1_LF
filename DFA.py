class DFA:
    def __init__(self):
        self.__estado = []
        self.__alfabeto = []
        self.__eInicial = None
        self.__eAceptacion = []
        self.__matriz = []

    def setEstado(self, estado):
        self.__estado = estado
    
    def getEstado(self):
        return self.__estado

    def setAlfabeto(self, alfabeto):
        self.__alfabeto = alfabeto
    
    def getAlfabeto(self):
        return self.__alfabeto

    def setEstadoInicial(self, estadoI):
        self.__eInicial = estadoI
    
    def getEstadoInicial(self):
        return self.__eInicial

    def setEstadoAceptacion(self, estadoA):
        self.__eAceptacion = estadoA
    
    def getEstadoAceptacion(self):
        return self.__eAceptacion
    
    def setMatriz(self, matriz):
        self.__matriz = matriz
    
    def getMatriz(self):
        return self.__matriz

    