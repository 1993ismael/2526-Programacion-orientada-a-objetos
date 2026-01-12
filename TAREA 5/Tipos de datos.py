"""
Programa: Conversor de temperatura
Descripción: Convierte grados Celsius a grados Fahrenheit.
Autor: Ismael
"""

# Solicitar el nombre del usuario (string)
nombre_usuario = input("Ingrese su nombre: ")

# Solicitar temperatura en Celsius (float)
temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# Conversión de Celsius a Fahrenheit
temperatura_fahrenheit = (temperatura_celsius * 9 / 5) + 32

# Verificar si la temperatura es mayor a cero (boolean)
es_temperatura_positiva = temperatura_celsius > 0

# Mostrar resultados
print("\n--- Resultado ---")
print(f"Usuario: {nombre_usuario}")
print(f"Temperatura en Celsius: {temperatura_celsius} °C")
print(f"Temperatura en Fahrenheit: {temperatura_fahrenheit} °F")

# Mostrar validación
print(f"¿La temperatura es mayor a 0°C?: {es_temperatura_positiva}")
