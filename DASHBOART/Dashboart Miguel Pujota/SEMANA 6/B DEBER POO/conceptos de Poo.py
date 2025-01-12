# Clase base
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Variable de instancia encapsulada
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def saludo(self):
        return "Hola, soy una persona"  # Método que puede ser sobrescrito (Polimorfismo)

# Clase derivada `Estudiante`
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def saludo(self):
        return f"Hola, soy un estudiante de {self.carrera}"  # Sobreescribiendo el método (Polimorfismo)
def presentar_persona(persona):
    return f"{persona.get_nombre()} dice: {persona.saludo()}"
if __name__ == "__main__":
    persona = Persona("Ana", 30)
    estudiante = Estudiante("Carlos", 22, "Informática")

    print(presentar_persona(persona))      # Output: Ana dice: Hola, soy una persona
    print(presentar_persona(estudiante))  # Output: Carlos dice: Hola, soy un estudiante de Informática
