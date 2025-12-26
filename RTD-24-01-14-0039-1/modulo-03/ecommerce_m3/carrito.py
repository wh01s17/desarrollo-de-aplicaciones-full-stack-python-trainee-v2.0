import productos as pr
import menu


def agregar_producto(productos: list, carrito: list) -> None:
    """
    Función que permite agregar un producto al carrito

    :param productos: Description
    :type productos: list
    :param carrito: Description
    :type carrito: list
    """
    producto_base = pr.buscar_id(productos)

    if not producto_base:
        print("No se encontró el producto")
        return

    cantidad = menu.pedir_opcion(1, 99, "Ingrese cantidad (1 a 99)")

    item_carrito = {
        "id": producto_base["id"],
        "nombre": producto_base["nombre"],
        "cantidad": cantidad,
        "precio_unitario": producto_base["precio"],
        "subtotal": cantidad * producto_base["precio"],
    }

    carrito.append(item_carrito)
    print("Producto agregado correctamente :D")


def ver_carrito(carrito: list) -> None:
    """
    Función que muestra el carrito

    :param carrito: Description
    :type carrito: list
    """
    if not carrito:
        print("Carrito vacío 🛒\n")
        return

    total = 0

    for item in carrito:
        print("-" * 25)
        print(f"ID: {item['id']}")
        print(f"Nombre: {item['nombre']}")
        print(f"Cantidad: {item['cantidad']}")
        print(f"Precio Unitario: ${item['precio_unitario']}")
        print(f"Subtotal: ${item['subtotal']}")
        total += item["subtotal"]

    print("-" * 25)
    print(f"Total a pagar: ${total}")


def vaciar_carrito(carrito) -> None:
    """
    Función que limpia el carrito

    :param carrito: Description
    """
    carrito.clear()
    print("Carrito eliminado")
