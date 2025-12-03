# Entrada
edad = input("Dime tu edad: ")

# Proceso
es_menor = int(edad) <= 18

# Salida
if not es_menor:
    print("Puedes entrar al casino")
else:
    print("No puedes entrar al casino")
