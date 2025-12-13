# ============================================
# PROGRAMACIÓN TRADICIONAL
# Cálculo del promedio semanal del clima
# ============================================

# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    print("Ingrese las temperaturas de los 7 días:")

    for dia in range(1, 8):
        temp = float(input(f"Día {dia}: "))
        temperaturas.append(temp)

    return temperaturas


# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio


# Programa principal
def main():
    temperaturas_semana = ingresar_temperaturas()
    promedio_semanal = calcular_promedio(temperaturas_semana)

    print("\nTemperaturas ingresadas:", temperaturas_semana)
    print("Promedio semanal del clima:", round(promedio_semanal, 2), "°C")


# Ejecución del programa
main()
