# =================================================
# EJERCICIO 2: SISTEMA DE PEDIDOS
# Tema: COLABORACIÓN ENTRE CLASES
# =================================================

# CONTEXTO:
# Se desea modelar un sistema de pedidos para una tienda.
# Un Pedido trabaja con un Cliente y varios Productos.

# IMPORTANTE:
# - Cliente y Producto pueden existir de forma independiente.
# - Pedido solo USA estas clases.
# Esto es un ejemplo de COLABORACIÓN.

# 1) Crea la clase Producto
# Atributos:
# - nombre
# - precio

# Métodos:
# - mostrar_info()


class Producto:
    def __init__(self, nombre: str, precio: int) -> None:
        self.nombre = nombre
        self.precio = precio

    def mostrar_info(self) -> None:
        print(f"\nProducto: {self.nombre}")
        print(f"Precio: ${self.precio}")


# 2) Crea la clase Cliente
# Atributos:
# - nombre

# Métodos:
# - mostrar_info()


class Cliente:
    def __init__(self, nombre: str) -> None:
        self.nombre = nombre

    def mostrar_info(self) -> None:
        print(f"Cliente: {self.nombre}")


# 3) Crea la clase Pedido
# Atributos:
# - cliente (instancia de Cliente)
# - productos (lista de Producto)

# Métodos:
# - agregar_producto(producto)
# - calcular_total()
# - mostrar_resumen()


class Pedido:
    def __init__(self, cliente: Cliente) -> None:
        self.cliente = cliente
        self.productos: list[Producto] = []

    def agregar_producto(self, producto: Producto) -> None:
        self.productos.append(producto)

    def calcular_total(self) -> int:
        return sum([p.precio for p in self.productos])

    def mostrar_resumen(self) -> None:
        print("\nDatos de pedido")
        print("---------------")
        self.cliente.mostrar_info()
        for p in self.productos:
            p.mostrar_info()

        print(f"\nTotal: ${self.calcular_total()}")


# 4) PRUEBAS (descomenta cuando tengas tu solución)

producto1 = Producto("Teclado", 15000)
producto2 = Producto("Mouse", 8000)

cliente1 = Cliente("María González")

pedido1 = Pedido(cliente1)
pedido1.agregar_producto(producto1)
pedido1.agregar_producto(producto2)

pedido1.mostrar_resumen()
