# Ejercicio 1 - Gestión de turnos médicos
# Contexto
# Un centro médico necesita administrar los turnos de atención de sus pacientes durante el día.
# Cada paciente tiene un nombre y una especialidad médica asociada a su turno.

# Desarrolle un programa que permita:
# •	Registrar varios pacientes con su especialidad.
# •	Almacenar los turnos en una estructura de datos.
# •	Recorrer todos los turnos para mostrarlos por pantalla.
# •	Simular la atención de cada paciente en orden.

# Se espera que:
# •	Exista una clase que represente un turno o paciente.
# •	Los turnos se gestionen mediante una lista.
# •	Se utilice un ciclo for para recorrer y atender los turnos.


class Paciente:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad

    def __str__(self):
        return f"Nombre: {self.nombre}, Especialidad: {self.especialidad}"


turnos = []

while True:
    nombre = input("Ingrese un nombre o enter para atender pacientes:\n")

    if not nombre:
        break

    especialidad = input("Ingrese la especialidad:\n")
    while len(especialidad) < 2:
        especialidad = input("Error, ingrese especialidad válida:\n")

    turnos.append(Paciente(nombre, especialidad))

print("Lista de turnos:")
for i, t in enumerate(turnos, start=1):
    print(f"Turno {i}: {t}")

print("\nPacientes atendidos:")
for i, t in enumerate(turnos, start=1):
    print(f"Atendiendo turno {i}:")
    print(f"Paciente: {t.nombre}")
    print(f"Especialidad: {t.especialidad}\n")
