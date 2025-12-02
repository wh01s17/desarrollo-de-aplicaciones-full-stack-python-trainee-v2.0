# 1. Presentación básica de una tupla
t = (1, 2, 3)
print(t)

# 2. Acceder por indice

print("Tupla completa:", t)
print("Primer elemento:", t[0])
print("Último elemento:", t[-1])

# 3. Recorrer con un for
for elemento in t:
    print("Elemento:", elemento)

# 4. Intentar modificar una tupla
print("Original:", t)

try:
    t[0] = 10
except TypeError:
    print("Error: las tuplas son inmutables, no permiten reasignación.")

# 5. Concatenación de tuplas
nueva_tupla = t + (4, 5)
print("Original:", t)
print("Tupla concatenada:", nueva_tupla)

# 6. Multiplicación de tuplas
repetir = t * 3
print("Original:", t)
print("Repetida:", repetir)

# 7. Convertir tupla en lista
lista = list(t)
lista.append(4)

tupla_mod = tuple(lista)

print("Tupla original:", t)
print("Tupla modificada:", tupla_mod)
