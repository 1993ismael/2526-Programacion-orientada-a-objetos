# Sistema de Reservas de una Biblioteca
# Ejemplo del mundo real usando Programación Orientada a Objetos (POO)

class Libro:
    """
    Clase que representa un libro de la biblioteca
    """
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar(self):
        self.disponible = False

    def devolver(self):
        self.disponible = True


class Usuario:
    """
    Clase que representa a un usuario de la biblioteca
    """
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []

    def tomar_libro(self, libro):
        self.libros_prestados.append(libro)


class Biblioteca:
    """
    Clase que gestiona los libros y las reservas
    """
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def prestar_libro(self, titulo, usuario):
        for libro in self.libros:
            if libro.titulo == titulo and libro.disponible:
                libro.prestar()
                usuario.tomar_libro(libro)
                print(f"Libro '{titulo}' prestado a {usuario.nombre}")
                return
        print(f"El libro '{titulo}' no está disponible")

    def mostrar_libros(self):
        for libro in self.libros:
            estado = "Disponible" if libro.disponible else "Prestado"
            print(f"{libro.titulo} - {libro.autor} ({estado})")


# Programa principal
biblioteca = Biblioteca()

libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")
libro2 = Libro("El Principito", "Antoine de Saint-Exupéry")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

usuario1 = Usuario("Ismael")

biblioteca.mostrar_libros()
biblioteca.prestar_libro("El Principito", usuario1)
biblioteca.mostrar_libros()
