class Persona:
    def __init__(self, nombre, edad):
        # Constructor: inicializa el nombre y la edad de la persona.
        self.nombre = nombre
        self.edad = edad
        print(f"Se ha creado una Persona: {self.nombre}, {self.edad} años.")

    def __del__(self):
        # Destructor: muestra un mensaje cuando el objeto es destruido.
        print(f"Se ha eliminado la Persona: {self.nombre}.")


# Demostración del uso de constructores y destructores.

# Uso de la clase Persona
persona1 = Persona("Miguel", 30)
persona2 = Persona("Andres", 25)

# Eliminar los objetos para llamar al destructor explícitamente
del persona1
del persona2
