import menu


def registrar_reserva(reservas: dict, salas: list):
    """
    Funcion para retgistrar reservas

    :param reservas: Description
    :type reservas: dict
    :param salas: Description
    :type salas: list
    """

    sala = menu.mostrar_salas(salas)
    usuario = input("Ingrese nombre del usuario: ")

    hora = int(input("Ingrese hora (8 a 20): "))
    while hora < 8 or hora > 20 or existe_reserva(reservas, sala, hora):
        if hora < 8 or hora > 20:
            print("Hora fuera de rango.")
        else:
            print(f"Ya existe una reserva en {sala} a las {hora} hrs.")
        hora = int(input("Ingrese hora (8 a 20): "))

    reservas[sala].append({"usuario": usuario, "hora": hora})
    print("Reserva registrada con éxito.\n")


def existe_reserva(reservas: dict, sala: str, hora: int):
    """
    Funcion para comprobar si existe la reserva

    :param reservas: Description
    :type reservas: dict
    :param sala: Description
    :type sala: str
    :param hora: Description
    :type hora: int
    """
    for reserva in reservas[sala]:
        if reserva["hora"] == hora:
            return True
    return False


def mostrar_reservas(reservas: dict):
    """
    Funcion que muestra las reservas por sala

    :param reservas: Description
    :type reservas: dict
    """
    for sala, lista in reservas.items():
        print(f"\n{sala}:")
        if not lista:
            print("  Sin reservas")
        else:
            lista.sort(key=lambda reserva: reserva["hora"])

            for reserva in lista:
                print(f"  {reserva['hora']} hrs - {reserva['usuario']}")
    print()
