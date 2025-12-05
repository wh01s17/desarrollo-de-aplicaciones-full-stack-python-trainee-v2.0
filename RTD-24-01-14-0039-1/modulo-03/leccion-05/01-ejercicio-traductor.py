entrada = input(
    "Ingresa las traducciones (formato palabra:traducción, separadas por comas):\n"
)

diccionario = {}

pares = entrada.split(",")
for par in pares:
    if ":" in par:
        esp, eng = par.split(":")
        diccionario[esp.strip()] = eng.strip()

frase = input("Ingresa una frase en español a traducir:\n")
palabras = frase.split()

traduccion = []
for palabra in palabras:
    traduccion.append(diccionario.get(palabra, palabra))

print("Traducción:")
print(" ".join(traduccion))
