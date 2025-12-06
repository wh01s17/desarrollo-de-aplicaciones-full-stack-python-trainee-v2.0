import math

entrada = input("Ingresa números separados por comas: ")

numeros = []
for n in entrada.split(","):
    numero = int(n.strip())
    numeros.append(numero)

# Calcular media
media = sum(numeros) / len(numeros)

# Calcular desviación típica
suma_cuadrados = sum((num - media) ** 2 for num in numeros)

varianza = suma_cuadrados / (len(numeros) - 1)

desviacion = math.sqrt(varianza)

print(f"Media: {media}")
print(f"Desviación típica: {desviacion}")
