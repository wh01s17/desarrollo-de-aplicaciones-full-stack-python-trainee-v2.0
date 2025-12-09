meses = [
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
]

dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

num = int(input("Ingrese un número de mes entre 1 y 12:\n"))

while num < 1 or num > 12:
    num = int(input("Mes inválido, ingrese un número de mes entre 1 y 12:\n"))

print(f"El mes es {meses[num - 1]} y tiene {dias[num - 1]} días.")
