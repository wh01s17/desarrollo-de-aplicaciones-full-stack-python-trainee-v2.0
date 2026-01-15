"""
¿QUÉ ES UNA EXCEPCIÓN?
Python utiliza un objeto especial llamado excepción para controlar cualquier error que pueda ocurrir
durante la ejecución de un programa.
Una declaración o expresión estando sintácticamente correcta, puede generar un error cuando se
intenta ejecutar. Los errores detectados durante la ejecución se llaman excepciones.
Cuando ocurre un error durante la ejecución de un programa, Python crea una excepción. Si esta no
se controla, la ejecución del programa se detiene y se muestra el error (traceback)
"""

###tipos de excepciones

# 1/0
# print('Hola mundo')
# 2 + variable
# 2 + '2'

"""
Principales
• TypeError: ocurre cuando se aplica una operación o función a un dato del tipo inapropiado.
• ZeroDivisionError: ocurre cuando se intenta dividir por cero.
• OverflowError: ocurre cuando un cálculo excede el límite para un tipo de dato numérico.
• IndexError: ocurre cuando se intenta acceder a una secuencia con un índice que no existe.
"""


# lista = [1,2,3,5]
# print(lista[6])
"""
• KeyError: ocurre cuando se intenta acceder a un diccionario con una clave que no existe.
• FileNotFoundError: ocurre cuando se intenta acceder a un fichero que no existe en la ruta
indicada.
• ImportError: ocurre cuando falla la importación de un módulo.



Error de sintaxis
"""

# if True:
#     print('Hola' 'Mundo')

"""
MANEJO DE EXCEPCIONES
Para el manejo de excepciones los lenguajes proveen ciertas palabras reservadas, los cuales
permiten manejar las excepciones que puedan surgir, y tomar acciones de recuperación para evitar
la interrupción del programa o, al menos, para realizar algunas acciones adicionales antes de
interrumpirlo.
En el caso de Python, el manejo de excepciones se hace mediante los bloques que utilizan las
sentencias try, except y finally.

LA SENTENCIA TRY/EXCEPT
Dentro del bloque try se ubica todo el código que pueda llegar a levantar una excepción, y se utiliza
el término levantar para referirse a la acción de generar una excepción.
A continuación, se ubica el bloque except, el cual se encarga de capturar la excepción, y nos da la
oportunidad de procesarla mostrando, por ejemplo, un mensaje adecuado al usuario. Veamos qué
sucede si se quiere realizar una división por cero
"""

numerador = 4
denominador = 0

# numerador / denominador

# if
# else

# try:         #4/0
#     numerador / denominador #excepciopn AKA error
#     print('No ocurrio ni un error')
# except:
#     print('No se admite la division por cero')

# print('Programa finalizado')
# print('Programa finalizado')
# print('Programa finalizado')
# print('Programa finalizado')
# print('Programa finalizado')

# [0,1,2,3,4]
# lista = [i for i in range(5)]

# for i in lista:
#     # print(10/i)
#     try:
#         print(10/i)
#     except:
#         pass

# print(lista)

##NO ABUSAR DE LAS EXCEPCIONES

# numero = input('dime un numero:')

# if str(numero).isdigit():
#     numero = int(numero)
# elif str(numero).isdecimal():
#     numero = float(numero)
# else:
#     print('no me diste un numero')

# print(numero)


"""
Dado que dentro de un mismo bloque try pueden producirse excepciones de distinto tipo, es posible
utilizar varios bloques except, cada uno para capturar un tipo distinto de excepción.
Esto se hace especificando, a continuación de la sentencia except, el nombre de la excepción que se
pretende capturar. Un mismo bloque except puede atrapar varios tipos de excepciones, lo cual se
hace especificando los nombres de las excepciones separados por comas luego de la palabra
except. Es importante destacar que, si bien luego de un bloque try puede haber varios bloques except,
se ejecutará, a lo sumo, uno de ellos.
"""

# try:
#     1/'0'
# except ZeroDivisionError:
#     print('No se puede dividir por cero')

# print('Programa finalizado')

# Apartado 2: Gestión de distintos tipos de excepciones
# frutas = ["0-Plátano", "1-Manzana", "2-Pera", "3-Melocotón"]

