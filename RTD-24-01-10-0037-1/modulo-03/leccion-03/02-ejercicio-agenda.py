agenda = {}

opc = "s"

while opc.lower() == "s":
    nombre = input("Ingrese el nombre: ")
    numero = input("Ingrese el numero: ")

    if nombre.strip() in agenda:
        print("El nombre ingresado ya existe en la agenda")
    else:
        agenda[nombre.strip()] = numero

    opc = input("Desea agregar otro número? (s/n)")

print("\nAgenda")
for nombre, numero in agenda.items():
    print(f"{nombre.capitalize()}: {numero}")
