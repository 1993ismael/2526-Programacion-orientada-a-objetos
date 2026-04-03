import tkinter as tk
from tkinter import messagebox

# Lista donde se guardan las tareas
tareas = []

# Función para añadir tarea
def agregar_tarea(event=None):
    tarea = entrada.get()
    if tarea != "":
        tareas.append({"texto": tarea, "completada": False})
        actualizar_lista()
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Escribe una tarea")

# Función para actualizar la lista visual
def actualizar_lista():
    lista.delete(0, tk.END)
    for i, tarea in enumerate(tareas):
        texto = tarea["texto"]
        if tarea["completada"]:
            lista.insert(tk.END, f"✔ {texto}")
            lista.itemconfig(i, fg="gray")
        else:
            lista.insert(tk.END, f"✗ {texto}")

# Función para marcar como completada
def completar_tarea(event=None):
    try:
        indice = lista.curselection()[0]
        tareas[indice]["completada"] = True
        actualizar_lista()
    except:
        messagebox.showwarning("Aviso", "Selecciona una tarea")

# Función para eliminar tarea
def eliminar_tarea(event=None):
    try:
        indice = lista.curselection()[0]
        tareas.pop(indice)
        actualizar_lista()
    except:
        messagebox.showwarning("Aviso", "Selecciona una tarea")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Tareas")
ventana.geometry("400x400")

# Campo de entrada
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=10)

# Botones
btn_agregar = tk.Button(ventana, text="Agregar Tarea", command=agregar_tarea)
btn_agregar.pack()

btn_completar = tk.Button(ventana, text="Completar Tarea", command=completar_tarea)
btn_completar.pack()

btn_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.pack()

# Lista de tareas
lista = tk.Listbox(ventana, width=40, height=10)
lista.pack(pady=10)

# ATAJOS DE TECLADO
ventana.bind("<Return>", agregar_tarea)     # Enter → agregar
ventana.bind("c", completar_tarea)          # C → completar
ventana.bind("d", eliminar_tarea)           # D → eliminar
ventana.bind("<Delete>", eliminar_tarea)    # Delete → eliminar
ventana.bind("<Escape>", lambda e: ventana.destroy())  # Escape → salir

# Ejecutar app
ventana.mainloop()