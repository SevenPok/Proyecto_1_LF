import os
import MenuCrearDFA
import MenuEvaluar

def main():
    os.system('cls')
    print('Lenguajes Formales')
    print('Sección B+')
    print('carné: 201800586')
    input()
    while True:
        os.system('cls')
        print('1. Crear AFD')
        print('2. Crear gramatica')
        print('3. Evaluar cadena')
        print('4. Reportes')
        print('5. Cargar archivo')
        print('6. Salir')
        print('')
        entrada = input()
        if entrada == '1':
            MenuCrearDFA.main()
        elif entrada == '2':
            pass
        elif entrada == '3':
            MenuEvaluar.main()
        elif entrada == '4':
            pass
        elif entrada == '5':
            pass
        elif entrada == '6':
            break
main()