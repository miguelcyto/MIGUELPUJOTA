# Definir la matriz 3D con datos de ejemplo
# Dimensiones: [ciudades][días de la semana][semanas]
temperaturas = [
    # Ciudad 1
    [
        [20, 22, 21, 19, 23, 24, 25],  # Semana 1
        [21, 23, 22, 20, 24, 25, 26],  # Semana 2
        [22, 24, 23, 21, 25, 26, 27]   # Semana 3
    ],
    # Ciudad 2
    [
        [18, 20, 19, 17, 21, 22, 23],  # Semana 1
        [19, 21, 20, 18, 22, 23, 24],  # Semana 2
        [20, 22, 21, 19, 23, 24, 25]   # Semana 3
    ]
]

# Calcular el promedio de temperaturas para cada ciudad por semana
def calcular_promedios(temperaturas):
    promedios = []
    for ciudad in temperaturas:
        promedios_ciudad = []
        for semana in ciudad:
            suma = sum(semana)
            promedio = suma / len(semana)
            promedios_ciudad.append(promedio)
        promedios.append(promedios_ciudad)
    return promedios

# Mostrar el promedio de temperaturas para cada ciudad y semana
def mostrar_promedios(promedios):
    for i, promedios_ciudad in enumerate(promedios):
        print(f"Ciudad {i + 1}:")
        for j, promedio in enumerate(promedios_ciudad):
            print(f"  Semana {j + 1}: {promedio:.2f}°C")

# Calcular y mostrar los promedios
promedios = calcular_promedios(temperaturas)
mostrar_promedios(promedios)