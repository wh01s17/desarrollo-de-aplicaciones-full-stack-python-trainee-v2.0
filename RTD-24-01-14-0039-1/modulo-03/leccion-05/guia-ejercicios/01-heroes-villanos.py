###############################################################
# 1) SISTEMA DE GESTIÓN DE HÉROES Y VILLANOS
# -------------------------------------------------------------
# Crea un sistema donde existan héroes y villanos.
# Estructura inicial:

# villanos = [
#     {"nombre": "Sombrío", "fuerza": 70, "velocidad": 40},
#     {"nombre": "Vortéx", "fuerza": 55, "velocidad": 95}
# ]

#
# Tareas:
# 1. Permitir al usuario agregar un héroe o un villano nuevo (con nombre, fuerza y velocidad). GUARDAR -> lista_vacia.append('elemento')

# 2. Crear una funcionalidad que determine el ganador entre cualquier héroe y villano.
#    El ganador se define por la suma: poder_total = fuerza + velocidad.
# 3. Simular una batalla: el usuario elige un héroe y un villano por nombre y el programa indica el ganador. EXTRAER -> con un for !!!!!!

# 4. Mostrar un ranking ordenado de mayor a menor poder de todos los personajes.

heroes = [
    {"nombre": "Spider-Man", "fuerza": 75, "velocidad": 90},
    {"nombre": "Iron Man", "fuerza": 85, "velocidad": 70},
    {"nombre": "Captain America", "fuerza": 80, "velocidad": 65},
    {"nombre": "Thor", "fuerza": 100, "velocidad": 80},
    {"nombre": "Black Panther", "fuerza": 85, "velocidad": 95},
]

villanos = [
    {"nombre": "Thanos", "fuerza": 100, "velocidad": 60},
    {"nombre": "Loki", "fuerza": 70, "velocidad": 75},
    {"nombre": "Green Goblin", "fuerza": 65, "velocidad": 85},
    {"nombre": "Ultron", "fuerza": 90, "velocidad": 70},
    {"nombre": "Venom", "fuerza": 85, "velocidad": 80},
]

while True:
    opcion = (
        input(
            "Ingrese el tipo de personaje que desea ingresar (héroe, villano), pelear, ranking o enter para salir:\n"
        )
        .lower()
        .strip()
    )

    if not opcion:
        break

    while (
        opcion != "heroe"
        and opcion != "villano"
        and opcion != "pelear"
        and opcion != "ranking"
    ):
        opcion = input("Entrada no válida, reingrese:\n").lower().strip()

    if opcion == "heroe":
        nombre = input("Ingresa el nombre:\n")
        fuerza = int(input("Ingresa la fuerza:\n"))
        velocidad = int(input("Ingresa la velocidad:\n"))
        heroes.append({"nombre": nombre, "fuerza": fuerza, "velocidad": velocidad})
    elif opcion == "villano":
        nombre = input("Ingresa el nombre:\n")
        fuerza = int(input("Ingresa la fuerza:\n"))
        velocidad = int(input("Ingresa la velocidad:\n"))
        villanos.append({"nombre": nombre, "fuerza": fuerza, "velocidad": velocidad})

    if opcion == "pelear":
        print("Elija un heroe de la lista:")
        for h in heroes:
            print(h.get("nombre"))

        heroe_peleador = input(">").strip()

        for h in heroes:
            if h.get("nombre") == heroe_peleador:
                h_poder_total = h.get("fuerza") + h.get("velocidad")

        print("Elija un villano de la lista:")
        for v in villanos:
            print(v.get("nombre"))

        villano_peleador = input(">").strip()

        for v in villanos:
            if v.get("nombre") == villano_peleador:
                v_poder_total = v.get("fuerza") + v.get("velocidad")

        if h_poder_total > v_poder_total:
            print("El ganador es: ", heroe_peleador)
        elif v_poder_total > h_poder_total:
            print("El ganador es: ", villano_peleador)
        else:
            print("Empate")

    # ALGORITMO SELECTION SORT
    if opcion == "ranking":
        ranking = heroes + villanos
        for i in range(len(ranking)):
            indice_max = i

            for j in range(i + 1, len(ranking)):
                poder_j = ranking[j]["fuerza"] + ranking[j]["velocidad"]
                poder_max = (
                    ranking[indice_max]["fuerza"] + ranking[indice_max]["velocidad"]
                )

                if poder_j > poder_max:
                    indice_max = j

            ranking[i], ranking[indice_max] = ranking[indice_max], ranking[i]

        for p in ranking:
            print(p["nombre"], "-", p["fuerza"] + p["velocidad"])

    # FUNCION LAMBDA
    # if opcion == "ranking":
    #     ranking = heroes + villanos

    #     ordenados = sorted(
    #         ranking, key=lambda p: p["fuerza"] + p["velocidad"], reverse=True
    #     )

    #     for p in ordenados:
    #         poder_total = p["fuerza"] + p["velocidad"]
    #         print(f"{p['nombre']} - Poder total: {poder_total}")

    # SOLO EL PERSONAJE MAS FUERTE VISTO EN CLASES
    # if opcion == "ranking":
    #     max_rank = None
    #     max_poder = 0

    #     personajes = villanos + heroes

    #     for personaje in personajes:
    #         poder_personaje = personaje["velocidad"] + personaje["fuerza"]
    #         if poder_personaje > max_poder:
    #             max_poder = poder_personaje
    #             max_rank = personaje

    #     print(f"personaje con mayor poder: {max_rank['nombre']}")
