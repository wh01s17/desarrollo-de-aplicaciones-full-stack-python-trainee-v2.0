def mostrar_menu():
    """
    Funcion para mostrar el menu principal de la aplicación y devuelve la opcion elegida como int
    """

    print("Salas de reuniones")
    print("1 - Crear reserva")
    print("2 - Listar reservas")
    print("3 - Salir")
    opcion = int(input("Seleccione un opción:\n"))

    while opcion < 1 or opcion > 3:
        opcion = int(input("Error, seleccione un opción:\n"))

    return opcion


def mostrar_salas(salas: list):
    """
    Funcion que muestra las salas y devuelve la opcion elegida como str
    """

    for i, sala in enumerate(salas):
        print(f"{i + 1} - {sala}")

    opcion = int(input("Seleccione un opción:\n"))

    while opcion < 1 or opcion > len(salas):
        opcion = int(input("Error, seleccione un opción:\n"))

    return salas[opcion - 1]
