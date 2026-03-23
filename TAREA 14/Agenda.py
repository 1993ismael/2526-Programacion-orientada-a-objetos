# Aplicación de Agenda Personal con Tkinter
# Incluye: TreeView, DatePicker, agregar y eliminar eventos

import tkinter as tk
from tkinter import ttk, messagebox

# Intentar importar DateEntry (DatePicker)
try:
    from tkcalendar import DateEntry
    calendario_disponible = True
except:
    calendario_disponible = False

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("600x400")

        # ===== Frame lista =====
        frame_lista = tk.Frame(root)
        frame_lista.pack(pady=10)

        self.tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripcion"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripcion", text="Descripción")
        self.tree.pack()

        # Evento de ejemplo
        self.tree.insert("", "end", values=("2026-03-20", "18:30", "Reunión de proyecto"))

        # ===== Frame entrada =====
        frame_entrada = tk.Frame(root)
        frame_entrada.pack(pady=10)

        tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0)

        if calendario_disponible:
            self.fecha_entry = DateEntry(frame_entrada, date_pattern='yyyy-mm-dd')
        else:
            self.fecha_entry = tk.Entry(frame_entrada)
            self.fecha_entry.insert(0, "2026-03-20")

        self.fecha_entry.grid(row=0, column=1)

        tk.Label(frame_entrada, text="Hora:").grid(row=1, column=0)
        self.hora_entry = tk.Entry(frame_entrada)
        self.hora_entry.grid(row=1, column=1)
        self.hora_entry.insert(0, "18:30")

        tk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0)
        self.desc_entry = tk.Entry(frame_entrada)
        self.desc_entry.grid(row=2, column=1)
        self.desc_entry.insert(0, "Evento de ejemplo")

        # ===== Frame botones =====
        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento).grid(row=0, column=0, padx=5)
        tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento).grid(row=0, column=1, padx=5)
        tk.Button(frame_botones, text="Salir", command=root.quit).grid(row=0, column=2, padx=5)

    def agregar_evento(self):
        fecha = self.fecha_entry.get()
        hora = self.hora_entry.get()
        descripcion = self.desc_entry.get()

        if fecha and hora and descripcion:
            self.tree.insert("", "end", values=(fecha, hora, descripcion))
            self.hora_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "Todos los campos son obligatorios")

    def eliminar_evento(self):
        seleccionado = self.tree.selection()

        if not seleccionado:
            messagebox.showwarning("Error", "Seleccione un evento")
            return

        confirmacion = messagebox.askyesno("Confirmar", "¿Desea eliminar el evento?")

        if confirmacion:
            self.tree.delete(seleccionado)

# Ejecutar
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()