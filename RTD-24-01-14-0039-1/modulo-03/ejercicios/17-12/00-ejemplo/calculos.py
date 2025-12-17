"""
archivo para realizar calculos
"""


def calcular_estadisticas(lista_notas:list) -> dict:
    return {
        'promedio': sum(lista_notas)/len(lista_notas),
        'n_min': min(lista_notas),
        'n_max': max(lista_notas),
        'sobre_5': sum([1 for n in lista_notas if n >= 5])
    }


