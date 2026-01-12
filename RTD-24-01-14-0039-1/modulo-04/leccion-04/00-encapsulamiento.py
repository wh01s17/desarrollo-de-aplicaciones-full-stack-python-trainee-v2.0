class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def presentar(self):
        print(f"Hola soy {self.nombre.upper()}")

    @property
    def edad(self):
        return self._edad

    @property
    def nombre(self):
        return self.__nombre

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad >= 0:
            self._edad = nueva_edad
        else:
            raise ValueError("Ingresaste un valor negativo")

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre if isinstance(nombre, str) else None

    def ver_edad(self):
        print(self._edad)


p1 = Persona("Tomas", 75)
p1.edad = 25
print(p1.edad)

p1.ver_edad()


print(p1.nombre)
p1.nombre = 6565
print(p1.nombre)
