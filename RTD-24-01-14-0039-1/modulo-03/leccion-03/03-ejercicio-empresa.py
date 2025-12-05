edad = int(input("Ingrese su edad: "))

if edad < 4:
    print("Entrada gratis")
elif edad <= 18:
    print("Valor de entrada $5")
else:
    print("Valor de entrada $10")
