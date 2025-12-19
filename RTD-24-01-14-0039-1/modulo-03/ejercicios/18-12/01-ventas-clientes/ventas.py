import menu


def registrar_venta(clientes: dict, ventas: list, medios: list) -> None:
    """
    Funcion que permite registrar una venta, asociada a un RUT de un cliente

    :param clientes: Description
    :type clientes: dict
    :param ventas: Description
    :type ventas: list
    :param medios: Description
    :type medios: list
    """
    rut = input("Ingrese RUT de cliente:\n")

    if rut not in clientes.keys():
        print("No existe el cliente ingresado")
        return

    venta = input("Ingrese monto de la venta:\n")
    while not validar_numerico(venta):
        venta = input("Error, ingrese monto de la venta:\n")

    monto = int(venta)
    medio_de_pago = menu.medio_de_pago(medios)

    for registro in ventas:
        if rut in registro:
            registro[rut].append({"monto": monto, "medio_pago": medio_de_pago})
            print(f"Venta registrada en cliente {rut}")
            return

    ventas.append({rut: [{"monto": monto, "medio_pago": medio_de_pago}]})
    print(f"Venta registrada en nuevo cliente {rut}")


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
