import os
import CrearDFA

listaAFD = {}
Le = ['[',']','-',',',';',' ','']

def main():
    os.system('cls')
    print('Ingrese nombre del AFD: ',end='')
    nombreAFD = input()
    AFD = CrearDFA.CrearDFA()
    if listaAFD.get(nombreAFD) == None and nombreAFD != '':
        listaAFD[nombreAFD] = AFD 
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
                if estado not in Le and AFD.addEstado(estado):
                    print('Se agrego correctamente')
                else:
                    print('Error al ingresar estado')
            elif entrada == '2':
                os.system('cls')
                print('Ingrese alfabeto: ',end='')
                alfabeto = input()
                if alfabeto not in Le and AFD.addAlfabeto(alfabeto):
                    print('Se agrego correctamente')
                else:
                    print('Error al ingresar estado')
            elif entrada == '3':
                os.system('cls')
                print('Ingrese estado inicial: ',end='')
                estado_inicial = input()
                if AFD.addEstadoInicial(estado_inicial):
                    print('Se agrego correctamente')
                else:
                    print('Error al ingresar estado')
            elif entrada == '4':
                os.system('cls')
                print('Ingrese estado de aceptación: ',end='')
                estado_aceptacion = input()
                if AFD.addEstadoAceptacion(estado_aceptacion):
                    print('Se agrego correctamente')
                else:
                    print('Error al ingresar estado')
            elif entrada == '5':
                os.system('cls')
                print('1. Modo 1\n2. Modo 2')
                modo = input()
                if modo == '1':
                    os.system('cls')
                    print('Ingrese cadena: ',end='')
                    cadena = input()
                    if AFD.modo1(cadena):
                        print('Se agrego correctamente la transicion')
                    else:
                        print('Cadena invalida')
                elif modo == '2':
                    os.system('cls')
                    print('Ingrese cadena para la columna: ',end='')
                    columna = input()
                    print('Ingrese cadena para la fila: ',end='')
                    fila = input()
                    print('Ingrese cadena para el destino: ',end='')
                    destino = input()
                    if AFD.modo2(fila,columna,destino):
                        print('Se agrego correctamente')
                    else:
                        print('Cadena invalida')
            elif entrada == '6':
                os.system('cls')
                print('Lenguajes Fomrales')
                print('Sección: B+')
                print('Carné: 201800586\n')
                AFD.mostrar()
            
            elif entrada == '7':
                    break
            input()
    else:
        print('Error nombre de AFD')
        input()