import validarores


def registrar_paciente(pacientes: dict) -> None:
    nombre = input("Dime tu nombre completo: ")
    rut = input("Dime tu rut ej: 99999999-9: ")

    if validarores.check_rut(rut) and (not validarores.check_duplicado(pacientes, rut)):
        pacientes[rut] = {
            "nombre": nombre,
        }
        print("Paciente Agregado.")
    else:
        print("Datos incorrectos, paciente no agregado.")


def registrar_atencion(lista_atencion: list, pacientes: dict) -> None:
    """
    Funcion para registrar una atencion
    """
    rut = input("Dime tu rut ej: 99999999-9: ")
    if rut in pacientes.keys():
        tipo_atencion = input(
            "tipo de atención (ej: kinesiología, medicina, enfermería:: "
        )
        costo_atencion = input("costo de la atención ")
        if validarores.check_costo_atencion(costo_atencion):
            lista_atencion.append(
                {
                    "rut": rut,
                    "tipo_atencion": tipo_atencion,
                    "costo_atencion": int(costo_atencion),
                }
            )

    else:
        print("Run igresado no existe:")


def total_por_atencion(atenciones: list) -> dict:
    """
    calcualr total recaudado por atencion
    """

    tipo_atenciones = set([atencion["tipo_atencion"] for atencion in atenciones])

    t = {}

    for tipo_atencion in tipo_atenciones:
        for atencion in atenciones:
            if tipo_atencion == atencion["tipo_atencion"]:
                if tipo_atencion in t.keys():
                    t[tipo_atencion] += atencion["costo_atencion"]
                else:
                    t[tipo_atencion] = atencion["costo_atencion"]

    return t
