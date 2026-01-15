import csv
from paciente import Paciente


class Sistema:
    def __init__(
        self, archivo_entrada="ejercicio.csv", archivo_salida="output_file.csv"
    ):
        self.archivo_entrada = archivo_entrada
        self.archivo_salida = archivo_salida

    def agregar_paciente(self, paciente: Paciente):
        with open(
            self.archivo_entrada, "a", encoding="utf8", newline=""
        ) as csv_entrada:
            archivo = csv.writer(csv_entrada, delimiter=";")
            archivo.writerow(
                [
                    f"{paciente.nombre} {paciente.apellido}",
                    paciente.peso,
                    paciente.talla,
                ]
            )

    def procesar_archivo(self):
        CABECERA = [
            "Nombre",
            "Apellido",
            "Peso[Kg]",
            "Talla[Mt]",
            "IMC",
            "Clasificacion",
        ]

        with open(self.archivo_salida, "w", encoding="utf8") as csv_salida:
            archivo = csv.writer(csv_salida, delimiter=";")
            archivo.writerow(CABECERA)

            for p in self.obtener_lista(self.archivo_entrada):
                nombre, apellido = p[0].split(maxsplit=1)
                paciente = Paciente(nombre, apellido, int(p[1]), int(p[2]))
                archivo.writerow(
                    [
                        paciente.nombre,
                        paciente.apellido,
                        round(paciente.peso / 1000, 1),
                        round(paciente.talla / 100, 2),
                        paciente.imc,
                        paciente.clasificar_imc(),
                    ]
                )

    @staticmethod
    def obtener_lista(archivo):
        with open(archivo, encoding="utf8") as csv_archivo:
            archivo = csv.reader(csv_archivo, delimiter=";")
            next(archivo)
            return list(archivo)

    @staticmethod
    def menu():
        print("Calcular y Clasificar IMC")
        print("-------------------------")
        print("1 - Agregar paciente")
        print("2 - Procesar datos")
        print("0 - Salir")

        return int(input("Ingrese opción:\n"))

    def run(self):
        while True:
            opcion = self.menu()

            if opcion == 0:
                break
            elif opcion == 1:
                nombre = input("Nombre:\n")
                apellido = input("Apellido:\n")
                peso = input("Peso (g):\n")
                talla = input("Talla (cm):\n")
                paciente = Paciente(nombre, apellido, int(peso), int(talla))
                self.agregar_paciente(paciente)
            elif opcion == 2:
                self.procesar_archivo()


sistema = Sistema()

sistema.run()
