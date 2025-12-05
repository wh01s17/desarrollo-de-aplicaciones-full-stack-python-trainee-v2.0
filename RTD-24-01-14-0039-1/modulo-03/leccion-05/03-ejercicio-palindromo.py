palabra = input("Ingresa una palabra: ").strip().lower()

if palabra == palabra[::-1]:
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")
