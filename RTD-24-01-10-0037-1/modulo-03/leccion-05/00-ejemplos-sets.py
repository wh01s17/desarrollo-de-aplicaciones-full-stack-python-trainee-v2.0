# Sets - Presentación básica
s = {1, 2, 3}
print(s)

# 2. Añadir un valor a set
s = {1, 2, 3}
s.add(4)
print(s)

s = {1, 2, 3}
s.add(4)
s.add(3)
print(s)

# 3. Eliminar un valor del conjunto
s = {1, 2, 3}
s.remove(3)
print(s)

# 4.Eliminar sin error si no existe
s = {1, 2, 3}

s.discard(2)
s.discard(10)
print(s)

# 5. Crear una copia del conjunto
s = {1, 2, 3, 4}
s2 = s.copy()
print(s, s2)

# 6. Eliminar todos los elementos de un conjunto
s = {1, 2, 3, 4}
s.clear()
print(s)
