# ======================================
# APLICACIÓN GUI BÁSICA CON TKINTER
# ======================================

import tkinter as tk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Aplicación de Lista de Tareas")
ventana.geometry("400x300")

# ------------------------------
# Función para agregar elementos
# ------------------------------
def agregar_dato():
    dato = entrada_texto.get()  # Obtener texto del campo
    if dato != "":
        lista_datos.insert(tk.END, dato)  # Agregar a la lista
        entrada_texto.delete(0, tk.END)  # Limpiar campo de texto

# ------------------------------
# Función para limpiar elemento
# ------------------------------
def limpiar_dato():
    seleccion = lista_datos.curselection()
    if seleccion:
        lista_datos.delete(seleccion)

# ------------------------------
# Componentes de la interfaz
# ------------------------------

# Etiqueta
label = tk.Label(ventana, text="Ingrese un dato:")
label.pack()

# Campo de texto
entrada_texto = tk.Entry(ventana)
entrada_texto.pack()

# Botón Agregar
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack()

# Lista para mostrar datos
lista_datos = tk.Listbox(ventana)
lista_datos.pack(fill=tk.BOTH, expand=True)

# Botón Limpiar
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_dato)
boton_limpiar.pack()

# Ejecutar aplicación
ventana.mainloop()