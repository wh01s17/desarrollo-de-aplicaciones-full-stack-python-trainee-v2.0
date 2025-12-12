class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}\nPrecio: {self.precio}\nStock: {self.stock}\n")

    def vender(self, cantidad):
        if self.stock >= cantidad:
            print("Venta realizada")
            self.stock -= cantidad
            self.mostrar_info()

        else:
            print("Stock insuficiente")
            self.mostrar_info()


p1 = Producto("Polera", 9990, 5)
p1.mostrar_info()
p1.vender(3)

p2 = Producto("Pantalon", 20990, 2)
p2.mostrar_info()
p2.vender(3)
