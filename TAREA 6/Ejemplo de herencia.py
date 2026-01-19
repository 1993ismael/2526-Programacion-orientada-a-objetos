# EJEMPLO DE HERENCIA

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Mi nombre es {self.nombre} y tengo {self.edad} años."


# Clase derivada que hereda de Persona
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)  # Hereda atributos de Persona
        self.carrera = carrera

    def datos_estudiante(self):
        return f"Estudio la carrera de {self.carrera}."


# Creación de objetos
persona1 = Persona("Carlos", 35)
estudiante1 = Estudiante("Ismael", 22, "Educación Inicial")

# Uso de métodos
print(persona1.presentarse())
print(estudiante1.presentarse())       # Método heredado
print(estudiante1.datos_estudiante())  # Método propio
