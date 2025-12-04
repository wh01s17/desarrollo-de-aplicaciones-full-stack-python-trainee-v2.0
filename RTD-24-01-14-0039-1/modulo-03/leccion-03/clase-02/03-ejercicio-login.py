password = "python2025"

# Opcion 1
while True:
    input_user = input("Ingrese su contraseña: ")

    if input_user != password:
        print("Contraseña incorrecta, reingrese")
    else:
        print("Bienvenido")
        break

# Opcion 2
input_user = input("Ingrese su contraseña: ")

while input_user != password:
    input_user = input("Contraseña incorrecta, reingrese: ")

print("Bienvenido")
