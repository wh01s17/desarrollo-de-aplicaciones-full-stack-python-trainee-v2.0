def sumar(*numeros):
    print(sum(numeros))


sumar(2, 34, 324, 45, 9)


def promedio(*notas):
    return 0 if len(notas) == 0 else sum(notas) / len(notas)


promedio()
