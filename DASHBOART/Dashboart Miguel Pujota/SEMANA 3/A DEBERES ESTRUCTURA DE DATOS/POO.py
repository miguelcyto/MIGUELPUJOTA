# Esta clase gestiona las temperaturas diarias. Tiene un atributo temperaturas
# que es una lista para almacenar las temperaturas.
class Temperatura:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperaturas(self):
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
            self.temperaturas.append(temp)
# El método calcular_promedio calcula el promedio de las temperaturas almacenadas.
    def calcular_promedio(self):
        suma = sum(self.temperaturas)
        promedio = suma / len(self.temperaturas)
        return promedio
# Esta clase organiza la lógica del programa.
#  llama a ingresar_temperaturas para recoger las temperaturas y luego a calcular_promedio
# para obtener y mostrar el promedio semanal.
class ProgramaTemperatura:
    def __init__(self):
        self.temperatura = Temperatura()
    def ejecutar(self):
        print("Programa para calcular el promedio semanal de temperaturas")
        self.temperatura.ingresar_temperaturas()
        promedio = self.temperatura.calcular_promedio()
        print(f"El promedio semanal de temperaturas es: {promedio:.2f}")

# Crear una instancia de ProgramaTemperatura y ejecutar el programa
programa = ProgramaTemperatura()
programa.ejecutar()
