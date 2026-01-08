# =================================================
# EJERCICIO 1: SISTEMA DE ATENCIÓN MÉDICA
# Tema: COMPOSICIÓN
# =================================================

# CONTEXTO:
# Se desea modelar un sistema simple de atención médica.
# Un Paciente tiene un Historial Médico que almacena
# diagnósticos y tratamientos.

# IMPORTANTE:
# - El historial médico NO debe existir sin el paciente.
# - El historial se crea dentro de la clase Paciente.
# Esto es un ejemplo de COMPOSICIÓN.

# 1) Crea la clase HistorialMedico
# Atributos:
# - diagnosticos (lista)
# - tratamientos (lista)

# Métodos:
# - agregar_diagnostico(diagnostico)
# - agregar_tratamiento(tratamiento)
# - mostrar_historial()


class HistorialMedico:
    def __init__(self) -> None:
        self.diagnosticos = []
        self.tratamientos = []

    def agregar_diagnostico(self, diagnostico: str) -> None:
        self.diagnosticos.append(diagnostico)

    def agregar_tratamiento(self, tratamiento: str) -> None:
        self.tratamientos.append(tratamiento)

    def mostrar_historial(self) -> None:
        print("\nDiagnósticos")
        print("------------")

        if self.diagnosticos:
            for d in self.diagnosticos:
                print(d)
        else:
            print("Sin diagnosticos para mostrar")

        print("\nTratamientos")
        print("------------")

        if self.tratamientos:
            for t in self.tratamientos:
                print(t)
        else:
            print("Sin tratamientos para mostrar")


# 2) Crea la clase Paciente
# Atributos:
# - nombre
# - edad
# - historial (instancia de HistorialMedico)

# Métodos:
# - mostrar_info()


class Paciente:
    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre = nombre
        self.edad = edad
        self.historial = HistorialMedico()

    def mostrar_info(self) -> None:
        print("\nDatos de paciente")
        print("-----------------")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        self.historial.mostrar_historial()


# 3) PRUEBAS (descomenta cuando tengas tu solución)

paciente1 = Paciente("Juan Pérez", 45)
paciente1.historial.agregar_diagnostico("Hipertensión")
paciente1.historial.agregar_diagnostico("Diabetes tipo 2")
paciente1.historial.agregar_tratamiento("Medicamento A")

paciente1.mostrar_info()
