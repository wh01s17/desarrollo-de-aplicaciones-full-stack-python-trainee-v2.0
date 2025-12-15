import operaciones.div as div
import resta
import suma as s
from multi import multiplicar
from tomar_datos import datos


def main():
    while True:
        opcion = input("""
    Dime:
    1 si quieres sumar
    2 si quieres restar
    3 si quieres multiplicar
    4 si quieres dividir
    5 para salir
    """)

        if opcion == "5":
            break

        elif opcion == "1":
            numero1, numero2 = datos()
            print(s.sumar(numero1, numero2))

        elif opcion == "2":
            numero1, numero2 = datos()
            print(resta.restar(numero1, numero2))

        elif opcion == "3":
            numero1, numero2 = datos()
            print(multiplicar(numero1, numero2))

        elif opcion == "4":
            numero1, numero2 = datos()
            print(div.dividir(numero1, numero2))


if __name__ == "__main__":
    main()
