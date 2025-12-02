# 1. Presentación de la lista inicial

lista = [1, 2, 3, 4, 5]
print("Lista inicial:", lista)

# 2. Agregar un valor a la lista

lista.append(6)
print("Después de append:", lista)

# 3. Agregar más de un valor a la lista
lista = [1, 2, 3, 4, 5]
lista_2 = [6, 7, 8]
lista.extend(lista_2)

print("Después del extend:", lista)

# 4. Agregar lo solicitado por un usuario
lista = [1, 2, 3, 4]
print("Lista inicial:", lista)

nuevo = int(input("Ingrese un número para agregar: "))
lista.append(nuevo)

print("Lista actualizada:", lista)

# 5. Método de lista clear()
lista = [1, 2, 3, 4, 5]
lista.clear()
print(lista)

# 6. Agregar un item a la lista en un indice especifico
lista = [5, 10, 15, 25]
lista.insert(-1, 20)
print(lista)
