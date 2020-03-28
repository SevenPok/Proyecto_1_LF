import Metodos

class AFD:
    def __init__(self):
        self.__estados = []
        self.__alfabeto = []
        self.__estado_inicial = ''
        self.__estados_aceptacion = []
        self.__transicionModo1 = []
        self.__transicionModo2 = []

    def agregarEstado(self, estado):
        if estado not in self.__estados and estado not in self.__alfabeto:
            self.__estados.append(estado)
            return True
        else:
            return False
    
    def agregarAlfabeto(self, alfabeto):
        if alfabeto not in self.__estados and alfabeto not in self.__alfabeto:
            self.__alfabeto.append(alfabeto)
            return True
        else:
            return False
    
    def agregarEstadoInicial(self, estado_inicial):
        if estado_inicial in self.__estados:
            self.__estado_inicial = estado_inicial
            return True
        else:
            return False

    def agregarEstadosAceptacionn(self, estado):
        if estado in self.__estados and estado not in self.__estados_aceptacion:
            self.__estados_aceptacion.append(estado)
            return True
        else:
            return False

    def toString(self):
        cadena = 'Estados: ' + ', '.join(self.__estados) + '\nAlfabeto: ' + ', '.join(self.__alfabeto) + '\nEstado inicial: ' + self.__estado_inicial + '\nEstados de aceptacion: ' + ', '.join(self.__estados_aceptacion)
        return cadena
    
    def modo1(self,cadena):
        if cadena not in self.__transicionModo1:
            if Metodos.modo1(cadena,self.__estados,self.__alfabeto):
                self.__transicionModo1.append(cadena)
                return True
            else:
                return False
        else:
            return False

    def modo2(self, columna, fila, destino):
        if Metodos.filaColumna(columna, self.__alfabeto) and Metodos.filaColumna(fila, self.__estados) and Metodos.destino(destino, self.__estados, len(self.__estados), len(self.__alfabeto)):
            cadena = [columna,fila,destino]
            self.__transicionModo2 = cadena
            return True
        else:
            return False

    def getTransicionModo1(self):
        return self.__transicionModo1
    
    def getTransicionModo2(self):
        return self.__transicionModo2

    def validarCadenaModo1(self, cadena):
        matriz = Metodos.crearMatriz(len(self.__estados),len(self.__alfabeto))
        for modo in self.__transicionModo1:
            chain = str(modo).replace(';',',').split(',')
            i = self.__estados.index(chain[0])
            j = self.__alfabeto.index(chain[2])
            k = self.__estados.index(chain[1])
            matriz[i][j] = k

        i = self.__estados.index(self.__estado_inicial)
        if i != None:
            for caracter in cadena:
                if caracter in self.__alfabeto:
                    j = self.__alfabeto.index(caracter)
                    if matriz[i][j] != None:
                        i = matriz[i][j]
                    else:
                        return False
                else:
                    return False
        else:
            return False 
        if self.__estados[i] in self.__estados_aceptacion:
            return True
        else:
            return False
    
    def validarCadenaModo2(self, cadena):
        matriz = Metodos.crearMatriz(len(self.__estados),len(self.__alfabeto))
        fila = self.__transicionModo2[1].replace('[','').replace(']','').split(',')
        columna = self.__transicionModo2[0].replace('[','').replace(']','').split(',')
        destino = self.__transicionModo2[2].replace('[','').replace(']','').split(';')

        for estado in fila:
            i = self.__estados.index(estado)
            for alfabeto in columna:
                j = self.__alfabeto.index(alfabeto)
                caracter = destino[i].split(',')
                if caracter[j] in self.__estados:
                    matriz[i][j] = self.__estados.index(caracter[j])

        i = self.__estados.index(self.__estado_inicial)
        if i != None:
            for caracter in cadena:
                if caracter in self.__alfabeto:
                    j = self.__alfabeto.index(caracter)
                    if matriz[i][j] != None:
                        i = matriz[i][j]
                    else:
                        return False
                else:
                    return False
        else:
            return False 
        if self.__estados[i] in self.__estados_aceptacion:
            return True
        else:
            return False
        

    def validarCadenaModo1Ruta(self, cadena):
        matriz = Metodos.crearMatriz(len(self.__estados),len(self.__alfabeto))
        ruta = ''
        for modo in self.__transicionModo1:
            chain = str(modo).replace(';',',').split(',')
            i = self.__estados.index(chain[0])
            j = self.__alfabeto.index(chain[2])
            k = self.__estados.index(chain[1])
            matriz[i][j] = k

        i = self.__estados.index(self.__estado_inicial)
        if i != None:
            for caracter in cadena:
                if caracter in self.__alfabeto:
                    j = self.__alfabeto.index(caracter)
                    if matriz[i][j] != None:
                        ruta = ruta + self.__estados[i] + ',' + self.__estados[matriz[i][j]] + ',' + self.__alfabeto[j] + '; '
                        i = matriz[i][j]
                        
                    else:
                        return False
                else:
                    return False
        else:
            return False 
        if self.__estados[i] in self.__estados_aceptacion:
            print(ruta)
            return True
        else:
            return False

matriz = []
estado = []
alfabeto = []

while True:
    print('1. Ingresar estado')
    print('2. Ingresar alfabeto')
    print('3. Mostrar matriz')
    print('4. salir')
    print()
    entrada = input()
    if entrada == '1':
        print('ingrese estado: ',end='')
        cadena = input()
        estado.append(cadena)
        if len(matriz) is 0:
            matriz.append([])
        else:
            subLista = []
            for i in matriz[0]:
                subLista.append(None)
            matriz.append(subLista)
        input()
    elif entrada == '2':
        print('ingrese alfabeto: ',end='')
        cadena = input()
        alfabeto.append(cadena)
        if len(matriz) is 0:
            matriz.append([None])
        else:
            for i in matriz:
                i.append(None)
        input()
    elif entrada == '3':
        print(matriz)
        input()
    elif entrada == '4':
        break