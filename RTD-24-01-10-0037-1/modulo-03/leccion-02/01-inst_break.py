# Ejemplo de instruccion break
for numero in range(1, 11):
    print(numero)
    if numero == 5:
        print("Se encontró el 5, saliendo del bucle.")
        break

# Ejemplo buscar un número en una lista y detener el ciclo
numeros = [3, 7, 15, 22, 30, 45]
buscado = 22

for n in numeros:
    if n == buscado:
        print("Encotrados: ", n)
        break
    print("Revisando: ", n)

# Detener un while cuando el usuario ingresa "salir"
while True:
    texto = input("Escribe algo interesante (o 'salir' para terminar)")

    if texto == "salir":
        print("Programa finalizado.")
        break
    print("Ingresaste: ", texto)
