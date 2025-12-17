# Composición
class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia


class Rueda:
    def __init__(self, diametro):
        self.diametro = diametro


class Automovil:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

        self.motor = Motor("V6", 300)
        self.ruedas = [Rueda(17) for _ in range(4)]


# Agregación
class MotorAgregacion:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia


class RuedaAgregacion:
    def __init__(self, diametro):
        self.diametro = diametro


class AutomovilAgregacion:
    def __init__(self, marca, modelo, color, motor, ruedas):
        self.marca = marca
        self.modelo = modelo
        self.color = color

        self.motor = motor
        self.ruedas = ruedas


motor = MotorAgregacion("V6", 300)
ruedas = [RuedaAgregacion(17) for _ in range(4)]

auto = AutomovilAgregacion("Toyota", "Supra", "Rojo", motor, ruedas)
