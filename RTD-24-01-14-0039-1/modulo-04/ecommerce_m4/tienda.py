from catalogo_clase import Catalogo
from carrito_clase import Carrito
from usuario import Usuario
from admin import Admin
from cliente import Cliente


class Tienda:
    def __init__(self):
        self.catalogo = Catalogo()
        self.usuario_actual = None
        self.carrito = None

    def mostrar_banner(self) -> None:
        cart_ascii = (
            """
⠀⠈⠛⠻⠶⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⢻⣆⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢻⡏⠉⠉⠉⠉⢹⡏⠉⠉⠉⠉⣿⠉⠉⠉⠉⠉⣹⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⣿⣀⣀⣀⣀⣸⣧⣀⣀⣀⣀⣿⣄⣀⣀⣀⣠⡿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⠀⠀⠀⢸⡇⠀⠀⠀⠀⣿⠁⠀⠀⠀⣿⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣧⣤⣤⣼⣧⣤⣤⣤⣤⣿⣤⣤⣤⣼⡏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠀⢸⡇⠀⠀⠀⠀⣿⠀⠀⢠⡿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣷⠤⠼⠷⠤⠤⠤⠤⠿⠦⠤⠾⠃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⣷⢶⣶⠶⠶⠶⠶⠶⠶⣶⠶⣶⡶⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⣠⡿⠀⠀⠀⠀⠀⠀⢷⣄⣼⠇
"""
            + "\033[0m"
        )

        print("\n\033[32m" + ("=" * 60))
        print("🛒 BIENVENIDO A PYTHON-SHOP 🛒".center(60))
        print("=" * 60)
        print(cart_ascii)

    def seleccionar_rol(self) -> Usuario:
        while True:
            print("\n" + "=" * 60)
            print("SELECCIONE SU ROL".center(60))
            print("=" * 60)
            print("1) 👨‍💼 Administrador")
            print("2) 👤 Cliente")
            print("0) Salir")

            try:
                opcion = input("\nIngrese su opción: ").strip()

                if opcion == "1":
                    return Admin()
                elif opcion == "2":
                    return Cliente()
                elif opcion == "0":
                    print("👋 ¡Hasta luego!")
                    return None
                else:
                    print("Opción inválida. Por favor, elija 1, 2 o 0.")

            except Exception as e:
                print(f"Error: {e}")

    def pedir_opcion(self) -> int:
        try:
            opcion = input("Ingrese su opción: ").strip()
            return int(opcion)
        except ValueError:
            print("Debe ingresar un número válido")
            return -1

    def ejecutar(self) -> None:
        self.mostrar_banner()

        self.usuario_actual = self.seleccionar_rol()

        if self.usuario_actual is None:
            return

        if isinstance(self.usuario_actual, Cliente):
            self.carrito = Carrito()

        while True:
            self.usuario_actual.mostrar_menu()
            opcion = self.pedir_opcion()

            if isinstance(self.usuario_actual, Admin):
                continuar = self.usuario_actual.ejecutar_opcion(opcion, self.catalogo)
            else:
                continuar = self.usuario_actual.ejecutar_opcion(
                    opcion, self.catalogo, self.carrito
                )

            if not continuar:
                break

        print("\n✨ Gracias por usar PYTHON-SHOP ✨\n")
