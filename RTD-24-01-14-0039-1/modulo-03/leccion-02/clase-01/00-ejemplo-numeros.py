"""
Van a generar un sript que le pregunte al usuario su edad y
le muestre cuantos años va a tener el 2035, independiente del años en el que encuentres
"""

# Algoritmo = Una serie de pasos o procedimientos para resolver una tarea

# Entrada
edad = int(input("Hola! indicame tu edad: "))
fecha_actual = 2025

# Proceso o procesos
# Calcular la edad de la persona en el 2035
edad_futura = (2035 - fecha_actual) + edad

# Salida
# la edad de la persona el 2035
print(edad_futura)
