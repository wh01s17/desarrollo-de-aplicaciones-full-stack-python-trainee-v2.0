"""
Ingresar notas
"""


def es_valido(numero: str) -> bool:
    """
    funcion para ver si un string es un numero valido
    """

    n = numero.replace(",", "").replace(".", "").strip()

    if n.isdigit():
        n = float(numero)
        if n >= 1 and n <= 7:
            return True

    return False


def ingreso_notas(lista_notas: list):
    """
    Funcion para ingresar una nota a la lista de notas
    """

    nota = input("Dime una nota del 1 al 7: ")

    if es_valido(nota):
        lista_notas.append(float(nota))

    else:
        print("Nota no valida")
