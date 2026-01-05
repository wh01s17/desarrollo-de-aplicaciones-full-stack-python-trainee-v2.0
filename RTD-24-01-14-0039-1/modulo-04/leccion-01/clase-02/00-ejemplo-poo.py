class Perro:
    # atributos de clase
    N_COLAS = 1
    N_PATAS = 4

    # atributos de instancia (Metodo constructor)
    def __init__(self, nombre, raza):
        # metodos magicos, double underscore method,  dunder method
        self.nombre = nombre
        self.raza = raza

    # metodos de instancia
    def saludar(self):
        print(f"Hola soy {self.nombre} de raza {self.raza}")

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    # metodos estatico
    @staticmethod
    def ladrar():
        print("GUAU!!!!!")

    # metodos de clase
    @classmethod
    def perder_colar(cls):
        cls.N_COLAS = 0


perro1 = Perro("jordy", "quiltro")
print(perro1.nombre)
perro1.saludar()

perro2 = Perro("tomas", "chiwawa")
perro2.cambiar_nombre("elizabeth")
perro2.saludar()
print(perro2.nombre)
