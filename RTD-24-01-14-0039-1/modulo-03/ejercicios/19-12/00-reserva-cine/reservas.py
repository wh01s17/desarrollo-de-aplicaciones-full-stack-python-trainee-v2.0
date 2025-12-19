import peliculas as pl
import menu


def crear_reserva(peliculas: list, reservas: list) -> None:
    """
    Funcion que crea una reserva

    :param peliculas: Description
    :type peliculas: list
    :param reservas: Description
    :type reservas: list
    """
    pl.mostrar_cartelera(peliculas)
    id_pelicula = menu.pedir_opcion(0, len(peliculas), "\nIngrese ID de pelicula")

    resultado = pl.buscar_id(peliculas, id_pelicula)

    if not resultado:
        print("No existe el ID ingresado")
        return

    cantidad = menu.pedir_opcion(1, 99, "\nIngrese cantidad de entradas (1 a 99)")

    resultado["cantidad"] = cantidad
    resultado["subtotal"] = resultado["valor_unitario"] * cantidad

    reservas.append(resultado)

    print("Reserva ingresada correctamente")


def listar_reservas(reservas: list) -> None:
    """
    Funcion que retorna todas las reservas

    :param reservas: Description
    :type reservas: list
    """
    for i, reserva in enumerate(reservas, start=1):
        print("----------------------------")
        print(f"Reserva N° {i}")
        print(f"ID: {reserva['id']}")
        print(f"Titulo: {reserva['titulo']}")
        print(f"Cantidad: {reserva['cantidad']}")
        print(f"Valor unitario: ${reserva['valor_unitario']}")
        print(f"Subtotal: ${reserva['subtotal']}")
        print("----------------------------\n")

    print("Total de ventas: ", total_ventas(reservas))


def total_ventas(reservas: list) -> int:
    """
    Funcion que retorna el total de ventas

    :param reservas: Description
    :type reservas: list
    :return: Description
    :rtype: int
    """
    suma = 0
    for reserva in reservas:
        suma += reserva["subtotal"]
    return suma


def cancelar_reservas(reservas: list) -> None:
    """
    Funcion que elimina todas las reservas

    :param reservas: Description
    :type reservas: list
    """
    reservas.clear()
    print("Se cancelaron todas las reservas")
