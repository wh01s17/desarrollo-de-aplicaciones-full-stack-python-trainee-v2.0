def menu_principal() -> int:
    """
    Función que muestra el menu principal de la aplicación y retorna un int con la opción seleccionada

    :return: Description
    :rtype: int
    """
    print("\033[38;5;34m1) Ver catálogo de productos\033[0m")
    print("\033[38;5;82m2) Buscar producto por nombre o categoría\033[0m")
    print("\033[35m3) Agregar producto al carrito\033[0m")
    print("\033[34m4) Ver carrito y total\033[0m")
    print("\033[33m5) Vaciar carrito\033[0m")
    print("\033[31m0) Salir\n\033[0m")

    return pedir_opcion(0, 5, "Ingrese una opción")


def pedir_opcion(min_opcion: int, max_opcion: int, mensaje: str) -> int:
    """
    Función que pide un ingreso de una opción y valida que sea numérico y esté en el rango definido

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

        if not validar_numerico(opcion, min_opcion):
            print("Error: debe ingresar un número")
            continue

        opcion = int(opcion)

        if opcion < min_opcion or opcion > max_opcion:
            print("Error: opción fuera de rango")
            continue

        return opcion


def validar_numerico(monto: str, min_num: int) -> bool:
    """
    Función que valida si un string es numérico y mayor a 0

    :param monto: Description
    :type monto: str
    :return: Description
    :rtype: bool
    """
    if monto.isnumeric():
        if int(monto) >= min_num:
            return True

    return False
