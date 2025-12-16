#unitario
-1 
#binario
True and False
palabra = 'Hola'
1+2

#ternario
"Mayor de edad" if 20 >= 18 else "Menor de edad"


# ============================================================
# PROGRAMACIÓN FUNCIONAL EN PYTHON
# List Comprehensions, Lambda, Map, Filter, Zip e If en una línea (ternarias)
# ============================================================

# ------------------------------------------------------------
# 1) LIST COMPREHENSION 
# ------------------------------------------------------------
# Es una forma compacta y más legible de construir listas.
# Sintaxis:
# nueva_lista = [ expresión for elemento in iterable ]
# También se pueden agregar condiciones.

# Ejemplo básico:
numeros = [1, 2, 3, 4, 5]

cuadrados = [ n**2 for n in numeros ]  # Elevar cada número al cuadrado
print("Cuadrados:", cuadrados)

# Ejemplo con condición (solo pares):


pares = [ 
    n for n in numeros 
    if n % 2 == 0 
]
print("Pares:", pares)

# Ejemplo práctico: transformar strings
palabras = ["python", "es", "poderoso"]
mayusculas = [p.upper() for p in palabras]
print("Mayúsculas:", mayusculas)


# ------------------------------------------------------------
# 2) IF EN UNA SOLA LÍNEA (EXPRESIONES TERNARIAS)
# ------------------------------------------------------------
# Sintaxis:
# valor_si_verdadero if condicion else valor_si_falso

edad = 20
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
print("Resultado IF:", mensaje)

# Combinado con list comprehension (ejemplo de label):
clasificacion = ["Par" if n % 2 == 0 else "Impar" for n in numeros]
print("Clasificación de números:", clasificacion)


# ------------------------------------------------------------
# 3) LAMBDA FUNCTIONS
# ------------------------------------------------------------
# Son funciones pequeñas sin nombre, útiles para funciones simples.
# Sintaxis:
# lambda argumentos: expresión
# Generalmente se usan con map, filter y sorted.

sumar = lambda a, b: a + b
print("Lambda sumar:", sumar(3, 4))

# Lambda con condicion simple
es_par = lambda x: "Par" if x % 2 == 0 else "Impar"
print("Lambda es_par(5):", es_par(5))


# ------------------------------------------------------------
# 4) MAP()
# ------------------------------------------------------------
# Aplica una función a cada elemento de un iterable.
# Sintaxis: map(función, iterable)

dobles = list( map(lambda x: x * 2, numeros) )
print("Doble con map:", dobles)

# Ejemplo práctico: pasar a mayúsculas
mayus_map = list(map(lambda w: w.upper(), palabras))
print("Mayúsculas con map:", mayus_map)


# ------------------------------------------------------------
# 5) FILTER()
# ------------------------------------------------------------
# Filtra elementos según una condición.
# Sintaxis: filter(función_condición, iterable)

solo_pares = list(filter(lambda x: x % 2 == 0, numeros))
print("Filter solo pares:", solo_pares)

# Ejemplo práctico: filtrar palabras largas
largas = list(filter(lambda w: len(w) > 5, palabras))
print("Palabras largas:", largas)


# ------------------------------------------------------------
# 6) ZIP()
# ------------------------------------------------------------
# Une varios iterables en tuplas. Útil para tablas, pares clave-valor, etc.
# Sintaxis: zip(iterable1, iterable2, ...)

nombres = ["Ana", "Luis", "Pedro"]
edades = [22, 30, 25]
ciudades = ["Santiago", "México", "Lima"]

datos = list( zip(nombres, edades, ciudades) )
print("Datos combinados con zip:", datos)

# Practico: convertir a diccionario
diccionario = dict(zip(nombres, edades))
print("Diccionario nombre-edad:", diccionario)


# ------------------------------------------------------------
# EXTRA: COMBINAR TODO 💡
# ------------------------------------------------------------
# Ejemplo: Estudiantes con notas, filtrar aprobados y obtener mensaje

estudiantes = ["Juan", "Camila", "Sofía", "Pedro"]
notas = [55, 80, 49, 92]

# 1. Combinar datos
registro = list(zip(estudiantes, notas))

# 2. Filtrar aprobados (>= 60)
aprobados = list(filter(lambda x: x[1] >= 60, registro))

# 3. Crear mensaje con list comprehension e if
mensajes = [f"{nombre} aprobó con {nota}" for nombre, nota in aprobados]
print("\nRESULTADO FINAL (COMBINANDO TODO):")
print("\n".join(mensajes))

# ------------------------------------------------------------
# FIN DEL DOCUMENTO
# ------------------------------------------------------------

