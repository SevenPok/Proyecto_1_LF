import AFD
import os

listaAFD = {}
Le = ['[',']','-',',',';',' ','']
def main():
    os.system('cls')
    print('Ingrese nombre del AFD: ',end='')
    nombreAFD = input()
    automata = AFD.AFD()
    if listaAFD.get(nombreAFD) == None and nombreAFD != '':
        listaAFD[nombreAFD] = automata 
        while True:
            os.system('cls')
            print('1. Ingresar estados')
            print('2. Ingresar alfabeto')
            print('3. Ingresar estado inicial')
            print('4. Ingresar estados de aceptación')
            print('5. Ingrese transicion')
            print('6. Ayuda')
            print('7. Salir')
            print()
            entrada = input()
            if entrada == '1':
                os.system('cls')
                print('Ingrese estado: ',end='')
                estado = input()
                if estado not in Le:
                    if automata.agregarEstado(estado): 
                        print('Se agrego con exito el estado')
                    else:
                        print('Error al ingresar estado')
                else:
                    print('Error al ingresar estado')
            elif entrada == '2':
                os.system('cls')
                print('Ingrese alfabeto: ',end='')
                alfabeto = input()
                if alfabeto not in Le:
                    if automata.agregarAlfabeto(alfabeto):
                        print('Se agrego con exito el alfabeto')
                    else:
                        print('Error al ingresar alfabeto')
                else:
                    print('Error al ingresar alfabeto')
                
            elif entrada == '3':
                os.system('cls')
                print('Ingrese estado inicial: ',end='')
                estado_inicial = input()
                if automata.agregarEstadoInicial(estado_inicial):
                    print('Se agrego correctamente el estado inicial')
                else:
                    print('Error al agregar estado inicial')
            elif entrada == '4':
                os.system('cls')
                print('Ingrese estado de aceptación: ',end='')
                estado_aceptacion = input()
                if automata.agregarEstadosAceptacionn(estado_aceptacion):
                    print('Se agrego correctamente el estado de aceptacion')
                else:
                    print('Error al ingreso estado de aceptacion')
            elif entrada == '5':
                os.system('cls')
                print('1. Modo 1\n2. Modo 2')
                modo = input()
                if modo == '1':
                    os.system('cls')
                    print('Ingrese cadena: ',end='')
                    cadena = input()
                    if automata.modo1(cadena):
                        print('Se agrego correctamente la transición')
                    else:
                        print('Cadena invalida')
                elif modo == '2':
                    os.system('cls')
                    print('Ingrese cadena para la columna: ',end='')
                    colunma = input()
                    print('Ingrese cadena para la fila: ',end='')
                    fila = input()
                    print('Ingrese cadena para el destino: ',end='')
                    destino = input()
                    if automata.modo2(colunma,fila,destino):
                        print('Se agrego correcta la transicion')
                    else:
                        print('Error cadena invalida')
            elif entrada == '6':
                os.system('cls')
                print('Lenguajes Fomrales')
                print('Sección: B+')
                print('Carné: 201800586\n')
                print(automata.toString())
                print('Modo 1: ', ' '.join(automata.getTransicionModo1()))
                print('Modo 2: ', ' '.join(automata.getTransicionModo2()))
            elif entrada == '7':
                    break
            input()
    else:
        print('Error nombre de AFD')
        input()


