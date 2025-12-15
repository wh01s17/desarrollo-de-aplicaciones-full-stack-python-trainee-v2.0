# 5) MINI GESTOR DE BIBLIOTECA
# -------------------------------------------------------------
# La biblioteca parte con esta estructura:
# libros = [
#     {"titulo": "1984", "autor": "George Orwell", "prestado": False},
#     {"titulo": "Fundación", "autor": "Isaac Asimov", "prestado": False},
# ]
#
# Tareas:
# 1. Permitir agregar nuevos libros.
# 2. Permitir marcar un libro como prestado o devuelto.
# 3. Generar una lista de los libros disponibles y otra de los prestados.
# 4. Crear un buscador por título que ignore mayúsculas/minúsculas.
# 5. Mostrar un resumen final con totales y listados.


def pedir_opcion(minimo, maximo):
    opcion = int(input("Seleccione una opción:\n"))
    while opcion < minimo or opcion > maximo:
        opcion = int(input("Error, ingrese una opción válida:\n"))
    return opcion


def agregar_libro(libros: list):
    titulo = input("Ingrese el titulo:\n")
    while not titulo:
        titulo = input("Error, ingrese titulo:\n")

    autor = input("Ingrese el autor:\n")
    while not autor:
        autor = input("Error, ingrese autor:\n")

    libros.append({"titulo": titulo, "autor": autor, "prestado": False})


def estado_libro(libros: list):
    print("1 - Prestar libro")
    print("2 - Devolver libro")
    opcion = pedir_opcion(1, 2)

    prestar = opcion == 1

    libro = buscar_libro(libros)

    if not libro:
        print("No existe el libro ingresado")
        return

    prestado = libro.get("prestado", False)

    if prestar:
        if not prestado:
            libro["prestado"] = True
            print("Libro prestado correctamente")
        else:
            print("Lo sentimos, este título está prestado")
    else:
        if prestado:
            libro["prestado"] = False
            print("Libro devuelto correctamente")
        else:
            print("Este libro no estaba prestado")


def buscar_libro(libros: list):
    titulo = input("Ingrese titulo del libro\n")
    while not titulo:
        titulo = input("Error, ingrese titulo del libro\n")

    for libro in libros:
        if libro.get("titulo").lower() == titulo.lower():
            return libro

    return None


def buscador(libros: list):
    libro = buscar_libro(libros)

    if not libro:
        print("No existe el libro ingresado")
        return

    print(f"{libro.get('titulo')} - escrito por {libro.get('autor')}")


def listar_libros(libros: list):
    disponibles = []
    prestados = []

    for libro in libros:
        if libro.get("prestado"):
            prestados.append(libro)
        else:
            disponibles.append(libro)

    print("Disponibles:", len(disponibles))
    for libro in disponibles:
        print(f"{libro.get('titulo')} - escrito por {libro.get('autor')}")

    print("\nPrestados:", len(prestados))
    for libro in prestados:
        print(f"{libro.get('titulo')} - escrito por {libro.get('autor')}")


libros = [
    {"titulo": "1984", "autor": "George Orwell", "prestado": False},
    {"titulo": "Fundación", "autor": "Isaac Asimov", "prestado": False},
]

pergamino = r"""
(\ 
\'\ 
 \'\     __________  
 / '|   ()_________)
 \ '/    \ ~~~~~~~~ \
   \       \ ~~~~~~   \
   ==).      \__________\
  (__)       ()__________)
"""

while True:
    print('\nBiblioteca "La Iliada"')
    print(pergamino)
    print("1 - Agregar libro")
    print("2 - Prestar/Devolver libro")
    print("3 - Listar libros (disponibles y prestados)")
    print("4 - Buscar libro")
    print("5 - Salir")
    opcion = pedir_opcion(1, 5)

    if opcion == 5:
        listar_libros(libros)
        break

    elif opcion == 1:
        agregar_libro(libros)

    elif opcion == 2:
        estado_libro(libros)

    elif opcion == 3:
        listar_libros(libros)

    elif opcion == 4:
        buscador(libros)
