# Clase base o padre
class Empleado:
    def __init__(self, nombre, edad, salario_base):
        self.nombre = nombre
        self.edad = edad
        self.salario_base = salario_base

    def calcular_salario(self):
        """Método base para calcular salario"""
        return self.salario_base

    def mostrar_informacion(self):
        """Método para mostrar información básica del empleado"""
        return (f"Nombre: {self.nombre}, "
                f"Edad: {self.edad}, "
                f"Salario: ${self.calcular_salario()}")

# Clase derivada: Desarrollador (hereda de Empleado)
class Desarrollador(Empleado):
    def __init__(self, nombre, edad, salario_base, lenguaje_programacion):
        # Llamar al constructor de la clase padre
        super().__init__(nombre, edad, salario_base)
        self.lenguaje_programacion = lenguaje_programacion

    def calcular_salario(self):
        """Sobreescribir el método de cálculo de salario"""
        # Añadir un bono por conocimiento de lenguaje
        bono_lenguaje = {
            "Python": 500,
            "Java": 450,
            "JavaScript": 400,
            "C++": 600
        }
        return self.salario_base + bono_lenguaje.get(self.lenguaje_programacion, 0)

    def mostrar_informacion(self):
        """Extender el método de mostrar información"""
        info_base = super().mostrar_informacion()
        return f"{info_base}, Lenguaje: {self.lenguaje_programacion}"

# Clase derivada: Gerente (hereda de Empleado)
class Gerente(Empleado):
    def __init__(self, nombre, edad, salario_base, departamento, bono_anual):
        # Llamar al constructor de la clase padre
        super().__init__(nombre, edad, salario_base)
        self.departamento = departamento
        self.bono_anual = bono_anual

    def calcular_salario(self):
        """Sobreescribir el método de cálculo de salario"""
        return self.salario_base + self.bono_anual

    def mostrar_informacion(self):
        """Extender el método de mostrar información"""
        info_base = super().mostrar_informacion()
        return f"{info_base}, Departamento: {self.departamento}"

# Clase derivada: Diseñador (hereda de Empleado)
class Diseñador(Empleado):
    def __init__(self, nombre, edad, salario_base, herramienta_principal):
        # Llamar al constructor de la clase padre
        super().__init__(nombre, edad, salario_base)
        self.herramienta_principal = herramienta_principal

    def calcular_salario(self):
        """Sobreescribir el método de cálculo de salario"""
        # Añadir un bono por herramienta especializada
        bono_herramienta = {
            "Adobe Photoshop": 300,
            "Figma": 350,
            "Sketch": 325,
            "Adobe XD": 300
        }
        return self.salario_base + bono_herramienta.get(self.herramienta_principal, 0)

    def mostrar_informacion(self):
        """Extender el método de mostrar información"""
        info_base = super().mostrar_informacion()
        return f"{info_base}, Herramienta: {self.herramienta_principal}"

# Función para demostrar el uso de herencia
def main():
    # Crear instancias de diferentes tipos de empleados
    desarrollador = Desarrollador("Ana García", 28, 3000, "Python")
    gerente = Gerente("Carlos Rodríguez", 45, 5000, "Tecnología", 2000)
    diseñador = Diseñador("Laura Martínez", 32, 3500, "Figma")

    # Lista de empleados
    empleados = [desarrollador, gerente, diseñador]

    # Mostrar información de cada empleado
    print("=== Información de Empleados ===")
    for empleado in empleados:
        print(empleado.mostrar_informacion())
        print(f"Salario Total: ${empleado.calcular_salario()}\n")

# Ejecutar el programa
if __name__ == "__main__":
    main()