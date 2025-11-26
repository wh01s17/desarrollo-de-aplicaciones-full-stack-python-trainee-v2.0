# Definición de la clase
class Persona:
    # Esta clase es un molde para crear personas. Define que datos tendrán (nombre y edad), y qué podrá hacer (caminar, saludar)

    # Constructor de la clase
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Método que accede a los atributos de la clase
    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")


# Creamos una instancia de la clase (objeto)
p1 = Persona("wh01s17", 32)

# llamamos al metodo saludar
p1.saludar()
