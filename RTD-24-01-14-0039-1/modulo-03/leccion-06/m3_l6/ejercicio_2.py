notas = []

for i in range(1, 6):
    nota = float(input(f"Ingrese la {i}° nota del alumno en escala de 0 a 10:\n"))
    while nota < 0 or nota > 10:
        nota = float(
            input(f"Error, ingrese la {i}° nota del alumno en escala de 0 a 10:\n")
        )

    notas.append(nota)

mayor = max(notas)
menor = min(notas)
promedio = sum(notas) / len(notas)

print("Las notas obtenidas son:")
for n in notas:
    print(n, end=", ")

print(f"\nEl promedio es: {promedio}")
print(f"La nota más baja es: {menor}")
print(f"La nota más alta es: {mayor}")
