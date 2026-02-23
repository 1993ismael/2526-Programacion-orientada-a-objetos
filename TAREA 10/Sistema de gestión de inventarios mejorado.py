# ==============================
# SISTEMA DE INVENTARIO MEJORADO
# ==============================

import os

# ------------------------------
# Clase Producto
# ------------------------------
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.id},{self.nombre},{self.cantidad},{self.precio}"


# ------------------------------
# Clase Inventario
# ------------------------------
class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.productos = {}
        self.archivo = archivo
        self.cargar_desde_archivo()

    # --------------------------
    # Cargar productos del archivo
    # --------------------------
    def cargar_desde_archivo(self):
        try:
            # Si el archivo no existe o está vacío
            if not os.path.exists(self.archivo) or os.path.getsize(self.archivo) == 0:
                print("Archivo no encontrado o vacío. Creando productos iniciales...")

                productos_iniciales = [
                    Producto("P001", "Arroz", 50, 1.25),
                    Producto("P002", "Café", 30, 2.50),
                    Producto("P003", "Azúcar", 40, 1.10),
                    Producto("P004", "Aceite", 20, 3.75),
                    Producto("P005", "Maní", 35, 1.80),
                ]

                for producto in productos_iniciales:
                    self.productos[producto.id] = producto

                self.guardar_en_archivo()
                print("Productos iniciales creados correctamente.")
                return

            # Si el archivo tiene datos, los carga
            with open(self.archivo, "r") as file:
                for linea in file:
                    datos = linea.strip().split(",")
                    if len(datos) == 4:
                        id, nombre, cantidad, precio = datos
                        self.productos[id] = Producto(
                            id,
                            nombre,
                            int(cantidad),
                            float(precio)
                        )

            print("Inventario cargado correctamente desde el archivo.")

        except FileNotFoundError:
            print("Error: No se encontró el archivo.")
        except PermissionError:
            print("Error: No tienes permisos para leer el archivo.")
        except Exception as e:
            print("Error inesperado al cargar el archivo:", e)

    # --------------------------
    # Guardar inventario en archivo
    # --------------------------
    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w") as file:
                for producto in self.productos.values():
                    file.write(str(producto) + "\n")
            print("Inventario guardado correctamente.")

        except PermissionError:
            print("Error: No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print("Error inesperado al guardar:", e)

    # --------------------------
    # Añadir producto
    # --------------------------
    def añadir_producto(self, producto):
        if producto.id in self.productos:
            print("Error: El producto ya existe.")
        else:
            self.productos[producto.id] = producto
            self.guardar_en_archivo()
            print("Producto añadido exitosamente.")

    # --------------------------
    # Actualizar producto
    # --------------------------
    def actualizar_producto(self, id, cantidad, precio):
        if id in self.productos:
            self.productos[id].cantidad = cantidad
            self.productos[id].precio = precio
            self.guardar_en_archivo()
            print("Producto actualizado exitosamente.")
        else:
            print("Error: Producto no encontrado.")

    # --------------------------
    # Eliminar producto
    # --------------------------
    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            self.guardar_en_archivo()
            print("Producto eliminado exitosamente.")
        else:
            print("Error: Producto no encontrado.")

    # --------------------------
    # Buscar producto
    # --------------------------
    def buscar_producto(self, id):
        if id in self.productos:
            print("Producto encontrado:")
            print(self.productos[id])
        else:
            print("Producto no encontrado.")

    # --------------------------
    # Mostrar inventario
    # --------------------------
    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("=== INVENTARIO ACTUAL ===")
            for producto in self.productos.values():
                print(producto)


# ------------------------------
# Interfaz de Usuario
# ------------------------------
def menu():
    inventario = Inventario()

    while True:
        print("\n===== MENÚ INVENTARIO =====")
        print("1. Añadir producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                id = input("ID: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                producto = Producto(id, nombre, cantidad, precio)
                inventario.añadir_producto(producto)

            elif opcion == "2":
                id = input("ID del producto a actualizar: ")
                cantidad = int(input("Nueva cantidad: "))
                precio = float(input("Nuevo precio: "))
                inventario.actualizar_producto(id, cantidad, precio)

            elif opcion == "3":
                id = input("ID del producto a eliminar: ")
                inventario.eliminar_producto(id)

            elif opcion == "4":
                id = input("ID del producto a buscar: ")
                inventario.buscar_producto(id)

            elif opcion == "5":
                inventario.mostrar_inventario()

            elif opcion == "6":
                print("Saliendo del programa...")
                break

            else:
                print("Opción inválida.")

        except ValueError:
            print("Error: Debe ingresar números válidos en cantidad y precio.")
        except Exception as e:
            print("Error inesperado:", e)


# Ejecutar programa
if __name__ == "__main__":
    menu()