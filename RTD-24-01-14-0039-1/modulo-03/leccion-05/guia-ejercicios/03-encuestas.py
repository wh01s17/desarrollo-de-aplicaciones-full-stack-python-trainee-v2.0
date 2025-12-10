# 3) SISTEMA DE ENCUESTAS CON ANÁLISIS ESTADÍSTICO
# -------------------------------------------------------------
# El programa debe recoger opiniones sobre un servicio.
# Las preguntas serán:
# - Calidad (1 a 7)
# - Rapidez (1 a 7)
# - Amabilidad (1 a 7)
#
# Tareas:
# 1. Permitir almacenar respuestas de varios encuestados (mínimo 5). Cada respuesta es un diccionario.
# 2. Calcular el promedio de cada criterio.
# 3. Identificar cuál criterio obtuvo la mejor valoración promedio.
# 4. Identificar al encuestado con mejor promedio global.
# 5. Mostrar un reporte final con toda la información.

encuestados = []
criterios = ["calidad", "rapidez", "amabilidad"]
contador = 0

while contador < 5:
    nombre = input("Ingrese nombre de encuestado:\n")
    respuesta = {"nombre": nombre}

    for criterio in criterios:
        valor = int(input(f"Ingrese {criterio} del servicio (1 a 7)"))

        while valor < 1 or valor > 7:
            valor = int(input(f"Error, ingrese {criterio} del servicio (1 a 7)"))

        respuesta[criterio] = valor

    encuestados.append(respuesta)
    contador += 1

max_promedio = 0
mejor_encuestado = None
suma = {"calidad": 0, "rapidez": 0, "amabilidad": 0}

for e in encuestados:
    prom = (e["calidad"] + e["rapidez"] + e["amabilidad"]) / 3

    if prom > max_promedio:
        max_promedio = prom
        mejor_encuestado = e

    for c in criterios:
        suma[c] += e[c]

promedios = {
    "calidad": suma["calidad"] / len(encuestados),
    "rapidez": suma["rapidez"] / len(encuestados),
    "amabilidad": suma["amabilidad"] / len(encuestados),
}

mejor_criterio = ""
mejor_valor = 0

for crit in criterios:
    if promedios[crit] > mejor_valor:
        mejor_valor = promedios[crit]
        mejor_criterio = crit

print("\nREPORTE")
for c in criterios:
    print(f"Promedio {c}: {promedios[c]:.2f}")

print(f"El criterio mejor evaluado fue {mejor_criterio} con {mejor_valor:.2f}")
print(
    f"El encuestado con mejor promedio: {mejor_encuestado['nombre']} con {max_promedio:.2f}"
)
