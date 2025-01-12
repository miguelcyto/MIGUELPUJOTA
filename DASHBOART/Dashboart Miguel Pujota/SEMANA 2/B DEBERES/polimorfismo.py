from abc import ABC, abstractmethod
import math

# Clase abstracta base para figuras geométricas
class FiguraGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        """Método abstracto para calcular el área"""
        pass

    @abstractmethod
    def calcular_perimetro(self):
        """Método abstracto para calcular el perímetro"""
        pass

    def describir(self):
        """Método concreto que puede ser utilizado por todas las figuras"""
        return f"Área: {self.calcular_area():.2f}, Perímetro: {self.calcular_perimetro():.2f}"

# Implementaciones concretas de figuras
class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        """Cálculo de área específico para círculo"""
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        """Cálculo de perímetro específico para círculo"""
        return 2 * math.pi * self.radio

    def describir(self):
        """Descripción personalizada para círculo"""
        return f"Círculo - Radio: {self.radio}, " + super().describir()

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        """Cálculo de área específico para rectángulo"""
        return self.base * self.altura

    def calcular_perimetro(self):
        """Cálculo de perímetro específico para rectángulo"""
        return 2 * (self.base + self.altura)

    def describir(self):
        """Descripción personalizada para rectángulo"""
        return f"Rectángulo - Base: {self.base}, Altura: {self.altura}, " + super().describir()

class Triangulo(FiguraGeometrica):
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_area(self):
        """Cálculo de área usando fórmula de Herón"""
        # Semiperímetro
        s = self.calcular_perimetro() / 2
        # Fórmula de Herón
        return math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))

    def calcular_perimetro(self):
        """Cálculo de perímetro para triángulo"""
        return self.lado1 + self.lado2 + self.lado3

    def describir(self):
        """Descripción personalizada para triángulo"""
        return f"Triángulo - Lados: {self.lado1}, {self.lado2}, {self.lado3}, " + super().describir()

# Función que demuestra el polimorfismo
def analizar_figura(figura):
    """
    Esta función muestra polimorfismo al trabajar con cualquier figura
    que herede de FiguraGeometrica
    """
    print(figura.describir())

# Función principal para demostrar el uso
def main():
    # Crear diferentes figuras
    figuras = [
        Circulo(5),
        Rectangulo(4, 6),
        Triangulo(3, 4, 5)
    ]

    print("=== Análisis de Figuras ===")
    # Demostración de polimorfismo
    for figura in figuras:
        analizar_figura(figura)
        print()  # Línea en blanco para separar

# Ejecutar el programa
if __name__ == "__main__":
    main()