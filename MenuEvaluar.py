import os
import MenuCrearDFA

def main():
    os.system('cls')
    print('Ingrese nombre del AFD o Gramática: ', end = '')
    nombre = input()
    if nombre in MenuCrearDFA.listaAFD.keys():
        evaluar = MenuCrearDFA.listaAFD.get(nombre)
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
                if evaluar.evaluar(cadena):
                    print('Cadena valida')
                else:
                    print('Cadena invalida')
            elif entrada == '2':
                os.system('cls')
                print('Ingrese cadena: ',end='')
                cadena = input()
                print()
                if evaluar.rutaEvaluar(cadena):
                    print()
                    print('Cadena valida')
                else:
                    print('cadena inavalida')
            elif entrada == '3':
                pass
            elif entrada == '4':
                break
            input()
    else:
        print('No existe ese archivo')
        input()