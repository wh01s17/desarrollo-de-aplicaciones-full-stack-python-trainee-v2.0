from datetime import datetime
from producto import Producto
from excepciones import CantidadInvalidaError, CarritoVacioError, ArchivoError


class ItemCarrito:
    def __init__(self, producto: Producto, cantidad: int):
        if cantidad <= 0:
            raise CantidadInvalidaError("La cantidad debe ser mayor a 0")

        self.producto = producto
        self.cantidad = cantidad
        self.subtotal = producto.precio * cantidad

    def __str__(self) -> str:
        return (
            f"{self.producto.nombre} x{self.cantidad} "
            f"(${self.producto.precio} c/u) = ${self.subtotal}"
        )


class Carrito:
    def __init__(self):
        self.items = []

    def agregar_producto(self, producto: Producto, cantidad: int) -> None:
        for item in self.items:
            if item.producto.id == producto.id:
                item.cantidad += cantidad
                item.subtotal = item.producto.precio * item.cantidad
                print(
                    f"✅ Cantidad actualizada: {producto.nombre} (Total: {item.cantidad} unidades)"
                )
                return

        nuevo_item = ItemCarrito(producto, cantidad)
        self.items.append(nuevo_item)
        print(f"✅ Producto agregado al carrito: {producto.nombre} x{cantidad}")

    def ver_carrito(self) -> None:
        if not self.items:
            raise CarritoVacioError("El carrito está vacío 🛒")

        print("\n" + "=" * 60)
        print("🛒 MI CARRITO".center(60))
        print("=" * 60)

        total = 0
        for item in self.items:
            print("-" * 60)
            print(f"ID: {item.producto.id}")
            print(f"Nombre: {item.producto.nombre}")
            print(f"Cantidad: {item.cantidad}")
            print(f"Precio Unitario: ${item.producto.precio}")
            print(f"Subtotal: ${item.subtotal}")
            total += item.subtotal

        print("-" * 60)
        print(f"💰 TOTAL A PAGAR: ${total}")
        print("=" * 60)

    def calcular_total(self) -> float:
        return sum(item.subtotal for item in self.items)

    def vaciar_carrito(self) -> None:
        self.items.clear()
        print("🗑️  Carrito vaciado")

    def confirmar_compra(self, nombre_archivo: str = "ordenes.txt") -> None:
        if not self.items:
            raise CarritoVacioError(
                "No se puede confirmar la compra. El carrito está vacío."
            )

        try:
            fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            total = self.calcular_total()

            with open(nombre_archivo, "a", encoding="utf-8") as archivo:
                archivo.write("=" * 70 + "\n")
                archivo.write(f"ORDEN DE COMPRA - {fecha_hora}\n")
                archivo.write("=" * 70 + "\n")

                for item in self.items:
                    archivo.write(
                        f"  • {item.producto.nombre} x{item.cantidad} "
                        f"(${item.producto.precio} c/u) = ${item.subtotal}\n"
                    )

                archivo.write("-" * 70 + "\n")
                archivo.write(f"TOTAL: ${total}\n")
                archivo.write("=" * 70 + "\n\n")

            print("\n" + "=" * 60)
            print("✅ ¡COMPRA CONFIRMADA!".center(60))
            print("=" * 60)
            print(f"Fecha: {fecha_hora}")
            print(f"Total pagado: ${total}")
            print(f"Orden guardada en: {nombre_archivo}")
            print("=" * 60)

            self.vaciar_carrito()

        except IOError as e:
            raise ArchivoError(f"Error al guardar la orden: {str(e)}")

    def esta_vacio(self) -> bool:
        return len(self.items) == 0
