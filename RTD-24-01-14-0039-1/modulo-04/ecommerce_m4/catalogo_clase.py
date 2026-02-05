from producto import Producto
from excepciones import ProductoNoEncontradoError, ArchivoError


class Catalogo:
    def __init__(self):
        self.productos = []
        self._proximo_id = 1

        import os

        if os.path.exists("catalogo.csv"):
            try:
                self.cargar_catalogo()
            except ArchivoError:
                self._cargar_productos_iniciales()
        else:
            self._cargar_productos_iniciales()

    def _cargar_productos_iniciales(self) -> None:
        productos_iniciales = [
            {"nombre": "Polera", "categoria": "ropa", "precio": 9990},
            {"nombre": "Jeans azul", "categoria": "ropa", "precio": 24990},
            {"nombre": "Zapatillas deportivas", "categoria": "ropa", "precio": 45990},
            {
                "nombre": "Smartphone Android",
                "categoria": "tecnología",
                "precio": 189990,
            },
            {
                "nombre": "Audífonos inalámbricos",
                "categoria": "tecnología",
                "precio": 39990,
            },
            {"nombre": "Teclado mecánico", "categoria": "tecnología", "precio": 69990},
            {"nombre": "Lámpara de escritorio", "categoria": "hogar", "precio": 15990},
            {"nombre": "Set de sábanas", "categoria": "hogar", "precio": 29990},
            {"nombre": "Silla ergonómica", "categoria": "hogar", "precio": 89990},
            {"nombre": "Mochila urbana", "categoria": "ropa", "precio": 34990},
        ]

        for datos in productos_iniciales:
            producto = Producto(
                self._proximo_id,
                datos["nombre"],
                datos["categoria"],
                datos["precio"],
            )
            self.productos.append(producto)
            self._proximo_id += 1

    def listar_productos(self) -> None:
        if not self.productos:
            print("No hay productos en el catálogo")
            return

        print("\n" + "=" * 60)
        print("📦 CATÁLOGO DE PRODUCTOS".center(60))
        print("=" * 60)

        for producto in self.productos:
            print("-" * 60)
            print(f"ID: {producto.id}")
            print(f"Producto: {producto.nombre}")
            print(f"Categoría: {producto.categoria}")
            print(f"Precio: ${producto.precio}")
        print("-" * 60)

    def buscar_por_id(self, id_producto: int) -> Producto:
        for producto in self.productos:
            if producto.id == id_producto:
                return producto

        raise ProductoNoEncontradoError(f"Producto con ID {id_producto} no encontrado")

    def buscar_productos(self, filtro: str) -> list[Producto]:
        filtro_lower = filtro.lower().strip()
        resultados = []

        for producto in self.productos:
            if (
                filtro_lower in producto.nombre.lower()
                or filtro_lower in producto.categoria.lower()
            ):
                resultados.append(producto)

        return resultados

    def crear_producto(self, nombre: str, categoria: str, precio: float) -> Producto:
        nuevo_producto = Producto(self._proximo_id, nombre, categoria, precio)
        self.productos.append(nuevo_producto)
        self._proximo_id += 1
        print(f"✅ Producto '{nombre}' creado exitosamente con ID {nuevo_producto.id}")
        return nuevo_producto

    def actualizar_producto(
        self,
        id_producto: int,
        nombre: str = None,
        categoria: str = None,
        precio: float = None,
    ) -> None:
        producto = self.buscar_por_id(id_producto)
        producto.actualizar(nombre, categoria, precio)
        print(f"✅ Producto ID {id_producto} actualizado exitosamente")

    def eliminar_producto(self, id_producto: int) -> None:
        producto = self.buscar_por_id(id_producto)
        self.productos.remove(producto)
        print(
            f"✅ Producto '{producto.nombre}' (ID {id_producto}) eliminado exitosamente"
        )

    def guardar_catalogo(self, nombre_archivo: str = "catalogo.csv") -> None:
        try:
            with open(nombre_archivo, "w", encoding="utf-8") as archivo:
                archivo.write("ID;NOMBRE;CATEGORIA;PRECIO\n")

                for producto in self.productos:
                    linea = f"{producto.id};{producto.nombre};{producto.categoria};{producto.precio}\n"
                    archivo.write(linea)

            print(f"✅ Catálogo guardado en '{nombre_archivo}' exitosamente")

        except IOError as e:
            raise ArchivoError(f"Error al guardar el catálogo: {str(e)}")

    def cargar_catalogo(self, nombre_archivo: str = "catalogo.csv") -> None:
        try:
            with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                lineas = archivo.readlines()

                if len(lineas) > 1:
                    self.productos = []
                    max_id = 0

                    for linea in lineas[1:]:
                        linea = linea.strip()
                        if linea:
                            partes = linea.split(";")
                            if len(partes) == 4:
                                id_prod = int(partes[0])
                                nombre = partes[1]
                                categoria = partes[2]
                                precio = float(partes[3])

                                producto = Producto(id_prod, nombre, categoria, precio)
                                self.productos.append(producto)

                                if id_prod > max_id:
                                    max_id = id_prod

                    self._proximo_id = max_id + 1
                    print(f"✅ Catálogo cargado desde '{nombre_archivo}' exitosamente")

        except FileNotFoundError:
            pass
        except (IOError, ValueError) as e:
            raise ArchivoError(f"Error al cargar el catálogo: {str(e)}")

    def obtener_max_id(self) -> int:
        if not self.productos:
            return 0
        return max(p.id for p in self.productos)
