from usuario import Usuario
from catalogo_clase import Catalogo
from carrito_clase import Carrito
from excepciones import (
    ProductoNoEncontradoError,
    CantidadInvalidaError,
    CarritoVacioError,
    ArchivoError,
)


class Cliente(Usuario):
    def __init__(self, nombre: str = "Cliente"):
        super().__init__(nombre)

    def mostrar_menu(self) -> None:
        print("\n" + "=" * 60)
        print("👤 MENÚ CLIENTE".center(60))
        print("=" * 60)
        print("\033[38;5;34m1) Ver catálogo de productos\033[0m")
        print("\033[38;5;82m2) Buscar producto por nombre o categoría\033[0m")
        print("\033[35m3) Agregar producto al carrito\033[0m")
        print("\033[34m4) Ver carrito y total\033[0m")
        print("\033[36m5) Confirmar compra\033[0m")
        print("\033[33m6) Vaciar carrito\033[0m")
        print("\033[31m0) Salir\n\033[0m")

    def ejecutar_opcion(
        self, opcion: int, catalogo: Catalogo, carrito: Carrito
    ) -> bool:
        try:
            if opcion == 0:
                print("👋 ¡Hasta luego! Gracias por visitarnos.")
                return False

            elif opcion == 1:
                catalogo.listar_productos()

            elif opcion == 2:
                self._buscar_producto(catalogo)

            elif opcion == 3:
                self._agregar_al_carrito(catalogo, carrito)

            elif opcion == 4:
                carrito.ver_carrito()

            elif opcion == 5:
                carrito.confirmar_compra()

            elif opcion == 6:
                carrito.vaciar_carrito()

            else:
                print("Opción inválida")

            return True

        except (
            ProductoNoEncontradoError,
            CantidadInvalidaError,
            CarritoVacioError,
            ArchivoError,
        ) as e:
            print(f"{e}")
            return True
        except Exception as e:
            print(f"Error inesperado: {e}")
            return True

    def _buscar_producto(self, catalogo: Catalogo) -> None:
        filtro = input("\nIngrese producto o categoría a buscar: ").strip()

        if not filtro:
            print("Debe ingresar un texto para buscar")
            return

        resultados = catalogo.buscar_productos(filtro)

        if resultados:
            print(f"\n🔍 Se encontraron {len(resultados)} coincidencia(s):")
            print("-" * 60)
            for producto in resultados:
                print(f"ID: {producto.id}")
                print(f"Producto: {producto.nombre}")
                print(f"Categoría: {producto.categoria}")
                print(f"Precio: ${producto.precio}")
                print("-" * 60)
        else:
            print("No se encontraron productos con ese criterio")

    def _agregar_al_carrito(self, catalogo: Catalogo, carrito: Carrito) -> None:
        catalogo.listar_productos()

        try:
            id_producto = int(input("\nIngrese ID del producto: "))
            producto = catalogo.buscar_por_id(id_producto)

            cantidad = int(input("Ingrese cantidad (1-99): "))

            if cantidad < 1 or cantidad > 99:
                raise CantidadInvalidaError("La cantidad debe estar entre 1 y 99")

            carrito.agregar_producto(producto, cantidad)

        except ValueError:
            print("Debe ingresar números válidos")
        except (ProductoNoEncontradoError, CantidadInvalidaError) as e:
            print(f"{e}")
