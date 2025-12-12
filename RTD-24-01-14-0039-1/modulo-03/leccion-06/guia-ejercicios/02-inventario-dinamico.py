# 2) SIMULADOR DE TIENDA CON INVENTARIO DINÁMICO
# -------------------------------------------------------------
# Usar un diccionario como inventario:
# inventario = {
#     "manzana": 30,
#     "pan": 15,
#     "agua": 50
# }
#
# Tareas:
# 1. Permitir agregar productos con su cantidad.
# 2. Permitir vender productos (restar cantidad), validando que exista y que haya stock suficiente.
# 3. Si la cantidad queda en 0, eliminar automáticamente el producto.
# 4. Mostrar un resumen final del inventario, el total de productos vendidos y el desglose por artículo.


def agregar_productos(inventario: dict):
    producto = input("Ingresa un producto:\n")
    while not producto:
        producto = input("Error, ingresa un producto:\n")

    cantidad = int(input("Ingresa cantidad del procucto:\n"))
    while cantidad < 1:
        cantidad = input("Error, ingresa una cantidad válida:\n")

    if inventario.get(producto, False):
        inventario[producto] += cantidad
    else:
        inventario[producto] = cantidad


def mostrar_productos(inventario: dict):
    for k, v in inventario.items():
        print(f"hay {v} del producto {k}")


def check_productos(inventario: dict, producto: str):
    productos = inventario.keys()
    return producto in productos


def check_cantidad(inventario: dict, cantidad: int, producto: str):
    cantidad_producto = inventario[producto]
    return cantidad_producto >= cantidad


def eliminar_producto(inventario: dict, producto: str):
    if inventario[producto] == 0:
        inventario.pop(producto)
        print(f"se vendieron todos los productos de {producto}")


def vender_producto(inventario: dict):
    if inventario:
        mostrar_productos(inventario)
        producto = input("Ingresa un producto:\n")
        while not producto:
            producto = input("Error, ingresa un producto:\n")

        cantidad = int(input("Ingresa cantidad del procucto:\n"))
        while cantidad < 1:
            cantidad = input("Error, ingresa una cantidad válida:\n")

        if check_productos(inventario, producto) and check_cantidad(
            inventario, cantidad, producto
        ):
            inventario[producto] -= cantidad
            print(f"Compraste {cantidad} de {producto}")
            eliminar_producto(inventario, producto)
        else:
            print(
                "No se puede vender la cantidad deseada porque no existe el producto o quieres comprar mas de lo que hay"
            )
    else:
        print("No hay productos disponibles")


inventario = {}

while True:
    opcion = input(
        "Presiona enter para salir o 1 para agregar productos, 2 para comprar:\n"
    )

    if not opcion:
        break
    elif opcion == "1":
        agregar_productos(inventario)
    elif opcion == "2":
        vender_producto(inventario)

print(inventario)
