peso = float(input("Ingrse su peso: "))
altura = float(input("Ingrese su estatura (m): "))

# Con round()
imc = round(peso / (altura**2), 2)

print(f"Su IMC es: {imc}")

# string formatting
imc = peso / (altura**2)

print(f"Su IMC es: {imc:.2f}")
