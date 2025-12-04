input_user = int(input("Ingrese un numero entero positivo: "))

# Opcion 1
# Con variable auxiliar num
for i in range(input_user):
    num = i + 1
    if num % 2 == 1:
        print(num, end=",")

print("\n")

# Opcion 2
# Sin variable auxiliar
for i in range(1, input_user + 1):
    if i % 2 == 1:
        print(i, end=",")

print("\n")

# Opcion 3
# Empieza en 1 y suma de 2 en 2
for i in range(1, input_user + 1, 2):
    print(i, end=",")
