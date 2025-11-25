# Ejercicio 1
# Funcion for()

nombres = ["Ana", "Pedro", "Julieta", "Ursula"]

for nombre in nombres:
    print(nombre.upper())

# Ejercicio 2 - Mostrar solo numeros pares del 1 al 20
for numero in range(1,21):
    if (numero %2 == 0):
        print('par: ',numero)
    else:
        print('impar: ',numero)
