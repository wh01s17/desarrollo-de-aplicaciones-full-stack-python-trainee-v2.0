def check_rut(rut: str) -> bool:
    """
    Funcion que checkea si el rut tiene el formato adecuado
    """

    tiene_guion = "-" in rut
    largo_rut = len(rut) >= 9

    if tiene_guion and largo_rut:
        return True

    return False


def check_duplicado(dic_pacientes, rut):
    if rut in dic_pacientes.keys():
        return True

    return False


def check_costo_atencion(costo_atencion: str) -> bool:
    if costo_atencion.isnumeric():
        if int(costo_atencion) > 0:
            return True

    return False
