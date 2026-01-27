class Archivo:
    """
    Clase que demuestra el uso de constructores y destructores en Python.
    Simula la apertura y cierre de un archivo.
    """

    def __init__(self, nombre_archivo):
        """
        CONSTRUCTOR
        Se ejecuta automáticamente cuando se crea un objeto de la clase.
        Inicializa los atributos del objeto.
        """
        self.nombre_archivo = nombre_archivo
        self.archivo_abierto = True
        print(f"📂 El archivo '{self.nombre_archivo}' ha sido abierto.")

    def escribir(self, texto):
        """
        Método que simula la escritura en un archivo.
        """
        if self.archivo_abierto:
            print(f"✍️ Escribiendo en '{self.nombre_archivo}': {texto}")
        else:
            print("❌ No se puede escribir, el archivo está cerrado.")

    def __del__(self):
        """
        DESTRUCTOR
        Se ejecuta automáticamente cuando el objeto es eliminado
        o cuando el programa finaliza.
        Se encarga de liberar recursos.
        """
        if self.archivo_abierto:
            self.archivo_abierto = False
            print(f"🔒 El archivo '{self.nombre_archivo}' ha sido cerrado correctamente.")


# PROGRAMA PRINCIPAL
print("=== Programa de Constructores y Destructores ===")

archivo1 = Archivo("datos.txt")
archivo1.escribir("Hola, este es un ejemplo de constructor y destructor en Python.")

# Al finalizar el programa o eliminar el objeto,
# el destructor (__del__) se ejecutará automáticamente
