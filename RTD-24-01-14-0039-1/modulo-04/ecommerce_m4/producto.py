class Producto:
    def __init__(self, id: int, nombre: str, categoria: str, precio: float):
        self.id = id
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio

    def __str__(self) -> str:
        return f"ID: {self.id} | {self.nombre} | {self.categoria} | ${self.precio}"

    def __repr__(self) -> str:
        return f"Producto(id={self.id}, nombre='{self.nombre}', categoria='{self.categoria}', precio={self.precio})"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
        }

    def actualizar(
        self, nombre: str = None, categoria: str = None, precio: float = None
    ) -> None:
        if nombre is not None:
            self.nombre = nombre
        if categoria is not None:
            self.categoria = categoria
        if precio is not None:
            self.precio = precio
