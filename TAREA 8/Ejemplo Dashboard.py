# Dashboard.py
# Autor: Ismael
# Descripción: Dashboard para gestionar tareas del curso de POO

class Tarea:
    def __init__(self, titulo, descripcion, estado="Pendiente"):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado

    def completar(self):
        self.estado = "Completada"

    def __str__(self):
        return f"{self.titulo} - {self.descripcion} [{self.estado}]"


class Dashboard:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, titulo, descripcion):
        tarea = Tarea(titulo, descripcion)
        self.tareas.append(tarea)
        print("✅ Tarea agregada correctamente")

    def mostrar_tareas(self):
        if not self.tareas:
            print("📭 No hay tareas registradas")
        else:
            for i, tarea in enumerate(self.tareas, 1):
                print(f"{i}. {tarea}")

    def completar_tarea(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice].completar()
            print("🎉 Tarea marcada como completada")
        else:
            print("❌ Índice inválido")

    def menu(self):
        while True:
            print("\n📌 DASHBOARD POO")
            print("1. Agregar tarea")
            print("2. Ver tareas")
            print("3. Completar tarea")
            print("4. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                titulo = input("Título: ")
                descripcion = input("Descripción: ")
                self.agregar_tarea(titulo, descripcion)

            elif opcion == "2":
                self.mostrar_tareas()

            elif opcion == "3":
                self.mostrar_tareas()
                indice = int(input("Número de tarea a completar: ")) - 1
                self.completar_tarea(indice)

            elif opcion == "4":
                print("👋 Saliendo del Dashboard")
                break

            else:
                print("⚠️ Opción no válida")


if __name__ == "__main__":
    dashboard = Dashboard()
    dashboard.menu()
