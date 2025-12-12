class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def promedio(self):
        return sum(self.notas) / len(self.notas)


alumno1 = Alumno("Pepe")
alumno1.agregar_nota(7)
alumno1.agregar_nota(5)
alumno1.agregar_nota(4)
print(f"Promedio: {alumno1.promedio():.2f}")
