class Auto:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.encendido = False

    def encender(self):
        if not self.encendido:
            self.encendido = True
            print(f"El auto {self.marca} {self.modelo} se ha encendido.")
        else:
            print("El auto ya estaba encendido.")

    def apagar(self):
        if self.encendido:
            self.encendido = False
            print(f"El auto {self.marca} {self.modelo} se ha apagado.")
        else:
            print("El auto ya estaba apagado.")

    def estado(self):
        if self.encendido:
            print(f"El auto {self.marca} {self.modelo} esta ENCENDIDO.")
        else:
            print(f"El auto {self.marca} {self.modelo} esta APAGADO.")


# Objetos
auto1 = Auto("Toyota", "MR2")

# Acciones
auto1.estado()
auto1.encender()
auto1.estado()
auto1.apagar()
auto1.estado()
