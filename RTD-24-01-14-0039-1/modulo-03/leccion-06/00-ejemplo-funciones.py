# def nomre_funcion(parametros):
#     codigo


def suma(a, b):
    resultado = a + b
    print(resultado)


suma(2, 4)

# def potencia(a, b=2):
#     resultado = a**b
#     return resultado


def potencia(a, b=2):
    return a**b


print(potencia(2) + 2)


lista = []


def agregar_elemento(a, b):
    a.append(b)


agregar_elemento(lista, 5)

print(lista)
