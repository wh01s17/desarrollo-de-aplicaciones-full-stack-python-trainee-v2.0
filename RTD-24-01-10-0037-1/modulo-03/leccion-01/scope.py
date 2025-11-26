# Scopes
# Local scope
def print_number():
    first_num = 1
    # imprimir declaracion
    print("El primer numero definido es: ", first_num)

print_number()

# Global scope
saludo = "Hola"

def saludar_mundo():
    palabra = "mundo"
    print(saludo, palabra)

def saludar_nombre(nombre):
    print(saludo, nombre)

saludar_mundo()
saludar_nombre('Julieta')
