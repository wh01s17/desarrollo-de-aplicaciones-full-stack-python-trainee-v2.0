"""
open(file, mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
Abre file y retorna un file object correspondiente. Si el archivo no se puede abrir, se lanza un OSError. 
Consulte Leyendo y escribiendo archivos para obtener más ejemplos de cómo utilizar esta función.
file es un path-like object que da la ruta (absoluta o relativa al directorio de trabajo actual) 
del fichero a ser abierto o un descriptor de fichero entero del fichero a ser envuelto. 
(Si un descriptor de fichero es dado, será cerrado cuando el objeto de entrada-salida sea cerrado, 
a menos que closefd esté puesto a False.)mode es una cadena de caracteres opcional que especifica el modo en el cual el fichero es abierto. 
Su valor por defecto es 'r' que significa que está abierto para lectura en modo texto. Otros valores comunes son ’w’ para escritura 
(truncando el fichero si ya existe), ’x’ para creación en exclusiva y ’a’ para añadir (lo que en algunos sistemas Unix implica que toda 
la escritura añade al final del fichero independientemente de la posición de búsqueda actual). En modo texto, 
si no se especifica encoding entonces la codificación empleada es dependiente de plataforma: se invoca a locale.getencoding() 
para obtener la codificación regional actual. (Para lectura y escritura de bytes en crudo usa el modo binario y deja encoding sin especificar). 
Los modos disponibles son:

Carácter        Significado
’r’         abierto para lectura (por defecto)
'w'         abierto para escritura, truncando primero el fichero
'x'         abierto para creación en exclusiva, falla si el fichero ya existe
’a’         abierto para escritura, añadiendo al final del fichero si este existe
'b'         modo binario
’t’         modo texto (por defecto)
’+’         abierto para actualizar (lectura y escritura)
El modo por defecto es ’r’ (abierto para lectura de texto, sinónimo de ’rt’. Los modos ’w+’ y ’w+b’ abren y truncan el fichero. Los modos ’r+’ y ’r+b’ abren el fichero sin truncarlo.

Como se menciona en Resumen, Python distingue entre I/O binario y de texto. Los ficheros abiertos en modo binario (incluyendo ’b’ en el argumento mode) 
retornan su contenido como objetos de bytes sin ninguna descodificación. En modo de texto (por defecto, o cuando se incluye ’t’ en el argumento mode), 
los contenidos del fichero se retornan como str, tras descodificar los bytes usando una codificación dependiente de plataforma o usando el encoding especificado como argumento.
"""

#BUENAS PRACTICAS!!!!!

#lista = ['Carlos', 'Valentina', 'Maria','Migue','Dominique']


# print(range(10000))


# i= 0
# while i < len(lista):
#     print(lista[i]) 


# for i in range(len(lista)): #__iter__
#     print(lista[i])



# for i in lista:
#     print(i)






#print(r'carpeta1\texto.txt')
#print('carpeta1\\texto.txt')


"""
\n
\t tab
\r 
"""

import os

# os.system('ls')

os.chdir('manejo_archivos')
# os.system('ls')

# texto = open('test.txt', 'r')

#print(texto)
# print(dir(texto))

# print(texto.name)
# print(texto.closed)


# print(texto.read())


# print(texto.readline()) # __iter__
# print(texto.readline())
# print(texto.readline())
# print(texto.readline())
# print(texto.readline())


# print(texto.readlines())
# print(texto.readlines())


##objeto como iterable
# texto_list = list(texto)
# print(texto_list[3].replace('\n',''))

# for i in texto:
#     print(i, end='') #\n

# print(texto.read(10))
# print(texto.read(10))
# print(texto.read(10))
# print(texto.read(10))
# texto.close()




# escritura = open('new_file.txt', 'w')


# for i in range(10):
#     escritura.write(f'nuevo mensaje numero: {i+1}\n')

# escritura.close()


"""
Buenas practicas con relacion a los archivos
En el código anterior podemos ver como existe la llamada close(). 
La intención de este código es buena, porque se cierra el fichero abierto, 
pero el problema es que sólo se cerrará si f.read() funciona correctamente. 
Es decir, si existe un error en la función f.read(), el programa terminará 
y el cierre del fichero no se producirá.
Por lo tanto, una de las mejores formas de asegurarnos de que el fichero 
se cierra correctamente, pase lo que pase, es la siguiente haciendo uso de with.
"""

# try:
#     archivo = open('datos.cvs', 'r')
#     archivo.close()
# except FileExistsError:
#     print("El archivo datos.cvs existe o a sido creadopreviamente")
# except Exception as error:
#     print('Se ha generado un error no considerado')


# with open("test.txt") as my_file:
#     file_list = list(my_file)
#     print(my_file.read())


# print(file_list)


import csv #comma separated values


"""
Nombre,Apellido
Miguel,Serrano
Dominique,Reyes
"""

#excel --> guardar como --> csv
#pandas --> pandas.read_excel()
#xlsd --> excel
#pandas --> R


with open('bd_bc_interes.csv') as bd:
    data = csv.reader(bd, delimiter=';')
    data = list(data)


# # print(data)
# for i in data:
#     print(i)
# consumo = []


with open('Lista.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter.writerow(['Nombre', 'Apelido'])
    spamwriter.writerow(['Christian','Donoso'])
    spamwriter.writerow(['Christian','Donoso'])
    spamwriter.writerow(['Christian','Donoso'])
    spamwriter.writerow(['Christian','Donoso'])
    spamwriter.writerow(['Christian','Donoso'])
    spamwriter.writerow(['Christian','Donoso'])
    spamwriter.writerow(['Christian','Donoso'])
    spamwriter.writerow(['Christian','Donoso'])






