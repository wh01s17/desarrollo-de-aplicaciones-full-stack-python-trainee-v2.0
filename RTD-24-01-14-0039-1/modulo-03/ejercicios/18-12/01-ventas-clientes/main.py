# Ejercicio 2: Sistema de Ventas y Clientes con Validación de RUT
# Contexto:
# Un pequeño negocio necesita un sistema en consola para registrar clientes y ventas realizadas durante el día.

# Objetivo:
# Crear una aplicación que permita registrar clientes con RUT, ingresar ventas y generar reportes simples.

# Menú principal:
# 1. Registrar cliente
# 2. Registrar venta
# 3. Ver ventas totales
# 4. Ver ventas por cliente
# 5. Salir

# 1. Registrar cliente:
# - Solicitar nombre del cliente
# - Solicitar RUT
# - Validar formato del RUT
# - Almacenar clientes en un diccionario

# 2. Registrar venta:
# - Solicitar RUT del cliente
# - Validar que el cliente exista
# - Solicitar monto de la venta
# - Solicitar medio de pago (efectivo, débito, crédito)
# - Guardar ventas en una lista de diccionarios

# 3. Ver ventas totales:
# - Total de ventas realizadas
# - Monto total vendido
# - Promedio de venta

# 4. Ver ventas por cliente:
# - Solicitar RUT
# - Mostrar cantidad de compras y monto total asociado

# Desafío adicional (opcional):
# - Mostrar el medio de pago más utilizado
import menu
import clientes as cl
import ventas as vt
import reportes as rp


def main():
    clientes = {
        "12.345.678-9": "Juan Pérez",
        "9.876.543-2": "María González",
        "11.111.111-1": "Pedro Ramírez",
        "22.222.222-2": "Ana Torres",
        "33.333.333-3": "Luis Fernández",
    }

    ventas = [
        {
            "12.345.678-9": [
                {"monto": 15000, "medio_pago": "Débito"},
                {"monto": 22000, "medio_pago": "Crédito"},
            ]
        },
        {"9.876.543-2": [{"monto": 50000, "medio_pago": "Efectivo"}]},
        {"11.111.111-1": [{"monto": 18000, "medio_pago": "Débito"}]},
        {"22.222.222-2": [{"monto": 35000, "medio_pago": "Crédito"}]},
        {"33.333.333-3": [{"monto": 12000, "medio_pago": "Efectivo"}]},
    ]

    medios_pago = ["Efectivo", "Débito", "Crédito"]

    while True:
        opcion = menu.menu_principal()

        if opcion == 6:
            break
        elif opcion == 1:
            cl.registrar_cliente(clientes)
        elif opcion == 2:
            vt.registrar_venta(clientes, ventas, medios_pago)
        elif opcion == 3:
            rp.total_ventas(ventas)
        elif opcion == 4:
            rp.ventas_cliente(ventas, clientes)
        elif opcion == 5:
            rp.mayor_medio_pago(ventas, medios_pago)


if __name__ == "__main__":
    main()
