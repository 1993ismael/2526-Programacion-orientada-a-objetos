# EJEMPLO DE ENCAPSULACIÓN

class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.__nota = nota  # Atributo privado (encapsulado)

    # Método para obtener la nota
    def obtener_nota(self):
        return self.__nota

    # Método para modificar la nota
    def cambiar_nota(self, nueva_nota):
        if 0 <= nueva_nota <= 10:
            self.__nota = nueva_nota
        else:
            print("La nota debe estar entre 0 y 10")


# Creación del objeto
estudiante = Estudiante("Ismael", 8)

# Acceso a la nota (encapsulación)
print("Nota inicial:", estudiante.obtener_nota())

# Modificación controlada de la nota
estudiante.cambiar_nota(9)

print("Nota final:", estudiante.obtener_nota())
