import DFA
import re
import Graphviz

class CrearDFA:
    def __init__(self):
        self.__automata = DFA.DFA()
    
    def setAutomata(self, automata):
        self.__automata = automata
    
    def getAutomata(self):
        return self.__automata

    def addEstado(self, estado):
        if estado not in self.__automata.getEstado() and estado not in self.__automata.getAlfabeto():
            self.__automata.getEstado().append(estado)
            if len(self.__automata.getMatriz()) == 0:
                self.__automata.getMatriz().append([])
            else:
                subLista = []
                for i in self.__automata.getMatriz()[0]:
                    subLista.append(None)
                self.__automata.getMatriz().append(subLista)
            return True
        else:
            return False

    def addAlfabeto(self, alfabeto):
        if alfabeto not in self.__automata.getEstado() and alfabeto not in self.__automata.getAlfabeto():
            self.__automata.getAlfabeto().append(alfabeto)
            if len(self.__automata.getMatriz()) == 0:
                self.__automata.getMatriz().append([None])
            else:
                for i in self.__automata.getMatriz():
                    i.append(None)
            return True
        else:
            return False

    def addEstadoInicial(self, estado):
        if estado in self.__automata.getEstado():
            self.__automata.setEstadoInicial(estado)
            return True
        else:
            return False

    def addEstadoAceptacion(self, estado):
        if estado in self.__automata.getEstado() and estado not in self.__automata.getEstadoAceptacion():
            self.__automata.getEstadoAceptacion().append(estado)
            return True
        else:
            return False

    def modo1(self, cadena):
        estado = 0
        for caracter in cadena:
            if estado == 0:
                if caracter in self.__automata.getEstado():
                    estado = 1
                else:
                    break
            elif estado == 1:
                if caracter == ',':
                    estado = 2
                else:
                    break
            elif estado == 2:
                if caracter in self.__automata.getEstado():
                    estado = 3
                else:
                    break
            elif estado == 3:
                if caracter == ';':
                    estado = 4
                else: 
                    break
            elif estado == 4:
                if caracter in self.__automata.getAlfabeto():
                    estado = 5
                else:
                    break
            else:
                break
        if estado == 5:
            subcadena = str(cadena).replace(';',',').split(',')
            i = self.__automata.getEstado().index(subcadena[0])
            j = self.__automata.getAlfabeto().index(subcadena[2])
            if self.__automata.getMatriz()[i][j] == None:
                self.__automata.getMatriz()[i][j] = subcadena[1]
                return True
            else:
                return False
        else:
            return False
    
    def __columnaFila(self, cadena, lista):
        estado = 0
        cadenaAux = ''
        for c in cadena:
            if estado == 0:
                if c == '[':
                    estado = 1
                else:
                    break
            elif estado == 1:
                if c in lista and c not in cadenaAux:
                    estado = 2
                    cadenaAux = cadenaAux + c
                else:
                    break
            elif estado == 2:
                if c == ',':
                    estado = 1
                elif c == ']':
                    estado = 3
                else:
                    break
            else:
                break
        if estado == 3:
            return True
        else:
            return False

    def __destino(self,cadena,lista,fila,columna):
        estado = 0
        n = fila
        m = columna
        for caracter in cadena:
            if estado == 0:
                if caracter == '[':
                    estado = 1
                else:
                    break
            elif estado == 1:
                if n > 0 and m > 0 and (caracter in lista or caracter == '-'):
                    estado = 2
                    m = m - 1
                else:
                    break
            elif estado == 2:
                if caracter == ',' and n > 0 and m > 0:
                    estado = 1
                elif caracter == ';' and n > 0 and m == 0:
                    estado = 1
                    m = columna
                    n = n - 1
                elif caracter == ']' and n == 1 and m == 0:
                    estado = 3
                else:
                    break
            else:
                break
        if estado == 3:
            return True
        else:
            return False

    def modo2(self,fila,columna,destino):
        if self.__columnaFila(columna,self.__automata.getAlfabeto()):
            columna = str(columna).replace('[','').replace(']','').split(',')
            if self.__columnaFila(fila,self.__automata.getEstado()):
                fila = str(fila).replace('[','').replace(']','').split(',')
                if self.__destino(destino,self.__automata.getEstado(),len(fila),len(columna)):
                    destino = str(destino).replace('[','').replace(']','').split(';')
                    
                    for i in range(0,len(destino)):
                        x = destino[i]
                        aux = x.split(',')
                        for j in range(0,len(aux)):
                            y = aux[j]
                            if y != '-':
                                estado = self.__automata.getEstado().index(fila[i])
                                alfabeto = self.__automata.getAlfabeto().index(columna[j])
                                self.__automata.getMatriz()[estado][alfabeto] = y
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def graficar(self):
        Graphviz.crearGraphviz(self.__automata.getEstado(),self.__automata.getEstadoInicial(),self.__automata.getAlfabeto(),self.__automata.getEstadoAceptacion(),self.__automata.getMatriz())


    def mostrar(self):
        print('Estados: ',', '.join(self.__automata.getEstado()))
        print('Alfabeto: ',', '.join(self.__automata.getAlfabeto()))
        if self.__automata.getEstadoInicial() == None:
            print('Estado inicial: ')
        else:
            print('Estado inicial: ', self.__automata.getEstadoInicial())
        print('Estados de aceptación: ', ', '.join(self.__automata.getEstadoAceptacion()))
        print('')
        if self.__automata.getMatriz() == 0:
            print('Tabla de tranción: None')
        else:
            print('Tabla de tranción')
            print()
            print('',end='    ')
            for i in self.__automata.getAlfabeto():
                print(i,end=' ')
            print()
            for i in range(0,len(self.__automata.getMatriz())):
                print(self.__automata.getEstado()[i],end=' | ')
                for j in range(0,len(self.__automata.getMatriz()[i])):
                    if self.__automata.getMatriz()[i][j] == None:
                        print('-',end=' ')
                    else:
                        print(self.__automata.getMatriz()[i][j],end=' ')
                print('|')
                



