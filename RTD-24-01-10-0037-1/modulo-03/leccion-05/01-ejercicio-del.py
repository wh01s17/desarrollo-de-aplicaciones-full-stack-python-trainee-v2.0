import random

# genera una lista con 10 numeros aleatorios entre 1 y 100
lista = [random.randint(1, 100) for _ in range(10)]
index = 2

print(f"Lista original: {lista}")
print(f"Cantidad de elementos: {len(lista)}")

del lista[index]

print(f"Lista con el {index + 1}° elemento elimidado: {lista}")
print(f"Cantidad de elementos: {len(lista)}")
