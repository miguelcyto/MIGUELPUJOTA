# Definimos la matriz como indica en la tarea de tres cuidades y cuatro semana.
# Definimos Dimensiones: [ciudades][días de la semana][semanas]
temperatura = [
    # Quito
    [
        [20, 18, 21, 19, 23, 24, 25],  # Semana 1
        [21, 23, 22, 18, 24, 25, 26],  # Semana 2
        [22, 24, 23, 21, 23, 26, 27],  # Semana 3
        [18, 26, 23, 21, 16, 26, 27]   # Semana 4
    ],
    # Guayaquil
    [
        [18, 20, 19, 17, 24, 22, 23],  # Semana 1
        [19, 21, 18, 18, 22, 23, 24],  # Semana 2
        [20, 22, 21, 19, 23, 23, 25],  # Semana 3
        [23, 22, 21, 19, 18, 23, 25]   # Semana 4
    ],
    # Cuenca
    [
        [18, 20, 19, 17, 24, 22, 23],  # Semana 1
        [19, 21, 18, 18, 22, 23, 24],  # Semana 2
        [20, 22, 21, 19, 23, 23, 25],  # Semana 3
        [23, 22, 21, 19, 18, 23, 25]   # Semana 4
    ]
]

# mediante la fuincion def vamos a calcular el promedio de temperaturas para cada ciudad por semana
def calcular_promedios(temperatura):
    promedios = []
    for Quito in temperatura:
        promedios_ciudad = []
        for semana in Quito:
            suma = sum(semana)
            promedio = suma / len(semana)
            promedios_ciudad.append(promedio)
        promedios.append(promedios_ciudad)
    return promedios

# Mostrar el promedio de temperaturas para cada ciudad y semana
def mostrar_promedios(promedios):
    for i, promedios_ciudad in enumerate(promedios):
        print(f"Quito {i + 1}:")
        for j, promedio in enumerate(promedios_ciudad):
            print(f"  Semana {j + 1}: {promedio:.2f}°C")

# Una ves calculados los promedios desplegamos en pantalla
promedio = calcular_promedios(temperatura)
print(f"  Semana ")
mostrar_promedios(promedio)