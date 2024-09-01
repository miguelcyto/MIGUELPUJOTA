#Escribe un programa que incluya una matriz bidimensional con valores numéricos (puede ser una matriz pequeña de 3x3).
#Implementa una función que ordene una fila específica de la matriz en orden ascendente utilizando un algoritmo de ordenación de tu elección
#Crear una matriz bidimensional (3x3)
matriz = [
    [57, 12, 19],
    [53, 97, 71],
    [86, 54, 76]
]

# Función para ordenar una fila de manera ascendente utilizando Bubble Sort
def bubble_sort_fila(fila):
    n = len(fila)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]  # Intercambiar elementos
# Función para mostrar la matriz
def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

# Mostrar la matriz original
print("Matriz sin Organizar:")
mostrar_matriz(matriz)

# Ordenar cada fila de la matriz utilizando Bubble Sort
for fila in matriz:
    bubble_sort_fila(fila)

# Mostrar la matriz ordenada
print("Matriz Organizada:")
mostrar_matriz(matriz)


