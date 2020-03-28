import os
from reportlab.pdfgen import canvas

def crearMatriz(f,c):
    lista = []
    for i in range(0,f):
        lista2 = []
        lista.append(lista2)
        for j in range(0,c):
            lista2.append(None)
    return lista

def modo1(cadena,lista_estado,lista_alfabeto):
    estado = 0
    for c in cadena:
        if estado == 0:
            if c in lista_estado:
                estado = 1
            else:
                break
        elif estado == 1:
            if c == ',':
                estado = 2
            else:
                break
        elif estado == 2:
            if c in lista_estado:
                estado = 3
            else:
                break
        elif estado == 3:
            if c == ';':
                estado = 4
            else:
                break
        elif estado == 4:
            if c in lista_alfabeto:
                estado = 5
            else:
                break
        else:
            break

    if estado == 5:
        return True
    else:
        return False

def filaColumna(cadena,lista):
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

def destino(cadena,lista,fila,columna):
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

def gramatica(cadena,NT,T):
    estado = 0
    for caracter in cadena:
        if estado == 0:
            if caracter in NT:
                estado = 1
            else:
                return False
        elif estado == 1:
            if caracter == '>':
                estado = 2
            else:
                return False
        elif estado == 2:
            if caracter in NT or caracter in T:
                estado = 3
            elif caracter == ' ':
                estado = 4
            else:
                return False
        elif estado == 3:
            if caracter in NT or caracter in T:
                estado = 3
            elif caracter == '|':
                estado = 5
            else:
                return False
        elif estado == 5:
            if caracter in NT or caracter in T:
                estado = 3
            elif caracter == ' ':
                estado = 4
            else:
                return False
        else:
            return False

    if estado == 3 or estado == 4:
        return True
    else:
        return False 

