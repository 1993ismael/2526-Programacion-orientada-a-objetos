# ============================================
#      Clase base: Vehiculo
# ============================================

# --------------------------------------------
# 1. ABSTRACCIÓN (Clase Vehiculo)
# --------------------------------------------
# Representa solo lo esencial de un vehículo:
# marca, modelo, año.
# --------------------------------------------

class Vehiculo:
    def __init__(self, marca, modelo, año):
        # 2. ENCAPSULAMIENTO (atributos protegidos)
        self._marca = marca
        self._modelo = modelo
        self._año = año

    # Método general (abstracción)
    def descripcion(self):
        return f"{self._marca} {self._modelo} - Año: {self._año}"

    # Getters y Setters
    def get_año(self):
        return self._año

    def set_año(self, nuevo_año):
        if nuevo_año > 1900:
            self._año = nuevo_año


# ============================================
#      HERENCIA: Carro, Moto, Camion
# ============================================

class Carro(Vehiculo):
    def __init__(self, marca, modelo, año, num_puertas):
        super().__init__(marca, modelo, año)
        self.num_puertas = num_puertas

    def descripcion(self):
        return (f"Carro: {self._marca} {self._modelo} - Año: {self._año} "
                f"- Puertas: {self.num_puertas}")


class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, tipo):
        super().__init__(marca, modelo, año)
        self.tipo = tipo

    def descripcion(self):
        return (f"Moto: {self._marca} {self._modelo} - Año: {self._año} "
                f"- Tipo: {self.tipo}")


class Camion(Vehiculo):
    def __init__(self, marca, modelo, año, capacidad_toneladas):
        super().__init__(marca, modelo, año)
        self.capacidad = capacidad_toneladas

    def descripcion(self):
        return (f"Camión: {self._marca} {self._modelo} - Año: {self._año} "
                f"- Capacidad: {self.capacidad} toneladas")


# ============================================
#      PROGRAMA PRINCIPAL
# ============================================

v1 = Vehiculo("Toyota", "Corolla", 2010)
c1 = Carro("Chevrolet", "Onix", 2022, 4)
m1 = Moto("Yamaha", "R3", 2019, "Deportiva")
ca1 = Camion("Volvo", "FH", 2018, 25)

print(v1.descripcion())
print(c1.descripcion())
print(m1.descripcion())
print(ca1.descripcion())

# Probando encapsulación
v1.set_año(2015)
print(v1.descripcion())