# def elegirFruta(listaFrutas):
#     try:
#         print(listaFrutas)
#         index = int(input("¿Cual es tu fruta favorita? "))
#         print(f"Tu fruta favorita es: {listaFrutas[index]}")
#     except IndexError:
#         print("Esa posición no existe!")
#     except ValueError: #Exception
#         print(f"Tienes que poner un número entre 0 y {len(listaFrutas)-1}")

# elegirFruta(frutas)
# print('programa finalizado')

#   Apartado 3: Excepción Exception.
#   Las excepciones son objetos que heredan de la clase Exception.
# frutas = ["0-Plátano", "1-Manzana", "2-Pera", "3-Melocotón"]

# def elegirFruta(listaFrutas):
#     try:
#         print(listaFrutas)
#         index = int(input("¿Cual es tu fruta favorita? "))
#         print(f"Tu fruta favorita es: {listaFrutas[index]}")
#     except Exception as nombreDelError:
#         print(nombreDelError)


# elegirFruta(frutas)
# print('Programa finalizado')


# try:
#     3 + '4'
# except ZeroDivisionError:
#     print('No se puede dividir por cero')
# except:
#     print('Algun otro error')


"""
PARTE 2:

EXCEPCIONES DEFINIDAS POR EL USUARIO
Los programas pueden nombrar sus propias excepciones creando una nueva clase excepción. Las
excepciones, típicamente, deberán derivar de la clase Exception, directa o indirectamente.
La mayoría de las excepciones se definen con nombres acabados en «Error», de manera similar a la
nomenclatura de las excepciones estándar.
Muchos módulos estándar definen sus propias excepciones para reportar errores que pueden ocurrir
en funciones propias. 
"""

# class DividirPorDosError(Exception):
#     def __str__(self) -> str:
#         return 'No se pueden realizar divisiones con el numero 2 en el denominador'


# def division(a,b):
#     if b == 2:
#         raise DividirPorDosError()
#     else:
#         return a / b
#     try:
#         if b == 2:
#             raise DividirPorDosError()
#         else:
#             return a / b
#     except:
#         print('error')

# print(division(15,2))
# print('la funcion finalizo')


##ejemplo 2

# class StringError(Exception):
#     def __init__(self, valor) -> None:
#         self.valor = valor

#     def __str__(self) -> str:
#         return f'Ingresaste un valor incorrecto: {self.valor} --> {str(type(self.valor)).replace("<","").replace(">","")}'


# def validate_str(cadena):
#     if isinstance(cadena,str):
#         if str(cadena).isdigit():
#             raise StringError(cadena)
#         else:
#             return cadena
#     else:
#         raise StringError(cadena)


# class Persona:
#     def __init__(self, nombre,apellido) -> None:
#         self.nombre = validate_str(nombre)
#         self.apellido = validate_str(apellido)


# p = Persona(True, 'Serrano')
# print(p.nombre)
# print(p.apellido)


##FINALY

# try:
#     for i in range(5):
#         if i == 8:
#             raise ValueError('WTF')
#         else:
#             print(i)
# except Exception as e:
#     print(e)
# finally:
#     print('Estamos por terminar')

# print('programa finalizado')


"""
try:
       # Some Code.... 

except:
       # optional block
       # Handling of exception (if required)

else:
       # execute if no exception

finally:
      # Some code .....(always executed)
"""


# # Python code to illustrate
# # working of try()

# def divide(x, y):
#     try:
#         # Floor Division : Gives only Fractional
#         # Part as Answer
#         result = x // y
#     except ZeroDivisionError:
#         print("Sorry ! You are dividing by zero ")
#     else:
#         print("Yeah ! Your answer is :", result)

# # Look at parameters and note the working of Program
# divide(3, 2)
# divide(3, 0)


# # Python code to illustrate
# # working of try()


# def divide(x, y):
#     try:
#         # Floor Division : Gives only Fractional
#         # Part as Answer
#         result = x // y
#     except ZeroDivisionError:
#         print("Sorry ! You are dividing by zero ")
#     else:
#         print("Yeah ! Your answer is :", result)
#     finally:
#         # this block is always executed
#         # regardless of exception generation.
#         print('This is always executed')

# # Look at parameters and note the working of Program
# divide(3, 2)

# print('')
# divide(3, 0)
