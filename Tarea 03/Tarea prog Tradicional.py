# ============================================
# Programación Tradicional
# Ejemplo: Gestión de una motocicleta
# ============================================

# Definición de variables globales
fuel_tank = 0
distance_traveled = 0
fuel_efficiency = 40  # millas por galón

# Función para llenar el tanque de combustible
def fill_tank(amount):
    global fuel_tank
    fuel_tank += amount

# Función para conducir la motocicleta
def ride(distance):
    global fuel_tank, distance_traveled, fuel_efficiency
    fuel_needed = distance / fuel_efficiency
    if fuel_needed <= fuel_tank:
        fuel_tank -= fuel_needed
        distance_traveled += distance
        print("Riding:", distance, "miles")
    else:
        print("Not enough fuel to ride that far.")

# Uso de las funciones en la programación tradicional
fill_tank(10)
ride(120)

# Imprimir la distancia recorrida y el nivel de combustible restante
print("Distance Traveled (Traditional):", distance_traveled)
print("Fuel Tank (Traditional):", fuel_tank)
