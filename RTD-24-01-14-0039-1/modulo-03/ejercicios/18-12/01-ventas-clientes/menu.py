import ventas as vt


def menu_principal() -> int:
    """
    Funcion que muestra el menu principal y devuelve la opcion elegida

    :return: Description
    :rtype: int
    """
    print("""
Menú principal:
1. Registrar cliente
2. Registrar venta
3. Ver ventas totales
4. Ver ventas por cliente
5. Ver medio de pago más utilizado
6. Salir
""")
    return pedir_opcion(6)


def medio_de_pago(medios: list) -> str:
    print("Métodos de pago:")
    for i, m in enumerate(medios, start=1):
        print(f"{i} - {m}")

    opcion = pedir_opcion(len(medios))
    return medios[opcion - 1]


def pedir_opcion(max_opcion: int) -> int:
    """
    Funcion que pide un ingreso de una opcion y valida que sea numerico y este en el rango definido

    :param max_opcion: Description
    :type max_opcion: int
    :return: Description
    :rtype: int
    """
    while True:
        opcion = input("Ingrese una opción:\n")

        if not vt.validar_numerico(opcion):
            print("Error: debe ingresar un número")
            continue

        opcion = int(opcion)

        if opcion < 1 or opcion > max_opcion:
            print("Error: opción fuera de rango")
            continue

        return opcion
