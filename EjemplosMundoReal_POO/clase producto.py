# Clase Producto
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_info(self):
        return f"Producto: {self.nombre} - Precio: ${self.precio}"


# Clase Cliente
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = []

    def agregar_producto(self, producto):
        self.carrito.append(producto)
        print(f"{producto.nombre} agregado al carrito de {self.nombre}")

    def calcular_total(self):
        total = sum(producto.precio for producto in self.carrito)
        return total


# Clase Tienda
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print(f"Productos disponibles en {self.nombre}:")
        for producto in self.productos:
            print(producto.mostrar_info())


# Programa principal
if __name__ == "__main__":
    # Crear tienda
    tienda = Tienda("Tienda Central")

    # Crear productos
    producto1 = Producto("Cuaderno", 2.50)
    producto2 = Producto("Lápiz", 0.50)

    # Agregar productos a la tienda
    tienda.agregar_producto(producto1)
    tienda.agregar_producto(producto2)

    # Mostrar productos
    tienda.mostrar_productos()

    # Crear cliente
    cliente = Cliente("Ismael")

    # Cliente compra productos
    cliente.agregar_producto(producto1)
    cliente.agregar_producto(producto2)

    # Mostrar total
    print(f"Total a pagar: ${cliente.calcular_total()}")
