from graphviz import Digraph


def crearGraphviz(estados, estadoInicial, alfabeto, estado_aceptacion, matriz):

    f = Digraph(format='png', name='salida')
    f.attr(rankdir='LR', size='8,5')

    f.attr('node', shape='circle')
    for i in estados:
        if i not in estado_aceptacion:
            f.node(i)
    
    f.attr('node', shape='doublecircle')
    for i in estado_aceptacion:
        f.node(i)

    for i in range (0,len(matriz)):
        for j in range(0,len(matriz[i])):
            if matriz[i][j] != None:
                f.edge(estados[i], matriz[i][j], label=alfabeto[j])

    f.attr('node', shape='none')
    f.attr('edge', arrowhead='empty', arrowsize='1.5')
    f.edge('', estadoInicial, None)
    f.render()


