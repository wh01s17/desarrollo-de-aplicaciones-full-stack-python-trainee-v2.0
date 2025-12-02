"""
Ejercicio 3
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
"""

fecha_nac = input("Ingrese su fecha de nacimiento en el formato dd/mm/aaaa: ")

lista = fecha_nac.split("/")

dia = lista[0]
mes = lista[1]
anio = lista[2]

print(f"Día: {dia}")
print(f"Mes: {mes}")
print(f"Año: {anio}")
