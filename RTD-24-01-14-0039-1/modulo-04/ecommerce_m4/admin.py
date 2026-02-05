from usuario import Usuario
from catalogo_clase import Catalogo
from carrito_clase import Carrito
from excepciones import ProductoNoEncontradoError, ArchivoError


class Admin(Usuario):
    def __init__(self, nombre: str = "Administrador"):
        super().__init__(nombre)

    def mostrar_menu(self) -> None:
        print("\n" + "=" * 60)
        print("👨‍💼 MENÚ ADMINISTRADOR".center(60))
        print("=" * 60)
        print("\033[38;5;34m1) Listar productos del catálogo\033[0m")
        print("\033[38;5;82m2) Crear nuevo producto\033[0m")
        print("\033[35m3) Actualizar producto\033[0m")
        print("\033[34m4) Eliminar producto\033[0m")
        print("\033[33m5) Guardar catálogo en archivo\033[0m")
        print("\033[31m0) Salir\n\033[0m")

    def ejecutar_opcion(
        self, opcion: int, catalogo: Catalogo, carrito: Carrito = None
    ) -> bool:
        try:
            if opcion == 0:
                print("👋 ¡Hasta luego, Administrador!")
                return False

            elif opcion == 1:
                catalogo.listar_productos()

            elif opcion == 2:
                self._crear_producto(catalogo)

            elif opcion == 3:
                self._actualizar_producto(catalogo)

            elif opcion == 4:
                self._eliminar_producto(catalogo)

            elif opcion == 5:
                catalogo.guardar_catalogo()

            else:
                print("Opción inválida")

            return True

        except (ProductoNoEncontradoError, ArchivoError) as e:
            print(f"Error: {e}")
            return True
        except Exception as e:
            print(f"Error inesperado: {e}")
            return True

    def _crear_producto(self, catalogo: Catalogo) -> None:
        print("\n--- Crear Nuevo Producto ---")
        nombre = input("Nombre del producto: ").strip()

        if not nombre:
            print("El nombre no puede estar vacío")
            return

        categoria = input("Categoría del producto: ").strip()

        if not categoria:
            print("La categoría no puede estar vacía")
            return

        try:
            precio = float(input("Precio del producto: ").strip())
            if precio <= 0:
                print("El precio debe ser mayor a 0")
                return

            catalogo.crear_producto(nombre, categoria, precio)

        except ValueError:
            print("El precio debe ser un número válido")

    def _actualizar_producto(self, catalogo: Catalogo) -> None:
        print("\n--- Actualizar Producto ---")
        catalogo.listar_productos()

        try:
            id_producto = int(input("\nIngrese ID del producto a actualizar: "))
            producto = catalogo.buscar_por_id(id_producto)

            print(f"\nProducto actual: {producto}")
            print("(Presione Enter para mantener el valor actual)")

            nombre = input(f"Nuevo nombre [{producto.nombre}]: ").strip()
            categoria = input(f"Nueva categoría [{producto.categoria}]: ").strip()
            precio_str = input(f"Nuevo precio [{producto.precio}]: ").strip()

            nuevo_precio = None
            if precio_str:
                try:
                    nuevo_precio = float(precio_str)
                    if nuevo_precio <= 0:
                        print(
                            "El precio debe ser mayor a 0. No se actualizará el precio."
                        )
                        nuevo_precio = None
                except ValueError:
                    print("Precio inválido. No se actualizará el precio.")
                    nuevo_precio = None

            catalogo.actualizar_producto(
                id_producto,
                nombre if nombre else None,
                categoria if categoria else None,
                nuevo_precio,
            )

        except ValueError:
            print("ID inválido")
        except ProductoNoEncontradoError as e:
            print(f"{e}")

    def _eliminar_producto(self, catalogo: Catalogo) -> None:
        print("\n--- Eliminar Producto ---")
        catalogo.listar_productos()

        try:
            id_producto = int(input("\nIngrese ID del producto a eliminar: "))
            confirmacion = input(
                f"¿Está seguro de eliminar el producto ID {id_producto}? (s/n): "
            )

            if confirmacion.lower() == "s":
                catalogo.eliminar_producto(id_producto)
            else:
                print("Eliminación cancelada")

        except ValueError:
            print("ID inválido")
        except ProductoNoEncontradoError as e:
            print(f"{e}")
