# Clase Producto representa un artículo en la tienda es lo que en el mundo real
# o en la vida diaria podemos emplear.
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"{self.nombre} - Precio: ${self.precio:.2f} - Stock: {self.stock}"

    def actualizar_stock(self, cantidad):
        self.stock += cantidad

# Clase Cliente representa un cliente de la tienda
class Cliente:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

    def __str__(self):
        return f"Cliente: {self.nombre} - Email: {self.email}"


# Clase Orden representa una orden realizada por un cliente
class Orden:
    def __init__(self, cliente, productos):
        self.cliente = cliente
        self.productos = productos  # Lista de productos
        self.total = sum(producto.precio for producto in productos)

    def __str__(self):
        productos_str = ", ".join([producto.nombre for producto in self.productos])
        return f"Orden de {self.cliente.nombre}: {productos_str} - Total: ${self.total:.2f}"


# Clase Tienda maneja los productos, clientes y órdenes
class Tienda:
    def __init__(self):
        self.productos = []
        self.clientes = []
        self.ordenes = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)

    def realizar_orden(self, cliente_email, nombres_productos):
        cliente = next((c for c in self.clientes if c.email == cliente_email), None)
        if not cliente:
            print("Cliente no registrado.")
            return None

        productos_orden = []
        for nombre in nombres_productos:
            producto = next((p for p in self.productos if p.nombre == nombre and p.stock > 0), None)
            if producto:
                productos_orden.append(producto)
                producto.actualizar_stock(-1)
            else:
                print(f"Producto {nombre} no disponible.")

        if productos_orden:
            orden = Orden(cliente, productos_orden)
            self.ordenes.append(orden)
            print("Orden realizada con éxito.")
            return orden
        else:
            print("No se pudo realizar la orden.")
            return None

    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)

    def mostrar_clientes(self):
        for cliente in self.clientes:
            print(cliente)

    def mostrar_ordenes(self):
        for orden in self.ordenes:
            print(orden)


# Demostración de uso

# Creando la tienda
tienda = Tienda()

# Creando y agregando productos
producto1 = Producto("Laptop", 500.00, 10)
producto2 = Producto("Smartphone", 800.00, 15)
producto3 = Producto("Audífonos", 50.00, 50)

tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)
tienda.agregar_producto(producto3)

# Mostrando productos disponibles
print("Productos disponibles:")
tienda.mostrar_productos()

# Registrando un cliente
cliente1 = Cliente("Ana García", "ana@hotmail.com")
tienda.registrar_cliente(cliente1)

# Mostrando clientes registrados
print("\nClientes registrados:")
tienda.mostrar_clientes()

# Realizando una orden
print("\nRealizando una orden:")
tienda.realizar_orden("ana@hotmail.com", ["Laptop", "Audífonos"])

# Mostrando órdenes realizadas
print("\nÓrdenes realizadas:")
tienda.mostrar_ordenes()

# Mostrando productos disponibles después de la orden
print("\nProductos disponibles después de la orden:")
tienda.mostrar_productos()
