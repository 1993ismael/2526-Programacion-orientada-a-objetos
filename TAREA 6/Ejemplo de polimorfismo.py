# POLIMORFISMO MEDIANTE MÉTODOS SOBRESCRITOS

class Evaluacion:
    def calcular_nota(self):
        pass  # Método que será sobrescrito


class Examen(Evaluacion):
    def __init__(self, aciertos):
        self.aciertos = aciertos

    def calcular_nota(self):
        # Examen calificado sobre 10
        return (self.aciertos / 10) * 10


class Tarea(Evaluacion):
    def __init__(self, puntaje):
        self.puntaje = puntaje

    def calcular_nota(self):
        # Tarea calificada directamente sobre 10
        return self.puntaje


# Creación de objetos
examen = Examen(7)
tarea = Tarea(9)

# Lista de evaluaciones (polimorfismo)
evaluaciones = [examen, tarea]

# Uso del mismo método en diferentes clases
for evaluacion in evaluaciones:
    print("Nota final:", evaluacion.calcular_nota())


