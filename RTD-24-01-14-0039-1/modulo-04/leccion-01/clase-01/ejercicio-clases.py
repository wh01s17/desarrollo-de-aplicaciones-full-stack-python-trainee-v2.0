# Deben crear 3 objetos con 3 atributos y 2 métodos cada uno
# Deben crear 2 instancias de cada objeto
# Y llamar a sus atributos y métodos
# Luego deben alterar el estado de la instancia cambiando un atributo de cada instancia
import time


class Notebook:
    ram = ""
    ssd = ""
    modelo = ""

    def encender(self):
        print(f"Iniciando {self.modelo}...")
        time.sleep(2)
        print("Encendido correctamente")

    @staticmethod
    def apagar():
        print("Cerrando aplicaciones...")
        print("Apagado correctamente")


class Auto:
    marca = ""
    modelo = ""
    combustible = ""

    def arrancar(self):
        print(f"El auto {self.marca} {self.modelo} está arrancando...")
        print("Listo para conducir")

    @staticmethod
    def detenerse():
        print("Deteniendo el vehículo...")
        time.sleep(2)
        print("El auto se ha detenido")


class Consola:
    marca = ""
    modelo = ""
    almacenamiento = ""

    def iniciar_sesion(self):
        print(f"Iniciando sesión en {self.modelo}...")
        print("Sesión iniciada correctamente")

    @staticmethod
    def cerrar_sesion():
        print("Guardando progreso...")
        time.sleep(2)
        print("Sesión cerrada")


print("-" * 40)
print("Instancias de la clase Notebook")
print("-" * 40)
notebook1 = Notebook()
notebook1.ram = "16 GB"
notebook1.ssd = "500 GB"
notebook1.modelo = "Lenovo Thinkpad E480"
notebook1.encender()
notebook1.ram = "32 GB"
print(f"Nueva RAM del notebook : {notebook1.ram}")
notebook1.apagar()

notebook2 = Notebook()
notebook2.ram = "64 GB"
notebook2.ssd = "2 TB"
notebook2.modelo = "Framework 16"
notebook2.encender()
notebook2.apagar()


print("-" * 40)
print("Instancias de la clase Auto")
print("-" * 40)
auto1 = Auto()
auto1.marca = "Toyota"
auto1.modelo = "Corolla"
auto1.combustible = "Bencina"
auto1.arrancar()
auto1.combustible = "Eléctrico"
print(f"Nuevo tipo de combustible: {auto1.combustible}")
auto1.detenerse()

auto2 = Auto()
auto2.marca = "Suzuki"
auto2.modelo = "Vitara 1GEN"
auto2.combustible = "Bencina"
auto2.arrancar()
auto2.detenerse()


print("-" * 40)
print("Instancias de la clase Consola")
print("-" * 40)
consola1 = Consola()
consola1.marca = "Sony"
consola1.modelo = "PlayStation 5"
consola1.almacenamiento = "1 TB"
consola1.iniciar_sesion()
consola1.almacenamiento = "2 TB"
print(f"Nuevo almacenamiento: {consola1.almacenamiento}")
consola1.cerrar_sesion()

consola2 = Consola()
consola2.marca = "Microsoft"
consola2.modelo = "Xbox Series X"
consola2.almacenamiento = "1 TB"
consola2.iniciar_sesion()
consola2.cerrar_sesion()
