capital_inicial = int(input("Ingrese su capital inicial: $"))
tasa_interes = float(input("Ingresa la tasa de interes anual (%): "))
anios = float(input("Ingrese cantidad de años: "))

monto_final = capital_inicial * (1 + (tasa_interes / 100) * anios)

print(f"Monto final: ${monto_final:,.2f}")
