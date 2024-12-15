from abc import ABC, abstractmethod

# Clase abstracta Vehículo
class Vehiculo(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    @abstractmethod
    def arrancar(self):
        """Método abstracto que debe ser implementado por las subclases"""
        pass

    @abstractmethod
    def detener(self):
        """Método abstracto que debe ser implementado por las subclases"""
        pass

    def obtener_informacion(self):
        """Método concreto que puede ser usado por todas las subclases"""
        return f"Marca: {self.marca}, Modelo: {self.modelo}"

# Clase concreta Coche
class Coche(Vehiculo):
    def __init__(self, marca, modelo, tipo_combustible):
        super().__init__(marca, modelo)
        self.tipo_combustible = tipo_combustible

    def arrancar(self):
        return "El coche arranca usando el motor de combustión"

    def detener(self):
        return "El coche se detiene presionando el freno"

# Clase concreta Bicicleta
class Bicicleta(Vehiculo):
    def arrancar(self):
        return "La bicicleta se pone en movimiento pedaleando"

    def detener(self):
        return "La bicicleta se detiene frenando con las manos"

# Uso del sistema
def main():
    # Creamos diferentes vehículos
    coche = Coche("Mazda", "Chevrolet", "Gasolina")
    bicicleta = Bicicleta("Trek", "Mountain Bike")

    # Podemos interactuar con los vehículos de manera abstracta
    vehiculos = [coche, bicicleta]

    for vehiculo in vehiculos:
        print(vehiculo.obtener_informacion())
        print(vehiculo.arrancar())
        print(vehiculo.detener())
        print("---")

if __name__ == "__main__":
    main()