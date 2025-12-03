ingrediente = ""
tipo_pizza = ""

print("Bienvenido a Pizzería Bella Napoli")
print("Todas las pizzas incluyen mozzarella, tomate y puede elegir un ingrediente más")
input_user = input("Desea una pizza vegetariana? (s/n): ").lower()

if input_user == "s":
    tipo_pizza = "es vegetariana"
    print("Ingredientes vegetarianos:")
    print("1. Pimiento")
    print("2. Tofu")
    opc_ingrediente = int(input("Seleccione su ingrediente: "))

    if opc_ingrediente == 1:
        ingrediente = "Pimiento"
    elif opc_ingrediente == 2:
        ingrediente = "Tofu"
    else:
        print("Opción inválida")

else:
    tipo_pizza = "NO es vegetariana"
    print("Ingredientes no vegetarianos:")
    print("1. Peperoni")
    print("2. Jamón")
    print("3. Salmón")
    opc_ingrediente = int(input("Seleccione su ingrediente: "))

    if opc_ingrediente == 1:
        ingrediente = "Peperoni"
    elif opc_ingrediente == 2:
        ingrediente = "Jamón"
    elif opc_ingrediente == 3:
        ingrediente = "Salmón"
    else:
        print("Opción inválida")

if ingrediente:
    print(f"Su pizza {tipo_pizza} y contiene Mozzarella, Tomate y {ingrediente}")
