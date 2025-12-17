"""
✅ Ejercicio 1: Sistema de Gestión de Reservas de Salas

Una empresa tiene 3 salas disponibles para reuniones: Sala Norte, Sala Sur y Sala Centro.
Cada sala puede tener varias reservas durante el día, pero las horas no pueden repetirse.
Debes crear un programa que permita:
    - Registrar una reserva indicando:
        Nombre del usuario
        Sala a reservar
    - Hora (entero entre 8 y 20)
    - Evitar reservas duplicadas en la misma sala y a la misma hora.
    - Mostrar todas las reservas registradas por sala.
    - Salir del sistema cuando el usuario lo indique.

Requisitos
El programa debe estar organizado con funciones claras:
mostrar_menu()
registrar_reserva(reservas)
mostrar_reservas(reservas)
main()
"""

import menu
import reservas as re
import os


def main():
    salas = ["Sala Norte", "Sala Sur", "Sala Centro"]
    reservas = {sala: [] for sala in salas}

    while True:
        os.system("clear")
        opcion = menu.mostrar_menu()

        if opcion == 3:
            print("Saliendo del sistema...")
            break

        elif opcion == 1:
            re.registrar_reserva(reservas, salas)

        elif opcion == 2:
            re.mostrar_reservas(reservas)


main()
