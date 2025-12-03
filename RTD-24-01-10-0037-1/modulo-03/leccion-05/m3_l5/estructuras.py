# 1. Crear estructuras
# Lista (list) - mutable, permite modificar sus elementos
mi_lista = [1, 2, 3]
print("Lista:", mi_lista)

# Tupla (tuple) - inmutable, no permite cambios una vez creada
mi_tupla = (10, 20, 30)
print("Tupla:", mi_tupla)

# Conjunto (set) - no tiene orden y no permite elementos duplicados
mi_conjunto = {"a", "b", "c"}
print("Conjunto:", mi_conjunto)

# Diccionario (dict) - almacena pares clave:valor
mi_diccionario = {"nombre": "wh01s17", "edad": 32, "ciudad": "Cartagena"}
print("Diccionario:", mi_diccionario)


# 2. Acceder a elementos
print("Segundo elemento de la lista:", mi_lista[1])

print("clave:valor del diccionario")
valor = mi_diccionario["nombre"]
print("Clave: nombre")
print("Valor:", valor)

# No puedes acceder por índice a un set en Python porque los sets no tienen orden y no garantizan ninguna posición fija, y el índice implica posición


# 3. Contar e iterar
print("Cantidad de elementos de lista:", len(mi_lista))
print("Cantidad de elementos de tupla:", len(mi_tupla))
print("Cantidad de elementos de set:", len(mi_conjunto))
print("Cantidad de elementos de diccionario:", len(mi_diccionario))

print("\nElementos en Lista")
for elemento in mi_lista:
    print(elemento)

print("\nElementos en Tupla")
for elemento in mi_tupla:
    print(elemento)

print("\nElementos en Set (conjunto)")
for elemento in mi_conjunto:
    print(elemento)

print("\nElementos en Diccionario")
for elemento in mi_diccionario.values():
    print(elemento)


# 4. Modificar estructuras
# Agrega un nuevo elemento a la lista y al conjunto.
mi_lista.append(4)
print("Nuevo elemento en lista:", mi_lista)

mi_conjunto.add("d")
print("Nuevo elemento en set:", sorted(mi_conjunto))

# Borra un elemento de la lista.
mi_lista.pop()
print("Elemento eliminado en lista:", mi_lista)

# Agrega una nueva clave al diccionario.
mi_diccionario["lenguaje"] = "Python"
print("Diccionario con nuevo elemento:", mi_diccionario)

# La tupla no se puede modificar, ya que por definción, son estructuras de datos inmutables
