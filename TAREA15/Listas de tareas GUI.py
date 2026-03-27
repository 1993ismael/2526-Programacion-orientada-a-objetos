import tkinter as tk
from tkinter import messagebox

class ListaTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("400x400")

        # Lista donde se almacenan las tareas
        self.tareas = []

        # ===== Campo de entrada =====
        self.entrada = tk.Entry(root, width=30)
        self.entrada.pack(pady=10)

        # Evento: presionar Enter para añadir tarea
        self.entrada.bind("<Return>", self.agregar_tarea_evento)

        # ===== Botones =====
        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=5)

        btn_agregar = tk.Button(frame_botones, text="Añadir Tarea", command=self.agregar_tarea)
        btn_agregar.grid(row=0, column=0, padx=5)

        btn_completar = tk.Button(frame_botones, text="Marcar como Completada", command=self.marcar_completada)
        btn_completar.grid(row=0, column=1, padx=5)

        btn_eliminar = tk.Button(frame_botones, text="Eliminar Tarea", command=self.eliminar_tarea)
        btn_eliminar.grid(row=0, column=2, padx=5)

        # ===== Lista de tareas =====
        self.lista = tk.Listbox(root, width=50, height=15)
        self.lista.pack(pady=10)

        # Evento: doble clic para completar tarea
        self.lista.bind("<Double-Button-1>", self.marcar_completada_evento)

    # ===== Funciones =====

    def agregar_tarea(self):
        tarea = self.entrada.get().strip()

        if tarea == "":
            messagebox.showwarning("Aviso", "Escribe una tarea")
            return

        self.tareas.append({"texto": tarea, "completada": False})
        self.actualizar_lista()
        self.entrada.delete(0, tk.END)

    def agregar_tarea_evento(self, event):
        self.agregar_tarea()

    def marcar_completada(self):
        try:
            indice = self.lista.curselection()[0]
            self.tareas[indice]["completada"] = True
            self.actualizar_lista()
        except:
            messagebox.showwarning("Aviso", "Selecciona una tarea")

    def marcar_completada_evento(self, event):
        self.marcar_completada()

    def eliminar_tarea(self):
        try:
            indice = self.lista.curselection()[0]
            del self.tareas[indice]
            self.actualizar_lista()
        except:
            messagebox.showwarning("Aviso", "Selecciona una tarea")

    def actualizar_lista(self):
        self.lista.delete(0, tk.END)

        for tarea in self.tareas:
            if tarea["completada"]:
                self.lista.insert(tk.END, "✔ " + tarea["texto"])
            else:
                self.lista.insert(tk.END, tarea["texto"])


# ===== Ejecutar la aplicación =====
if __name__ == "__main__":
    root = tk.Tk()
    app = ListaTareasApp(root)
    root.mainloop()