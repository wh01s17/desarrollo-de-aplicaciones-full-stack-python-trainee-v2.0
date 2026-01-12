class Persona:
    raza = "mamífero"

    def __init__(self, nombre, edad, rut):
        self.nombre = nombre
        self.edad = edad
        self.rut = rut

    def presentarse(self):
        return f"Hola soy {self.nombre} y tengo {self.edad} años"

    def cumplir_anios(self):
        self.edad += 1


class EstudiantePython(Persona):
    def __init__(self, nombre, edad, rut, otec, jornada):
        super().__init__(nombre, edad, rut)
        self.otec = otec
        self.jornada = jornada

    @staticmethod
    def programar():
        print("Hola estoy programando")

    def cumplir_anios(self):
        super().cumplir_anios()
        print("Cumplí años")


class Ayudante(Persona): ...


e1 = EstudiantePython("Elizabeth", 25, "123412332-9", "Sustantiva", "Tarde")

a = Ayudante("Jordy", 35, "12341234-9")
print(a.presentarse())


class Mamifero:
    def __init__(self, tipo_pelaje):
        self.tipo_pelaje = tipo_pelaje

    def caracteristica(self):
        print("Me reproduzco por crias vivas")


class Felino:
    def __init__(self, size):
        self.size = size

    def hablar(self):
        print("Hola tengo bigotes y puedo ronronear")


class Gato(Mamifero, Felino): ...


gato = Gato()
gato.caracteristica()
gato.hablar()
