class ProductoNoEncontradoError(Exception):
    def __init__(self, mensaje="Producto no encontrado"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class CantidadInvalidaError(Exception):
    def __init__(self, mensaje="La cantidad debe ser mayor a 0"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class CarritoVacioError(Exception):
    def __init__(self, mensaje="El carrito está vacío"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class ArchivoError(Exception):
    def __init__(self, mensaje="Error al operar con el archivo"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
