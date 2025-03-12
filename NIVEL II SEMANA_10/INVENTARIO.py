import os
class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.nombre},{self.cantidad},{self.precio}"

class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga los productos desde el archivo de inventario."""
        if not os.path.exists(self.archivo):
            # Si el archivo no existe, lo creamos
            with open(self.archivo, 'w') as f:
                pass
            print("Archivo de inventario creado.")
            return

        try:
            with open(self.archivo, 'r') as f:
                for linea in f:
                    nombre, cantidad, precio = linea.strip().split(',')
                    self.productos[nombre] = Producto(nombre, int(cantidad), float(precio))
            print("Inventario cargado exitosamente.")
        except FileNotFoundError:
            print("Error: El archivo de inventario no se encontró.")
        except PermissionError:
            print("Error: No se tienen permisos para acceder al archivo de inventario.")
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")

    def guardar_inventario(self):
        """Guarda los productos en el archivo de inventario."""
        try:
            with open(self.archivo, 'w') as f:
                for producto in self.productos.values():
                    f.write(str(producto) + '\n')
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print("Error: No se tienen permisos para escribir en el archivo de inventario.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def añadir_producto(self, nombre, cantidad, precio):
        """Añade un nuevo producto al inventario."""
        if nombre in self.productos:
            print("Error: El producto ya existe en el inventario.")
            return
        self.productos[nombre] = Producto(nombre, cantidad, precio)
        self.guardar_inventario()
        print(f"Producto '{nombre}' añadido exitosamente.")

    def actualizar_producto(self, nombre, cantidad, precio):
        """Actualiza un producto existente en el inventario."""
        if nombre not in self.productos:
            print("Error: El producto no existe en el inventario.")
            return
        self.productos[nombre].cantidad = cantidad
        self.productos[nombre].precio = precio
        self.guardar_inventario()
        print(f"Producto '{nombre}' actualizado exitosamente.")

    def eliminar_producto(self, nombre):
        """Elimina un producto del inventario."""
        if nombre not in self.productos:
            print("Error: El producto no existe en el inventario.")
            return
        del self.productos[nombre]
        self.guardar_inventario()
        print(f"Producto '{nombre}' eliminado exitosamente.")

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("El inventario está vacío.")
            return
        for producto in self.productos.values():
            print(producto)

# Ejemplo de uso
if __name__ == "__main__":
    inventario = Inventario()
    inventario.mostrar_inventario()
    inventario.añadir_producto("Manzana", 50, 0.5)
    inventario.añadir_producto("Banana", 30, 0.3)
    inventario.actualizar_producto("Manzana", 60, 0.55)
    inventario.eliminar_producto("Banana")
    inventario.mostrar_inventario()