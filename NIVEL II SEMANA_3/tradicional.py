# Esta función solicita al usuario ingresar las temperaturas de cada uno de los 7 días de la semana.
def ingresar_temperaturas():
    temperaturas = []
# Utiliza un bucle for para recoger la temperatura de cada día y las almacena en una lista
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal de temperaturas
# Calcula la suma de todas las temperaturas y luego divide por el número de días (7) para obtener el promedio.
def calcular_promedio(temperaturas):
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio

# Función principal que organiza la lógica del programa
# Esta función organiza la lógica principal del programa.
def main():
    print("Programa para calcular el promedio semanal de temperaturas")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
# Finalmente, imprime el promedio semanal de temperaturas
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}")

# Llamada a la función principal para ejecutar el programa
main()
