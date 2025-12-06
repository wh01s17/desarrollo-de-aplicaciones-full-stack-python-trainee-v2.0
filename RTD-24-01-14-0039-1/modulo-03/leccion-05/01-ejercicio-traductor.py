palabras_usuario = input(
    "Ingrese palabras en español e inglés separadas por 2 puntos, y cada par esp:eng separadas por comas:\n"
).split(",")

diccionario_eng_esp = {}

for par in palabras_usuario:
    k_esp, v_eng = par.split(":")
    diccionario_eng_esp[k_esp.strip()] = v_eng.strip()

frase = input("Ingrese una frase en español para traducir:\n").split()

traduccion = []
for palabra in frase:
    traduccion.append(diccionario_eng_esp.get(palabra.strip(), palabra.strip()))

print("Traducción:")
print(" ".join(traduccion))
