# --------------------------------------------------
# EJERCICIO 3: LIBRO
# --------------------------------------------------
# Objetivo:
# Usar atributo de clase para contar instancias y método estático.
# Debe crear una clase Libro con:

# Atributo de clase:
# - total_libros = 0

# Atributos de instancia:
# - titulo
# - autor
# - prestado (inicia en False)

# Métodos:
# - prestar(): cambia el estado a prestado
# - devolver(): cambia el estado a disponible
# - mostrar_estado(): imprime el estado actual
# - descripcion(): método estático que describe qué es un libro

# Tareas:
# 1. Crear la clase Libro.
# 2. Crear 3 instancias de libros.
# 3. Mostrar el total de libros creados.
# 4. Prestar al menos un libro.
# 5. Mostrar el estado de cada libro.
# 6. Llamar al método estático descripcion().


class Libro:
    total_libros = 0

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.prestado = False
        Libro.total_libros += 1

    def prestar(self):
        self.prestado = True

    def devolver(self):
        self.prestado = False

    def mostrar_estado(self):
        mensaje = "prestado" if self.prestado else "disponible"
        print(f'El libro "{self.titulo}", se encuentra {mensaje}')

    @staticmethod
    def descripcion():
        desc = "Un libro es una obra escrita que reúne conocimientos, ideas o historias organizadas en páginas.\nPuede tener fines educativos, informativos o recreativos, y permite transmitir cultura y pensamiento a través del tiempo."
        print(desc)


lotr = Libro("El señor de los anillos", "J. R. R. Tolkien")
revolucion = Libro("Revolución o reforma", "Rosa Luxemburgo")
valpo = Libro("Valparaíso", "Sergio Larraín")

print("Total de libros:", Libro.total_libros)

revolucion.prestar()

lotr.mostrar_estado()
revolucion.mostrar_estado()
valpo.mostrar_estado()

Libro.descripcion()
