f = open("archivo1.txt", "r", encoding="utf-8")
contenido = f.readlines()
print(contenido)
f.close()


with open("archivo1.txt", "r", encoding="utf-8") as f:
    contenido = f.read()
    print(contenido)
    print(f.fileno())
