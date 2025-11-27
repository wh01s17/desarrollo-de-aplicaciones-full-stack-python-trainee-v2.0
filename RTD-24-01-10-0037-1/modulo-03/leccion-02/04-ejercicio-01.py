"""
Ejercicio 1: Crear una “tupla” que contenga los nombres de los meses del año. El usuario deberá ingresar números al azar entre 1 y 12.  Sin embargo, si ingresa números fuera de este rango, el programa deberá indicarle que solo se aceptan entre 1 y 12 y continuar con su ejecución.

Según el numero ingresado el programa imprimirá por pantalla el mes correspondiente (ej: ingresa  “1”, imprime  “enero”).

Utilice  ciclo “while” y condicionales.
"""

meses = (
    "enero",
    "febrero",
    "marzo",
    "abril",
    "mayo",
    "junio",
    "julio",
    "agosto",
    "septiembre",
    "octubre",
    "noviembre",
    "diciembre",
)

while True:
    try:
        mes = int(input("Ingrese el número de un mes del año (1 al 12)"))

        if mes < 1 or mes > 12:
            print("Mes inválido, ingrese nuevamente")
        else:
            print(meses[mes - 1])
    except ValueError:
        print("Debe ingresar un número")
