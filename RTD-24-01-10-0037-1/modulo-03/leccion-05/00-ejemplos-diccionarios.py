# 1. Diccionario base y cómo se ve por pantalla
# dictionary = {"clave": "valor"}
dictionary = {"a": 1, "b": 2}
print(dictionary["a"])

# 2. Mostrar claves y valores completos
dictionary = {"a": 1, "b": 2}

print("Diccionario completo:", dictionary)
print("Claves:", dictionary.keys())
print("Valores:", dictionary.values())
print("Items:", dictionary.items())

print("Tipos de valores que retornan los métodos")
print(type(dictionary))
print(type(dictionary.keys()))
print(type(dictionary.values()))
print(type(dictionary.items()))

# 3. Método get(), para consultar por clave un elemento, y si no existe, no muestra errores visibles

dictionary = {"a": 1, "b": 2}
print(dictionary.get("a"))
print(dictionary.get("c"))

# 4. Agregar y modificar claves
dictionary = {"a": 1, "b": 2}
dictionary["c"] = 3
dictionary["a"] = 10

print(dictionary)

#  5. Eliminar clave con pop()
dictionary = {"a": 1, "b": 2}
valor_eliminado = dictionary.pop("b")
print("Valor eliminado:", valor_eliminado)
print("Diccionario actualizado:", dictionary)

# 6. Eliminar clave utilizando del
dictionary = {"a": 1, "b": 2}

del dictionary["a"]
print(dictionary)

# 7. Diccionario dentro de una lista
usuarios = [{"nombre": "Julieta", "edad": 44}, {"nombre": "Ursula", "edad": 43}]

for user in usuarios:
    print(f"Nombre: {user['nombre']} | Edad: {user['edad']}")

# 8. Construccion dinámica

# persona = {}
# persona["nombre"] = input("Ingrese su nombre: ")
# persona["edad"] = int(input("Ingrese su edad: "))
# persona["ciudad"] = input("Ingrese su ciudad: ")

# print("Registro ingresado:", persona)

# 9. Eliminar elemento con pop(), indicandole la clave
dictionary = {"a": 1, "b": 2}
valor = dictionary.pop("a")
print(dictionary)

# 10. Eliminar todo el contenido de un diccionario
dictionary = {"a": 1, "b": 2, "c": 3}
valor = dictionary.clear()
print(dictionary)

# 11. El método update() de los diccionarios, sirve para agregar o actualizar pares clave:valor desde otro diccionario u otra estructura compatible.
dict_1 = {"a": 1, "b": 2}
dict_2 = {"c": 3}
dict_1.update(dict_2)
print(dict_1)
