# Módulo 3 – Sistema de Reserva de Cine CLI (Fundamentos de Python)
# 1) Propósito

# Desarrollar una aplicación de consola en Python que modele el funcionamiento básico de un sistema de reserva de entradas de cine, permitiendo:
# - Mostrar cartelera de películas.
# - Buscar películas por nombre o género.
# - Reservar entradas para una película.
# - Ver reservas realizadas y total acumulado.
# - Cancelar reservas.

# Usando solo los contenidos del Módulo 3: tipos de datos, condicionales, ciclos, estructuras de datos y funciones.

# 2) Alcance del ejercicio (MVP)

# 2.1. Cartelera de películas
# En el código se debe definir una cartelera inicial con mínimo 5 películas.
# Cada película debe tener:
# - id (entero y único)
# - título
# - género (ej.: acción, comedia, infantil, drama)
# - precio_entrada (float > 0)

# 2.2. Menú principal
# El menú debe mostrarse así:
# === Sistema de Reserva de Cine ===
# 1) Ver cartelera de películas
# 2) Buscar película por nombre o género
# 3) Reservar entradas
# 4) Ver reservas y total acumulado
# 5) Cancelar todas las reservas
# 0) Salir

# El menú debe repetirse hasta elegir la opción 0.
# 2.3. Reservas
# Las reservas se almacenarán en memoria (lista, diccionario u otra estructura).
# Cada reserva debe almacenar: id, título, cantidad, precio unitario, subtotal.
# Funciones mínimas:
# - Reservar entradas (validar id y cantidad > 0)
# - Ver reservas y total
# - Cancelar reservas

# 2.4. Búsqueda de películas
# Permitir buscar por nombre o género. Mostrar todas las coincidencias.

# 3) Requisitos técnicos
# - Usar int, float, str, bool
# - Usar estructuras compuestas
# - Usar condicionales
# - Usar ciclos while y for
# - Usar mínimo 3 funciones (una debe retornar valor)
# - Usar buenas prácticas de snake_case e indentación

# 4) Entregables
# - Archivo Python: cine_reservas_m3.py
# - Opcional README.txt o README.md con descripción y ejecución

import menu
import peliculas as pl
import reservas as rs


def main():
    peliculas = [
        {"id": 1, "titulo": "Inception", "genero": "acción", "precio_entrada": 7500.0},
        {
            "id": 2,
            "titulo": "La princesa Mononoke",
            "genero": "infantil",
            "precio_entrada": 5000.0,
        },
        {"id": 3, "titulo": "El Padrino", "genero": "drama", "precio_entrada": 8000.0},
        {"id": 4, "titulo": "Oldboy", "genero": "drama", "precio_entrada": 8500.0},
        {"id": 5, "titulo": "Goodfellas", "genero": "drama", "precio_entrada": 7000.0},
        {
            "id": 6,
            "titulo": "Enter the Void",
            "genero": "drama",
            "precio_entrada": 5500.0,
        },
        {
            "id": 7,
            "titulo": "Batman: The Dark Knight",
            "genero": "acción",
            "precio_entrada": 7800.0,
        },
        {
            "id": 8,
            "titulo": "Interstellar",
            "genero": "drama",
            "precio_entrada": 6000.0,
        },
        {
            "id": 9,
            "titulo": "Jurassic Park",
            "genero": "acción",
            "precio_entrada": 7200.0,
        },
        {
            "id": 10,
            "titulo": "Pulp Fiction",
            "genero": "drama",
            "precio_entrada": 6500.0,
        },
    ]

    reservas = []

    while True:
        opcion = menu.menu_principal()

        if opcion == 0:
            break
        elif opcion == 1:
            pl.mostrar_cartelera(peliculas)
        elif opcion == 2:
            pl.buscador(peliculas)
        elif opcion == 3:
            rs.crear_reserva(peliculas, reservas)
        elif opcion == 4:
            rs.listar_reservas(reservas)
        elif opcion == 5:
            rs.cancelar_reservas(reservas)


if __name__ == "__main__":
    main()
