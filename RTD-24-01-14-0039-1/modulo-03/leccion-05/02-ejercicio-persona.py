persona = {}

while True:
    clave = input(
        "Ingresa el tipo de dato (nombre, edad, etc.) o 'salir' para terminar: "
    ).strip()
    if clave.lower() == "salir":
        break

    valor = input(f"Ingresa el valor para '{clave}': ").strip()
    persona[clave] = valor

    print("Contenido actual del diccionario:")
    print(persona)
    print("-" * 40)
