import math

entrada = input("Ingresa números separados por comas: ")

# Convertir a lista de floats
numeros = []
for n in entrada.split(","):
    numero = float(n.strip())
    numeros.append(numero)

# Calcular media
media = sum(numeros) / len(numeros)

# Calcular desviación típica
suma_cuadrados = 0

for num in numeros:
    suma_cuadrados += (num - media) ** 2

varianza = suma_cuadrados / len(numeros)

desviacion = math.sqrt(varianza)

print(f"Media: {media}")
print(f"Desviación típica: {desviacion}")
