"""
Ejercicio 4
Escribir un programa que pregunte el nombre de un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con 3 dígitos y el coste total con 8 dígitos enteros y 2 decimales.
"""

nombre_producto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese precio del producto: $"))
unidades = int(input("Ingrese cantidad de unidades: "))

total = precio * unidades

print("Nombre producto:", nombre_producto)
print(f"Precio unitario: {precio:09.2f}")
print(f"Unidades: {unidades:03d}")
print(f"Coste total: {total:011.2f}")
