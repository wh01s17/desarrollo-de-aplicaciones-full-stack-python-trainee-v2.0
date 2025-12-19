def registrar_cliente(clientes: dict) -> None:
    """
    Funcion para registrar un cliente

    :param clientes: Description
    :type clientes: dict
    """
    rut = input("Ingrese RUT:\n")

    if not check_rut(rut):
        print("RUT no válido")
        return

    if rut in clientes.keys():
        print("El RUT ingresado ya se encuentra en la base de datos")
        return

    nombre = input("Ingrese nombre:\n")
    while not nombre:
        nombre = input("Error, ingrese nombre:\n")

    clientes[rut] = nombre


def check_rut(rut: str) -> bool:
    """
    Funcion que checkea si el rut tiene el formato adecuado

    :param rut: Description
    :type rut: str
    :return: Description
    :rtype: bool
    """

    tiene_guion = "-" in rut
    largo_rut = len(rut) >= 9

    if tiene_guion and largo_rut:
        return True

    return False
