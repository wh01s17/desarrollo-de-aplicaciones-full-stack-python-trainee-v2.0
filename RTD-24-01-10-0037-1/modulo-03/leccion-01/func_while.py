# Ejercicio 1
# Solicitar numeros al usuario y sumarlo, cuando ingrese 0, el programa termina e imprime la suma total
total = 0
numero = None

while numero != 0:
    numero = int(input("Ingrese un numero (0 para salir):"))
    total += numero

print("La suma total es: ", total)

# Ejercicio 2
# Solicitar al usuario una contrse·a hhasta que se ingrese la correcta: "Python2025"
clave_correcta = "Python2025"
clave = ""

while clave != clave_correcta:
    clave = input("Ingrese la contraseña:")

print("Acceso concedido")
