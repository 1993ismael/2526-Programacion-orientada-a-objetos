# ==========================================
# SISTEMA DE INVENTARIO CON PRODUCTOS BASE
# ==========================================

import json
import os

# ------------------------------
# Clase Producto
# ------------------------------
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.__id = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    def get_id(self):
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    def set_precio(self, precio):
        self.__precio = precio

    def to_dict(self):
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "cantidad": self.__cantidad,
            "precio": self.__precio
        }


# ------------------------------
# Clase Inventario
# ------------------------------
class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.productos = {}
        self.archivo = archivo
        self.cargar_archivo()

        # Si no existe archivo, cargar productos base
        if not self.productos:
            self.cargar_productos_base()

    def cargar_productos_base(self):
        print("📦 Cargando productos base...")
        productos_base = [
            Producto("1", "Arroz", 50, 1.20),
            Producto("2", "Azúcar", 30, 0.90),
            Producto("3", "Leche", 25, 1.00),
            Producto("4", "Aceite", 20, 2.50),
            Producto("5", "Fideos", 40, 0.75)
        ]

        for producto in productos_base:
            self.productos[producto.get_id()] = producto

    def añadir_producto(self, producto):
        if producto.get_id() in self.productos:
            print("❌ El producto ya existe.")
        else:
            self.productos[producto.get_id()] = producto
            print("✅ Producto añadido.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("🗑 Producto eliminado.")
        else:
            print("❌ Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].set_precio(precio)
            print("🔄 Producto actualizado.")
        else:
            print("❌ Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        encontrados = []
        for producto in self.productos.values():
            if nombre.lower() in producto.get_nombre().lower():
                encontrados.append(producto)

        if encontrados:
            for p in encontrados:
                print(f"ID: {p.get_id()} | Nombre: {p.get_nombre()} | "
                      f"Cantidad: {p.get_cantidad()} | Precio: ${p.get_precio()}")
        else:
            print("❌ No se encontraron productos.")

    def mostrar_todos(self):
        print("\n===== INVENTARIO =====")
        for p in self.productos.values():
            print(f"ID: {p.get_id()} | Nombre: {p.get_nombre()} | "
                  f"Cantidad: {p.get_cantidad()} | Precio: ${p.get_precio()}")

    def guardar_archivo(self):
        datos = [producto.to_dict() for producto in self.productos.values()]
        with open(self.archivo, "w") as f:
            json.dump(datos, f, indent=4)
        print("💾 Inventario guardado.")

    def cargar_archivo(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r") as f:
                datos = json.load(f)
                for item in datos:
                    producto = Producto(
                        item["id"],
                        item["nombre"],
                        item["cantidad"],
                        item["precio"]
                    )
                    self.productos[item["id"]] = producto


# ------------------------------
# Menú
# ------------------------------
def menu():
    inventario = Inventario()

    while True:
        print("\n===== MENÚ =====")
        print("1. Mostrar productos")
        print("2. Añadir producto")
        print("3. Eliminar producto")
        print("4. Actualizar producto")
        print("5. Buscar producto")
        print("6. Guardar y salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            inventario.mostrar_todos()

        elif opcion == "2":
            id_producto = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.añadir_producto(
                Producto(id_producto, nombre, cantidad, precio)
            )

        elif opcion == "3":
            id_producto = input("ID a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "4":
            id_producto = input("ID a actualizar: ")
            cantidad = input("Nueva cantidad (Enter si no cambia): ")
            precio = input("Nuevo precio (Enter si no cambia): ")

            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "5":
            nombre = input("Nombre a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "6":
            inventario.guardar_archivo()
            print("👋 Sistema cerrado.")
            break
 
        else:
            print("❌ Opción inválida.")


if __name__ == "__main__":
    menu()