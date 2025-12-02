"""
Escribir un programa que pregunte el nombre del usuario en la consola y
despues de que el usuario lo intriduzca, muestre por pantalla <NOMBRE> tiene <n> letras,
donde <NOMBRE> es el nombre de usuairo en mayusculas y <n> es el numero de letras que tienen el nombre.
"""

# Entrada
nombre = input("Dime tu nombre: ")

# Proceso
largo_nombre = len(nombre)

nombre_mayusculas = nombre.upper()

# Salida
print(
    f"Tu nombre en letras mayusculas es: {nombre_mayusculas}, y tiene {largo_nombre} letras"
)
