"""
=========================================================
GUÍA DE APRENDIZAJE
PROGRAMACIÓN ORIENTADA A OBJETOS (POO) EN PYTHON
=========================================================

Objetivo:
---------
Comprender y aplicar los conceptos fundamentales de la
Programación Orientada a Objetos (POO) en Python, utilizando
clases, atributos y distintos tipos de métodos.

Al finalizar esta guía serás capaz de:
- Crear clases y objetos
- Diferenciar atributos de clase y de instancia
- Utilizar métodos de instancia, de clase y estáticos
- Analizar un problema y resolverlo usando POO
"""

# =========================================================
# 1. ¿QUÉ ES LA PROGRAMACIÓN ORIENTADA A OBJETOS?
# =========================================================
"""
La Programación Orientada a Objetos (POO) es un paradigma
de programación que organiza el código en torno a objetos.

Un objeto representa una entidad del mundo real y contiene:
- Atributos  -> datos
- Métodos    -> comportamientos
"""

# =========================================================
# 2. CLASES Y OBJETOS
# =========================================================
"""
Una CLASE es un molde o plantilla.
Un OBJETO es una instancia creada a partir de una clase.
"""


class Persona:
    pass


persona1 = Persona()
persona2 = Persona()

# =========================================================
# 3. ATRIBUTOS DE INSTANCIA
# =========================================================
"""
Los atributos de instancia:
- Son propios de cada objeto
- Se definen dentro del método __init__
"""


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # atributo de instancia
        self.edad = edad  # atributo de instancia


p1 = Persona("Ana", 25)
p2 = Persona("Luis", 30)

# =========================================================
# 4. ATRIBUTOS DE CLASE
# =========================================================
"""
Los atributos de clase:
- Son compartidos por todas las instancias
- Se definen fuera del __init__
"""


class Persona:
    especie = "Humano"  # atributo de clase

    def __init__(self, nombre):
        self.nombre = nombre


# =========================================================
# 5. MÉTODOS DE INSTANCIA
# =========================================================
"""
Los métodos de instancia:
- Usan 'self'
- Operan sobre los datos del objeto
"""


class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre}"


# =========================================================
# 6. MÉTODOS DE CLASE
# =========================================================
"""
Los métodos de clase:
- Usan el decorador @classmethod
- Reciben 'cls' como parámetro
- Operan sobre la clase
"""


class Persona:
    especie = "Humano"

    @classmethod
    def cambiar_especie(cls, nueva_especie):
        cls.especie = nueva_especie


# =========================================================
# 7. MÉTODOS ESTÁTICOS
# =========================================================
"""
Los métodos estáticos:
- Usan el decorador @staticmethod
- No utilizan ni self ni cls
- Son funciones relacionadas conceptualmente con la clase
"""


class Persona:
    @staticmethod
    def es_mayor_de_edad(edad):
        return edad >= 18


# =========================================================
# 8. EJEMPLO INTEGRADOR
# =========================================================


class CuentaBancaria:
    banco = "Banco Python"

    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
        else:
            print("Saldo insuficiente")

    @classmethod
    def cambiar_banco(cls, nuevo_banco):
        cls.banco = nuevo_banco

    @staticmethod
    def es_monto_valido(monto):
        return monto > 0


"""
SUGERENCIA:
-----------
Antes de programar:
1. Identifica atributos y métodos
2. Distingue atributos de clase y de instancia
3. Dibuja la clase
4. Implementa paso a paso
5. Prueba con múltiples objetos
"""

# =========================================================
# 9. EJERCICIO 1: SISTEMA DE GESTIÓN DE VEHÍCULOS
# =========================================================

"""
CONTEXTO:
---------
Una empresa de transporte necesita administrar su flota
de vehículos.

REQUERIMIENTOS:
---------------
Cada vehículo debe tener:
- Patente
- Marca 
- Año 
- Kilometraje 

El sistema debe permitir:
- Registrar vehículos <- crear una instancia
- Mostrar información del vehículo
- Actualizar kilometraje
- Contar cuántos vehículos existen

REGLAS:
-------
- Crear una clase Vehiculo
- Usar atributos de instancia
- Usar un atributo de clase como contador
- Usar métodos de instancia
- Usar un método de clase
- Usar un método estático para validar el año
"""

mensaje = """
1 - Registrar vehículos 
2 - Mostrar información del vehículo
3 - Actualizar kilometraje
4 - Contar cuántos vehículos existen
5 - Salir
>>>: """
# 👉 AQUÍ COMIENZA TU SOLUCIÓN


class Vehiculo:
    def __init__(self, patente: str, marca: str, anio: int, kilometraje: float) -> None:
        self.patente = patente
        self.marca = marca
        self.anio = anio
        self.kilometraje = kilometraje

    def mostrar_info(self):
        return f"""
Informacion del Vehiculo
------------------------
patente = {self.patente}
marca = {self.marca} 
año = {self.anio} 
kilometraje = {self.kilometraje}  

"""

    def actualizar_kilomtraje(self, nuevo_kilometraje):
        self.kilometraje = nuevo_kilometraje


def crear_vehiculo(registro_vehiculos: list):
    marca = input("Dime la marcar del vehiculo: ")
    patente = input("Dime la patente del vehiculo: ")
    anio = input("Dime la año del vehiculo: ")
    km = input("Dime el kilometraje del vehiculo: ")
    vehiculo = Vehiculo(marca=marca, patente=patente, anio=anio, kilometraje=km)
    registro_vehiculos.append(vehiculo)


def mostrar_info_vehiculos(registr_vehiculos):
    for vehiculo in registr_vehiculos:
        print(vehiculo.mostrar_info())


vehiculos = []

while True:
    opcion = input(mensaje)
    if opcion == "5":
        break

    elif opcion == "1":
        crear_vehiculo(vehiculos)

    elif opcion == "2":
        mostrar_info_vehiculos(vehiculos)

    elif opcion == "3":
        nuevo_kilometraje = input("Dime un nuevo kilometraje")
        for vehiculo in vehiculos:
            vehiculo.actualizar_kilomtraje(nuevo_kilometraje)

    elif opcion == "4":
        print(len(vehiculos))


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

# 👉 AQUÍ COMIENZA TU SOLUCIÓN
# class Consulta:
#     pass


# =========================================================
# FIN DE LA GUÍA
# =========================================================
