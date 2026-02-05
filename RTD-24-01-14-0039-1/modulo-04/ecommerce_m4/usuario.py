from catalogo_clase import Catalogo
from carrito_clase import Carrito


class Usuario:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def mostrar_menu(self) -> None:
        raise NotImplementedError("Este método debe ser implementado por la subclase")

    def ejecutar_opcion(
        self, opcion: int, catalogo: Catalogo, carrito: Carrito = None
    ) -> bool:
        raise NotImplementedError("Este método debe ser implementado por la subclase")
