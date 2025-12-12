class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return (self.ancho * 2) + (self.alto * 2)


rect1 = Rectangulo(5, 3)

print(rect1.area())

print(rect1.perimetro())
