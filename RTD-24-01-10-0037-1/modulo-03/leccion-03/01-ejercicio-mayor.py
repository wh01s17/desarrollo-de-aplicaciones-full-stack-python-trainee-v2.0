lista = []
iguales = []

for i in range(1, 4):
    input_user = float(input(f"Ingrese {i}° número: "))
    lista.append(input_user)

mayor = lista[0]

for num in lista:
    if num > mayor:
        mayor = num


print("el mayor es: ", mayor)
