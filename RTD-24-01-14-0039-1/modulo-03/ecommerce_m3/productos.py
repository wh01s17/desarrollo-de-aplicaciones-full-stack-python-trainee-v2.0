import menu


def mostrar_productos(productos: list) -> None:
    """
    Función que muestra los productos disponibles

    :param productos: Description
    :type productos: list
    """
    for producto in productos:
        print("-" * 25)
        print(f"ID: {producto['id']}")
        print(f"Producto: {producto['nombre']}")
        print(f"Categoría: {producto['categoria']}")
        print(f"${producto['precio']}")
        print("-" * 25)


def buscar_producto(productos: list) -> None:
    """
    Función que busca y muestra todas las coincidencias en el listado de productos, según el filtro ingresado

    :param productos: Description
    :type productos: list
    """
    filtro = input("Ingrese producto o categoria:\n").strip().lower()

    while not filtro:
        print("Error, entrada inválida")
        filtro = input("Ingrese producto o categoria:\n")

    resultados = []

    for producto in productos:
        if (
            filtro in producto["nombre"].lower()
            or filtro in producto["categoria"].lower()
        ):
            resultados.append(producto)

    if resultados:
        print(f"\n🔍Coincidencias: {len(resultados)}")
        mostrar_productos(resultados)
    else:
        print("No existe el producto ingresado")


def buscar_id(productos: list) -> dict | None:
    """
    Función que busca y retorna un diccionario con el producto según la ID ingresada

    :param productos: Description
    :type productos: list
    :return: Description
    :rtype: dict | None
    """
    id_producto = menu.pedir_opcion(
        1, max(p["id"] for p in productos), "Ingrese ID del procucto"
    )

    for producto in productos:
        if id_producto == producto["id"]:
            return producto

    return None
