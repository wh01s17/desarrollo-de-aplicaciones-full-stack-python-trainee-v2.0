# --------------------------------------------------
# EJERCICIO 1: PERSONA
# --------------------------------------------------
# Objetivo:
# Practicar atributos de instancia, atributo de clase y método estático.
# Debe crear una clase llamada Persona con:

# Atributo de clase:
# - especie = "Humano"

# Atributos de instancia:
# - nombre
# - edad

# Métodos:
# - saludar(): imprime "Hola, mi nombre es {nombre}"
# - es_mayor_de_edad(): imprime si es mayor o menor de edad
# - validar_edad(edad): método estático que retorna True si la edad es válida (>=0)

# Tareas:
# 1. Crear la clase Persona.
# 2. Crear 2 instancias de Persona.
# 3. Llamar al método saludar() para ambas instancias.
# 4. Llamar al método es_mayor_de_edad().
# 5. Mostrar el atributo de clase especie.
# 6. Usar el método estático validar_edad().


class Persona:
    ESPECIE = "Humano"

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}")

    def es_mayor_de_edad(self):
        mensaje = "es mayor de edad" if self.edad >= 18 else "es menor de edad"
        print(self.nombre, mensaje)

    @staticmethod
    def validar_edad(edad):
        return edad >= 0


persona1 = Persona("Juan", 20)
persona2 = Persona("Tania", 15)

persona1.saludar()
persona2.saludar()

persona1.es_mayor_de_edad()
persona2.es_mayor_de_edad()

print(f"Especie de la persona: {Persona.ESPECIE}")

edad = int(input("Ingrese una edad:\n"))
validacion = "Edad válida" if Persona.validar_edad(edad) else "Edad inválida"
print(validacion)
