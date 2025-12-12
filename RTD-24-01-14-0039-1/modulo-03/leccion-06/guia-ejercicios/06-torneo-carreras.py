# 6) SISTEMA DE TORNEO DE CARRERAS
# -------------------------------------------------------------
# Recibes una lista de corredores:
# corredores = [
#     {"nombre": "Luna", "velocidad": 8, "resistencia": 6},
#     {"nombre": "Kai", "velocidad": 7, "resistencia": 9},
#     {"nombre": "Rex", "velocidad": 9, "resistencia": 5}
# ]
#
# Fórmula de rendimiento:
# rendimiento = velocidad * 0.6 + resistencia * 0.4
#
# Tareas:
# 1. Permitir agregar nuevos corredores.
# 2. Simular una carrera: calcular rendimiento para cada participante.
# 3. Ordenar y mostrar el podio (1°, 2°, 3°).
# 4. Permitir al usuario buscar un corredor y mostrar su rendimiento.
# 5. Generar un ranking final completo.


def agregar_corredor(corredores: list):
    nombre = input("Ingrese nombre de corredor:\n")
    while not nombre:
        nombre = input("Error, ingrese nombre de corredor:\n")

    velocidad = int(input("Ingrese velocidad de corredor:\n"))
    while velocidad < 1:
        velocidad = int(input("Error, ingrese velocidad válida:\n"))

    resistencia = int(input("Ingrese resistencia de corredor:\n"))
    while resistencia < 1:
        resistencia = int(input("Error, ingrese resistencia válida:\n"))

    corredores.append(
        {"nombre": nombre, "velocidad": velocidad, "resistencia": resistencia}
    )


def ordenar_corredores(corredores: list):
    ordenados = sorted(
        corredores,
        key=lambda c: calcular_rendimiento(c),
        reverse=True,
    )

    return ordenados


def calcular_rendimiento(corredor):
    return round((corredor["velocidad"] * 0.6) + (corredor["resistencia"] * 0.4), 2)


def iniciar_carrera(corredores: list, ganadores: list):
    if len(corredores) < 3:
        print("No hay suficientes corredores para la carrera")
        return

    print("Comenzó la carrera!")

    for corredor in corredores:
        rendimiento = calcular_rendimiento(corredor)
        print(f"Rendimiento de {corredor['nombre']}: {rendimiento}")

    carrera = ordenar_corredores(corredores)

    print("\n🥇 1er lugar:", carrera[0]["nombre"])
    print("🥈 2do lugar:", carrera[1]["nombre"])
    print("🥉 3er lugar:", carrera[2]["nombre"], "\n")

    agregar_ganador(ganadores, carrera[0])


def agregar_ganador(ganadores: list, ganador):
    for i, g in enumerate(ganadores):
        if g["nombre"] == ganador["nombre"]:
            ganadores[i]["triunfos"] += 1
            return

    ganadores.append({"nombre": ganador["nombre"], "triunfos": 1})


def mostrar_ganadores(ganadores):
    if ganadores:
        ranking = sorted(ganadores, key=lambda g: g["triunfos"], reverse=True)
        iconos = {1: "🥇", 2: "🥈", 3: "🥉"}

        for i, ganador in enumerate(ranking, start=1):
            icono = iconos.get(i, "")
            print(
                f"{icono}{i}° Lugar: {ganador['nombre']} con {ganador['triunfos']} 🏆"
            )
    else:
        print("No hay ganadores")


def buscar_corredor(corredores: list):
    print("BUSCADOR")
    corredor = input("Ingrese nombre de corredor:\n").lower()
    encontrado = None

    for c in corredores:
        if c["nombre"].lower() == corredor:
            encontrado = c
            break

    if encontrado:
        print(f"{encontrado['nombre']}: {calcular_rendimiento(encontrado)}\n")
    else:
        print("No existe el corredor ingresado\n")


corredores = [
    {"nombre": "Luna", "velocidad": 8, "resistencia": 6},
    {"nombre": "Kai", "velocidad": 7, "resistencia": 9},
    {"nombre": "Rex", "velocidad": 9, "resistencia": 5},
]

ganadores = []

runner_ascii = (
    "\033[33m"
    + r"""
                _
              _( }
    -=   _  <<  \
        `.\__/`/\\
  -=      '--'\\  `
       -=     //
   jgs        \)
"""
    + "\033[0m"
)

while True:
    print("=" * 30)
    print("🏆 TORNEO DE CARRERAS 🏆".center(27))
    print(runner_ascii)
    print("=" * 30)

    print(
        "1) Agregar corredor\n2) Iniciar carrera\n3) Buscar corredor\n4) Ver ranking general y salir"
    )
    opcion = int(input("Ingrese una opción:\n"))

    while opcion < 1 or opcion > 4:
        opcion = int(input("Error, ingrese una opción válida:\n"))

    if opcion == 1:
        agregar_corredor(corredores)
    elif opcion == 2:
        iniciar_carrera(corredores, ganadores)
    elif opcion == 3:
        buscar_corredor(corredores)
    else:
        mostrar_ganadores(ganadores)
        break
