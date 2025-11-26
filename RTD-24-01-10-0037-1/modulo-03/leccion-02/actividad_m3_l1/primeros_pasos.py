import math

"""
1. Imprimir un mensaje inicial
Muestra en pantalla el texto:
"¡Hola! Este es mi primer programa en Python."
"""
print("¡Hola! Este es mi primer programa en Python.")

"""
2. Declarar variables simples
Declara las siguientes variables y muestra su contenido con print():
• Tu nombre
• Tu edad
• Tu ciudad
"""
nombre = "wh01s17"
edad = 32
ciudad = "Cartagena"

print(f"Mi nombre es {nombre}, tengo {edad} años y soy de {ciudad}")

"""
3. Realizar operaciones básicas
Suma dos números y muestra el resultado. Usa comentarios para explicar cada línea.
"""
numero_a = 3
numero_b = 4

print(numero_a + numero_b)

"""
4. Explorar un módulo integrado
Importa el módulo math y utiliza la función sqrt() para calcular la raíz cuadrada de un número.
(Ejemplo: math.sqrt(25) → debe mostrar 5.0)
Agrega comentarios explicativos en tu código para demostrar que comprendes cada instrucción.
"""
num = 25
raiz = math.sqrt(num)
print(f"La raiz cuadrad de {num} es {raiz}")
