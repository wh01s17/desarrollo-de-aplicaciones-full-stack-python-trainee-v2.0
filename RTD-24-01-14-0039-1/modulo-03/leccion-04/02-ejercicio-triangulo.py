altura = int(input("Ingrese un número entero positivo para la altura del triángulo: "))

# Triangulo rectangulo
for i in range(1, altura + 1):
    print("*" * i)

print("\n")

# Triangulo "equilatero" opcion 1
for i in range(1, altura + 1):
    espacios = altura - i
    cant_estrellas = i * 2 - 1
    linea = (" " * espacios) + ("*" * cant_estrellas)
    print(linea)

print("\n")

# Triangulo "equilatero" opcion 2
for i in range(1, altura + 1):
    cant_estrellas = i * 2 - 1
    linea = ("*" * cant_estrellas).center(altura * 2)
    print(linea)

print("\n")

# Pino navidad
# Parte superior del pino (el triángulo de hojas)
# El range va de 1 a 29, incrementando de 2 en 2 para generar solo números impares:
# 1, 3, 5, 7, ..., 29
# Cada línea imprime una cantidad de '^' centradas a lo ancho de 30 caracteres.
for i in range(1, 30, 2):
    print(("^" * i).center(30))


# Tronco del pino (3 líneas)
# Se imprime "|||" centrado, simulando el tronco del árbol.
for leg in range(3):
    print(("|||").center(30))

# Base del pino
# Se usa "\\" para imprimir una sola barra invertida y evitar el warning de escape.
print(("\\_____/").center(30))

# Línea separadora decorativa
print(" " + 30 * "-")
print(" (****) ¡Feliz Navidad! (****)")
