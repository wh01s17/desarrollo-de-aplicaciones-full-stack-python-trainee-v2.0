def total_ventas(ventas: list) -> None:
    """
    Funcion que entrega cantidad de ventas, monto total de las ventas y promedio de ventas

    :param ventas: Description
    :type ventas: list
    """
    total_monto = 0
    total_ventas = 0

    for registro in ventas:
        for lista_ventas in registro.values():
            for venta in lista_ventas:
                total_monto += venta["monto"]
                total_ventas += 1

    promedio = total_monto / total_ventas if total_ventas > 0 else 0

    print(f"Ventas realizadas: {total_ventas}")
    print(f"Monto total vendido: ${total_monto}")
    print(f"Promedio por venta: ${promedio:.2f}")


def ventas_cliente(ventas: list, clientes: dict) -> None:
    """
    Funcion que muestra todas las ventas asociadas a un RUT de un cliente

    :param ventas: Description
    :type ventas: list
    :param clientes: Description
    :type clientes: dict
    """
    rut = input("Ingrese RUT de cliente:\n")

    if rut not in clientes:
        print("No existe el cliente ingresado")
        return

    for registro in ventas:
        if rut in registro:
            lista_ventas = registro[rut]
            total = 0

            print(f"Cliente: {rut}")
            print(f"Nombre: {clientes[rut]}")
            print(f"Compras realizadas: {len(lista_ventas)}")

            for venta in lista_ventas:
                print(f"${venta['monto']}")
                total += venta["monto"]

            print(f"Total: ${total}")
            return

    print("El cliente no registra ventas")


def mayor_medio_pago(ventas: list, medios: list) -> None:
    """
    Funcion que imprime el medio de pago mas utilizado

    :param ventas: Description
    :type ventas: list
    :param medios: Description
    :type medios: list
    """
    contador = {medio: 0 for medio in medios}

    for registro in ventas:
        for lista_ventas in registro.values():
            for venta in lista_ventas:
                medio = venta["medio_pago"]
                if medio in contador:
                    contador[medio] += 1

    if not any(contador.values()):
        print("No hay ventas registradas")
        return

    medio_mas_usado = max(contador, key=contador.get)

    print("El medio de pago más utilizado es:")
    print(f"{medio_mas_usado} ({contador[medio_mas_usado]} ventas)")
