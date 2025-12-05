nombre = input("Ingrese su nombre: ")
sepso = input("Ingrese su sexo (M/H): ")

if (sepso.upper() == "M" and nombre[0].upper() < "M") or (
    sepso.upper() == "H" and nombre[0].upper() > "N"
):
    print("Tu grupo es A")
else:
    print("Tu grupo es B")
