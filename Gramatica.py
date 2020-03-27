
class Gramatica:

    def __init__(self):
        self.__NoTerminals = []
        self.__Terminales = []
        self.__NoTerminalInicial = ''
        self.__Producciones = {}


    def agregarNoTerminal(self, NT):
        if NT not in self.__NoTerminals and NT not in self.__Terminales:
            self.__NoTerminals.append(NT)
            return True
        else:
            return False

    
    def agregarTerminal(self, T):
        if T not in self.__NoTerminals and T not in self.__Terminales:
            self.__NoTerminals.append(T)
            return True
        else:
            return False

    def agregarNoTerminalInicial(self, NTI):
        if NTI in self.__NoTerminals:
            self.__NoTerminalInicial = NTI
            return True
        else:
            return False

    def getPosicionNoTerminal(self, caracter):
        if caracter in self.__NoTerminals:
            return self.__NoTerminals.index(caracter)
        else:
            return -1

    def getPosicionTerminal(self, caracter):
        if caracter in self.__Terminales:
            return self.__Terminales.index(caracter)
        else:
            return -1

    def produccion(self, cadena):
        estado = 0
        lista = []
        lexema = ''
        for caracter in cadena:
            if estado == 0:
                if caracter in self.__NoTerminals and caracter not in self.__Producciones.keys():
                    estado = 1
                else:
                    return False
            elif estado == 1:
                if caracter == '>':
                    estado = 2
                else:
                    return False
            elif estado == 2:
                if caracter in self.__NoTerminals:
                    estado = 3
                    lexema += caracter
                elif caracter in  self.__Terminales:
                    estado = 3
                    lexema += caracter
                else:
                    return False
            elif estado == 3:
                if caracter in self.__NoTerminals:
                    lexema += caracter
                    estado = 3
                elif caracter in  self.__Terminales and lexema not in lista:
                    lexema += caracter
                    estado = 3
                elif caracter == ' ':
                    estado = 4 
                else:
                    return False
            elif estado == 4:
                if caracter == '|' and lexema not in lista:
                    estado = 5
                    lista.append(lexema)
                    lexema = ''
                else:
                    return False
            elif estado == 5:
                if caracter == ' ':
                    estado = 6
                else:
                    return False
            elif estado == 6:
                if caracter in self.__NoTerminalInicial:
                    estado = 3
                    lexema += caracter
                elif caracter in self.__NoTerminals:
                    estado = 3
                    lexema += caracter
                else:
                    return False
            else:
                return False
        if estado == 3 and lexema not in lista:
            cadena = cadena.replace(' ','').split('>')
            subLista = []
            for i in cadena[1].split('|'):
                subLista.append(i)

            self.__Producciones[cadena[0]] = subLista

            return True
        else:
            return False

    def reconocerEpsilon(self, cadena):
        estado = 0
        for caracter in cadena:
            if estado == 0:
                if caracter == 'e':
                    estado = 1
                else:
                    return False
            elif estado == 1:
                if caracter == 'p':
                    estado = 2
                else:
                    return False
            elif estado == 2:
                if caracter == 's':
                    estado = 3
                else:
                    return False
            elif estado  == 3:
                if caracter == 'i':
                    estado = 4
                else:
                    return False
            elif estado == 4:
                if caracter == 'l':
                    estado = 5
                else:
                    return False
            elif estado == 5:
                if caracter == 'o':
                    estado = 6
                else:
                    return False
            elif estado == 6:
                if caracter == 'n':
                    estado = 7
                else:
                    return False
            else:
                return False
        if estado == 7:
            return True
        else:
            return False

a = Gramatica()
a.agregarNoTerminal('A')
a.agregarNoTerminal('B')
a.agregarNoTerminal('C')
a.agregarTerminal('a')
a.agregarTerminal('b')
a.agregarTerminal('c')
print(a.produccion('A>aAB | acbAB | acAB'))
print(a.produccion('A>aAB | acbAB | acAB'))


