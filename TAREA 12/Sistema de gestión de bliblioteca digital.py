# ==========================================
# SISTEMA DE GESTIÓN DE BIBLIOTECA DIGITAL
# ==========================================

# ------------------------------
# Clase Libro
# ------------------------------
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Tupla para datos inmutables
        self.__info = (titulo, autor)
        self.__categoria = categoria
        self.__isbn = isbn
        self.__disponible = True  # Controla si el libro está prestado

    def get_titulo(self):
        return self.__info[0]

    def get_autor(self):
        return self.__info[1]

    def get_categoria(self):
        return self.__categoria

    def get_isbn(self):
        return self.__isbn

    def esta_disponible(self):
        return self.__disponible

    def prestar(self):
        self.__disponible = False

    def devolver(self):
        self.__disponible = True

    def __str__(self):
        estado = "Disponible" if self.__disponible else "Prestado"
        return f"Título: {self.get_titulo()} | Autor: {self.get_autor()} | Categoría: {self.__categoria} | ISBN: {self.__isbn} | Estado: {estado}"


# ------------------------------
# Clase Usuario
# ------------------------------
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.__nombre = nombre
        self.__id_usuario = id_usuario
        self.__libros_prestados = []  # Lista de libros prestados

    def get_id(self):
        return self.__id_usuario

    def get_nombre(self):
        return self.__nombre

    def prestar_libro(self, libro):
        self.__libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.__libros_prestados:
            self.__libros_prestados.remove(libro)

    def listar_libros(self):
        if not self.__libros_prestados:
            print("No tiene libros prestados.")
        else:
            for libro in self.__libros_prestados:
                print(libro)

    def __str__(self):
        return f"Usuario: {self.__nombre} | ID: {self.__id_usuario}"


# ------------------------------
# Clase Biblioteca
# ------------------------------
class Biblioteca:
    def __init__(self):
        self.__libros = {}        # Diccionario ISBN -> Libro
        self.__usuarios = {}      # Diccionario ID -> Usuario
        self.__ids_usuarios = set()  # Conjunto para IDs únicos

    # --------------------------
    # Añadir libro
    # --------------------------
    def agregar_libro(self, libro):
        if libro.get_isbn() not in self.__libros:
            self.__libros[libro.get_isbn()] = libro
            print("Libro agregado correctamente.")
        else:
            print("El libro ya existe en la biblioteca.")

    # --------------------------
    # Quitar libro
    # --------------------------
    def quitar_libro(self, isbn):
        if isbn in self.__libros:
            del self.__libros[isbn]
            print("Libro eliminado.")
        else:
            print("Libro no encontrado.")

    # --------------------------
    # Registrar usuario
    # --------------------------
    def registrar_usuario(self, usuario):
        if usuario.get_id() not in self.__ids_usuarios:
            self.__usuarios[usuario.get_id()] = usuario
            self.__ids_usuarios.add(usuario.get_id())
            print("Usuario registrado correctamente.")
        else:
            print("ID de usuario ya existente.")

    # --------------------------
    # Dar de baja usuario
    # --------------------------
    def eliminar_usuario(self, id_usuario):
        if id_usuario in self.__usuarios:
            del self.__usuarios[id_usuario]
            self.__ids_usuarios.remove(id_usuario)
            print("Usuario eliminado.")
        else:
            print("Usuario no encontrado.")

    # --------------------------
    # Prestar libro
    # --------------------------
    def prestar_libro(self, isbn, id_usuario):
        if isbn in self.__libros and id_usuario in self.__usuarios:
            libro = self.__libros[isbn]
            usuario = self.__usuarios[id_usuario]

            if libro.esta_disponible():
                libro.prestar()
                usuario.prestar_libro(libro)
                print("Libro prestado correctamente.")
            else:
                print("El libro no está disponible.")
        else:
            print("Libro o usuario no encontrado.")

    # --------------------------
    # Devolver libro
    # --------------------------
    def devolver_libro(self, isbn, id_usuario):
        if isbn in self.__libros and id_usuario in self.__usuarios:
            libro = self.__libros[isbn]
            usuario = self.__usuarios[id_usuario]

            libro.devolver()
            usuario.devolver_libro(libro)
            print("Libro devuelto correctamente.")
        else:
            print("Libro o usuario no encontrado.")

    # --------------------------
    # Buscar libros
    # --------------------------
    def buscar_por_titulo(self, titulo):
        for libro in self.__libros.values():
            if libro.get_titulo().lower() == titulo.lower():
                print(libro)

    def buscar_por_autor(self, autor):
        for libro in self.__libros.values():
            if libro.get_autor().lower() == autor.lower():
                print(libro)

    def buscar_por_categoria(self, categoria):
        for libro in self.__libros.values():
            if libro.get_categoria().lower() == categoria.lower():
                print(libro)


# ==========================================
# PRUEBAS DEL SISTEMA
# ==========================================

# Crear biblioteca
biblioteca = Biblioteca()

# Crear libros
libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "111")
libro2 = Libro("1984", "George Orwell", "Distopía", "222")
libro3 = Libro("El Principito", "Antoine de Saint-Exupéry", "Fábula", "333")

# Agregar libros
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

# Crear usuarios
usuario1 = Usuario("Ismael", "U001")
usuario2 = Usuario("María", "U002")

# Registrar usuarios
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libro
biblioteca.prestar_libro("111", "U001")

# Listar libros prestados
print("\nLibros prestados a Ismael:")
usuario1.listar_libros()

# Devolver libro
biblioteca.devolver_libro("111", "U001")

# Buscar libro
print("\nBuscar por autor:")
biblioteca.buscar_por_autor("George Orwell")