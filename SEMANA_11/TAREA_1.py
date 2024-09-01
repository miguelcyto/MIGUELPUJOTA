
#Escribe un programa que incluya una matriz bidimensional (puede ser una matriz pequeña de 3x3) con valores numéricos.
#Implementa una función que realice una búsqueda en la matriz para encontrar un valor específico que definas.
#Muestra un mensaje que indique si el valor se encontró o no, y muestra su posición en la matriz si se encontró.
#Crear una matriz bidimensional (3x3)
matriz = [
    [3,5,7],
    [7,12,8],
    [11,34,6]
]
#busqueda de un valor especifico em la matriz.
buscado = 3
#Verificar si el valor se encuentra en la matriz.
#para su verificacion vamos a usar IF en donde busque fila por fila el numero ingresado hasta encontrarlo y desplegarara el mensaje
if any(buscado in fila for fila in matriz):
    print(f"El valor {buscado} se encuentra en la matriz")
    #Buscar la posicion del valor en la matriz
    for fila_num, fila in enumerate(matriz):
        if buscado in fila:
            columna_num = fila.index(buscado)
            print(f"El valor {buscado} se encuentra en la fila {fila_num+1}, columna {columna_num+1}")
else:
    print(f"El valor {buscado} no se encuentra en la matriz")





