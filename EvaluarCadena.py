import os
import CrearAFD

def main():
    os.system('cls')
    print('Ingrese nombre del AFD o Gramática: ', end = '')
    nombre = input()
    if nombre in CrearAFD.listaAFD.keys():
        evaluar = CrearAFD.listaAFD.get(nombre)
        while True:
            os.system('cls')
            print('1. Solo validar')
            print('2. Ruta en AFD')
            print('3. Expandir con gramatica')
            print('4. Salir')
            print('')
            entrada = input()
            if entrada == '1':
                os.system('cls')
                print('Ingrese cadena: ',end='')
                cadena = input()
                try:
                    if evaluar.validarCadenaModo1(cadena):
                        print('Cadena valida')
                    else:
                        print('Cadena invalida')
                except:
                    try:
                        if evaluar.validarCadenaModo2(cadena):
                            print('Cadena valida')
                        else:
                            print('Cadena invalida')
                    except:
                        print('Error')
            elif entrada == '2':
                os.system('cls')
                print('Ingrese cadena: ',end='')
                cadena = input()
                try:
                    if evaluar.validarCadenaModo1Ruta(cadena):
                        print('Cadena valida')
                    else:
                        print('Cadena invalida')
                except:
                    try:
                        if evaluar.validarCadenaModo2(cadena):
                            print('Cadena valida')
                        else:
                            print('Cadena invalida')
                    except:
                        print('Error')
            elif entrada == '3':
                os.system('cls')
                print('Ingrese cadena: ',end='')
                cadena = input()
            elif entrada == '4':
                break
            input()
    else:
        print('No existe ese nombre')
        input()
