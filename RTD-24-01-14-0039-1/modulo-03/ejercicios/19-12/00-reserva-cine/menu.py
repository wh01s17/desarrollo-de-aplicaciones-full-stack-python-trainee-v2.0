def menu_principal():
    print("""
=== Sistema de Reserva de Cine ===
1) Ver cartelera de películas
2) Buscar película por nombre o género
3) Reservar entradas
4) Ver reservas y total acumulado
5) Cancelar todas las reservas
0) Salir
""")
    return pedir_opcion(0, 6, "Ingrese una opción")


def pedir_opcion(min_opcion: int, max_opcion: int, mensaje: str) -> int:
    """
    Funcion que pide un ingreso de una opcion y valida que sea numerico y este en el rango definido

    :param min_opcion: Description
    :type min_opcion: int
    :param max_opcion: Description
    :type max_opcion: int
    :param mensaje: Description
    :type mensaje: str
    :return: Description
    :rtype: int
    """
    while True:
        opcion = input(f"{mensaje}:\n")

        if not validar_numerico(opcion):
            print("Error: debe ingresar un número")
            continue

        opcion = int(opcion)

        if opcion < min_opcion or opcion > max_opcion:
            print("Error: opción fuera de rango")
            continue

        return opcion


def validar_numerico(monto: str) -> bool:
    """
    Funcion que valida si un string es numerico y mayor a 0

    :param monto: Description
    :type monto: str
    :return: Description
    :rtype: bool
    """
    if monto.isnumeric():
        if int(monto) > 0:
            return True

    return False
