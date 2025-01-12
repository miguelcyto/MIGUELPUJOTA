# Programa para calcular el área de un círculo
# Funcionalidad: Este programa solicita al usuario el radio de un círculo y calcula su área.
# Tipos de Datos utilizados: float (para el radio y el área), string (para los mensajes), boolean (para la validación simple)

import math

def calcular_area_circulo(radio):
    """
    Función para calcular el área de un círculo dado su radio.
    :param radio: float
    :return: float
    """
    area = math.pi * (radio ** 2)
    return area

def es_radio_valido(radio):
    """
    Función para validar si el radio es un valor positivo.
    :param radio: float
    :return: bool
    """
    return radio > 0

def main():
    print("Calculadora de Área de un Círculo")

    # Solicitar al usuario el radio del círculo
    radio = float(input("Por favor, introduce el radio del círculo: "))

    # Validar que el radio es positivo
    if es_radio_valido(radio):
        # Calcular el área del círculo
        area = calcular_area_circulo(radio)
        print(f"El área del círculo con radio {radio} es: {area}")
    else:
        print("Por favor, introduce un radio positivo.")

if __name__ == "__main__":
    main()


