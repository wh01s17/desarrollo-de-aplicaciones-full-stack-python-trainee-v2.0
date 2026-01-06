# =========================================================
# 10. EJERCICIO 2: SISTEMA DE RESERVAS MÉDICAS
# =========================================================
"""
CONTEXTO:
---------
Un centro de salud necesita gestionar reservas de consultas.

REQUERIMIENTOS:
---------------
Cada consulta debe tener:
- Nombre del paciente
- Nombre del profesional
- Hora de atención
- Estado (reservada / cancelada)

El sistema debe permitir:
- Crear reservas
- Cancelar reservas
- Mostrar información
- Contar consultas activas
"""


class ConsultaMedica:
    def __init__(
        self, nombre_paciente: str, nombre_pro: str, hora_atencion: str, estado: str
    ) -> None:
        self.nombre_paciente = nombre_paciente
        self.nombre_pro = nombre_pro
        self.hora_atencion = hora_atencion
        self.estado = estado

    def mostrar_info(self) -> None:
        print(f"Paciente: {self.nombre_paciente}")
        print(f"Profesional: {self.nombre_pro}")
        print(f"Hora de atención: {self.hora_atencion}")
        print(f"Estado: {self.estado}")

    def modificar_reserva(self, nuevo_estado: str) -> None:
        self.estado = nuevo_estado


def crear_reserva(reservas: list) -> None:
    print("Crear Reserva")
    print("-------------")
    paciente = input("Nombre de paciente:\n")
    profesional = input("Nombre de profesional:\n")
    hora = input("Hora de atención:\n")
    estado = "reservada"

    reserva = ConsultaMedica(
        nombre_paciente=paciente,
        nombre_pro=profesional,
        hora_atencion=hora,
        estado=estado,
    )
    reservas.append(reserva)


def listar_reservas(reservas: list) -> None:
    if not reservas:
        print("No hay reservas")
        return

    for i, r in enumerate(reservas, start=1):
        print(f"\nReserva N° {i}")
        r.mostrar_info()


def cancelar_reserva(reservas: list) -> None:
    if not reservas:
        print("No hay reservas")
        return

    print("Cancelar estado de reserva")
    print("---------------------------")
    listar_reservas(reservas)
    opcion = int(input(f"Seleccione reserva (1 a {len(reservas)}):\n"))

    while opcion < 1 or opcion > len(reservas):
        opcion = int(input(f"Ingrese reserva válida (1 a {len(reservas)}):\n"))

    reservas[opcion - 1].modificar_reserva("cancelada")


def contar_activas(reservas: list) -> int:
    return sum([1 for r in reservas if r.estado == "reservada"])


reservas = []
menu = """
1 - Crear reservas
2 - Cancelar reservas
3 - Mostrar información
4 - Contar consultas activas
0 - Salir
Ingrese una opción del menú:\n"""

while True:
    opcion = int(input(menu))

    if opcion == 0:
        break
    elif opcion == 1:
        crear_reserva(reservas)
    elif opcion == 2:
        cancelar_reserva(reservas)
    elif opcion == 3:
        listar_reservas(reservas)
    elif opcion == 4:
        print("Cantidad de reservas activas:", contar_activas(reservas))
