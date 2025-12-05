# Tupla
niveles = ("1° Medio", "2° Medio", "3° Medio", "4° Medio")
print("Los cursos de enseñanza media son:", niveles)

# Lista
lista_estudiantes = ["Pedro", "Susana", "Roberto", "Josefa"]
print("La lista inicial de alumnos es:", lista_estudiantes)

# Agregar un alumno a la lista
lista_estudiantes.append("Rocío")
print("La nueva lista de estudiantes está compuesta por:", lista_estudiantes)

# Ordenar la lista
lista_estudiantes.sort()
print("La lista ordenada es:", lista_estudiantes)

# Remover un alumno de la lista
lista_estudiantes.remove("Roberto")
print("La nueva lista queda conformada por:", lista_estudiantes)
print("La cantidad de estudiantes son:", len(lista_estudiantes))


# Set
taller_danza = {"Josefa", "Pedro", "Rocío"}
taller_musica = {"Rocío", "Susana"}

print("Taller de danza:", taller_danza)
print("Taller de música:", taller_musica)

taller_union = taller_danza.union(taller_musica)
print("Unión (al menos un taller):", taller_union)

taller_intersección = taller_danza.intersection(taller_musica)
print("Intersección (ambos talleres):", taller_intersección)


# Diccionario
notas_alumnos = {
    "Josefa": [6.0, 5.5, 6.5],
    "Pedro": [5.0, 4.5, 7.0],
    "Rocío": [6.3, 6.5, 6.8],
    "Susana": [4.8, 6.2, 6.7],
}

print("\nDiccionario de notas:", notas_alumnos)

for nombre, notas in notas_alumnos.items():
    promedio = sum(notas) / len(notas)
    promedio = round(promedio, 1)
    print(f"- {nombre} : notas = {notas}, promedio = {promedio}")
