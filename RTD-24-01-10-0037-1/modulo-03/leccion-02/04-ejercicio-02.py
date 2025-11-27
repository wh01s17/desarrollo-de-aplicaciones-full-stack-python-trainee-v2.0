"""
EJERCICIO PRÁCTICO 2:

Crear un programa Python donde se le solicite por pantalla al usuario ingresar un número y se debe almacenar la correspondiente tabla de multiplicar hasta el 10 en una lista  e imprimirla.  Utilice ciclo “for”.

Ej: el usuario ingresa el número 5 y el programa imprimirá la lista con la tabla, en este caso, del número 5 (5,10,15,20,25,30,35,40,45,50).
"""

tablas = []
try:
    input_user = int(input("Ingrese la tabla de multiplicar a mostrar: "))

    while input_user < 1:
        print("Debe ingresar un número válido")
        input_user = int(input("Reingrese: "))

    for i in range(1, 11):
        tablas.append(f"{input_user} x {i} = {input_user * i}")

    for num in tablas:
        print(num)

except ValueError:
    print("Debe ingresar un número")
