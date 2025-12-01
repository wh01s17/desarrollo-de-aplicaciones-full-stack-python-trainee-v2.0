precio = int(input("Ingrese valor de producto: $"))
dcto = float(input("Ingrese porcentaje de descuento: "))

total = precio - ((dcto / 100) * precio)

print(f"Precio normal: {precio}")
print(f"Precio con {dcto}% de descuento: ${total}")
