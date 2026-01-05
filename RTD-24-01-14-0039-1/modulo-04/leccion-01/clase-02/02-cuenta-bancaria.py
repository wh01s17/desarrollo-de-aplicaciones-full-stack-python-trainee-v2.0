# --------------------------------------------------
# EJERCICIO 2: CUENTABANCARIA
# --------------------------------------------------
# Objetivo:
# Aplicar atributos de clase y métodos estáticos en un contexto financiero simple.
# Debe crear una clase CuentaBancaria con:

# Atributo de clase:
# - banco = "Banco Python"

# Atributos de instancia:
# - titular
# - saldo

# Métodos:
# - depositar(monto): suma el monto al saldo
# - retirar(monto): resta el monto si hay saldo suficiente
# - mostrar_saldo(): imprime el saldo actual
# - es_monto_valido(monto): método estático que retorna True si monto > 0

# Tareas:
# 1. Crear la clase CuentaBancaria.
# 2. Crear 1 instancia con saldo inicial.
# 3. Realizar al menos 2 depósitos.
# 4. Realizar 1 retiro.
# 5. Mostrar el saldo final.
# 6. Mostrar el nombre del banco usando el atributo de clase.


class CuentaBancaria:
    BANCO = "Banco Python"

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        if not self.es_monto_valido(monto):
            print("Monto inválido")
            return

        print("==================")
        print(f"Deposito: ${monto}")
        print("==================")

        self.saldo += monto

    def retirar(self, monto):
        if not self.es_monto_valido(monto):
            print("Monto inválido")
            return

        if self.saldo < monto:
            print("Saldo insuficiente")
            return

        print("===================")
        print(f"Retiro: ${monto}")
        print("===================")

        self.saldo -= monto

    def mostrar_saldo(self):
        print(f"Su saldo es ${self.saldo}")

    @staticmethod
    def es_monto_valido(monto):
        return monto > 0


cuenta = CuentaBancaria("Steven Wilson", 150000)
cuenta.mostrar_saldo()

cuenta.depositar(2000)
cuenta.depositar(12000)
cuenta.retirar(50000)

cuenta.mostrar_saldo()

print(f"Nombre del banco: {CuentaBancaria.BANCO}")
