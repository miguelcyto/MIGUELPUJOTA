import json
import os

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_id(self, id):
        self.id = id

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio


class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto.get_id()] = producto

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
        else:
            print("Producto no encontrado")

    def actualizar_cantidad(self, id, cantidad):
        if id in self.productos:
            self.productos[id].set_cantidad(cantidad)
        else:
            print("Producto no encontrado")

    def actualizar_precio(self, id, precio):
        if id in self.productos:
            self.productos[id].set_precio(precio)
        else:
            print("Producto no encontrado")

    def buscar_producto(self, nombre):
        for producto in self.productos.values():
            if producto.get_nombre().lower() == nombre.lower():
                return producto
        return None

    def mostrar_productos(self):
        for producto in self.productos.values():
            print(producto)


def guardar_inventario(inventario, archivo):
    datos = {}
    for id, producto in inventario.productos.items():
        datos[id] = {
            "nombre": producto.get_nombre(),
            "cantidad": producto.get_cantidad(),
            "precio": producto.get_precio()
        }
    with open(archivo, "w") as f:
        json.dump(datos, f)


def cargar_inventario(archivo):
    inventario = Inventario()
    if os.path.exists(archivo):
        with open(archivo, "r") as f:
            datos = json.load(f)
            for id, producto in datos.items():
                inventario.agregar_producto(Producto(id, producto["nombre"], producto["cantidad"], producto["precio"]))
    return inventario


def main():
    archivo = "inventario.json"
    inventario = cargar_inventario(archivo)

    while True:
        print("Menú de opciones:")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar cantidad")
        print("4. Actualizar precio")
        print("5. Buscar producto")
        print("6. Mostrar productos")
        print("7. Salir")

        opcion = input("Ingrese su opción: ")

        if opcion == "1":
            id = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == "2":
            id = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id)
        elif opcion == "3":
            id = input("Ingrese el ID del producto a actualizar: ")
            cantidad = int(input("Ingrese la nueva cantidad: "))
            inventario.actualizar_cantidad(id, cantidad)
        elif opcion == "4":
            id = input("Ingrese el ID del producto a actualizar: ")
            precio = float(input("Ingrese el nuevo precio: "))
            inventario.actualizar_precio(id, precio)
        elif opcion == "5":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            producto = inventario.buscar_producto(nombre)
            if producto:
                print(producto)
            else:
                print("Producto no encontrado")
        elif opcion == "6":
            inventario.mostrar_productos()
        elif opcion == "7":
            guardar_inventario(inventario, archivo)
            break
        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()