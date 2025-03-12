import json

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def obtener_id(self):
        return self.id_producto

    def obtener_nombre(self):
        return self.nombre

    def obtener_cantidad(self):
        return self.cantidad

    def obtener_precio(self):
        return self.precio

    def establecer_cantidad(self, cantidad):
        self.cantidad = cantidad

    def establecer_precio(self, precio):
        self.precio = precio

    def to_dict(self):
        return {
            'id_producto': self.id_producto,
            'nombre': self.nombre,
            'cantidad': self.cantidad,
            'precio': self.precio
        }

class Inventario:
    def __init__(self):
        self.productos = {}

    def añadir_producto(self, producto):
        self.productos[producto.obtener_id()] = producto

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print(f"Producto con ID {id_producto} eliminado.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].establecer_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].establecer_precio(precio)
            print(f"Producto con ID {id_producto} actualizado.")
        else:
            print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        resultados = [producto for producto in self.productos.values() if nombre.lower() in producto.obtener_nombre().lower()]
        return resultados

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            for producto in self.productos.values():
                print(f"ID: {producto.obtener_id()}, Nombre: {producto.obtener_nombre()}, Cantidad: {producto.obtener_cantidad()}, Precio: {producto.obtener_precio()}")

    def guardar_inventario(self, archivo):
        with open(archivo, 'w') as f:
            json.dump({id: producto.to_dict() for id, producto in self.productos.items()}, f)
        print("Inventario guardado en el archivo.")

    def cargar_inventario(self, archivo):
        try:
            with open(archivo, 'r') as f:
                data = json.load(f)
                for id_producto, info in data.items():
                    producto = Producto(info['id_producto'], info['nombre'], info['cantidad'], info['precio'])
                    self.añadir_producto(producto)
            print("Inventario cargado desde el archivo.")
        except FileNotFoundError:
            print("Archivo no encontrado. Se creará un nuevo inventario.")

def menu():
    inventario = Inventario()
    inventario.cargar_inventario('inventario.json')

    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Guardar inventario")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)
            print("Producto añadido.")

        elif opcion == '2':
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == '3':
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ")
            precio = input("Nuevo precio (dejar vacío para no cambiar): ")
            inventario.actualizar_producto(id_producto, int(cantidad) if cantidad else None, float(precio) if precio else None)

        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            if resultados:
                for producto in resultados:
                    print(f"ID: {producto.obtener_id()}, Nombre: {producto.obtener_nombre()}, Cantidad: {producto.obtener_cantidad()}, Precio: {producto.obtener_precio()}")
            else:
                print("Producto no encontrado.")

        elif opcion == '5':
            inventario.mostrar_productos()

        elif opcion == '6':
            inventario.guardar_inventario('inventario.json')

        elif opcion == '7':
            inventario.guardar_inventario('inventario.json')
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 7.")

if __name__ == "__main__":
    menu()