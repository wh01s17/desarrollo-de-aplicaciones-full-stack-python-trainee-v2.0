#### Colaboracion ###

# class Pelota:

#     def __init__(self):
#         self.c_botes = 0

#     def dar_bote(self):
#         self.c_botes += 1
#         print(f'La pelota dio un bote, ha dado {self.c_botes} en total')


# class Brocacochi:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad

#     def jugar(self, pelota:Pelota):
#         pelota.dar_bote()


# n1 = Brocacochi('jordy', 2)
# pelota = Pelota()

# n1.jugar(pelota)
# n1.jugar(pelota)
# n1.jugar(pelota)
# n1.jugar(pelota)



### COMPOSICION ###

class Motor:

    def __init__(self, encendido=False):
        self.encendido = encendido

    def encender(self):
        self.encendido = True
        print('El motor esta encendido')

    def apagar(self):
        self.encendido = False
        print('El motor esta apagado')


class Vehiculo:

    def __init__(self, patente, modelo, motor:Motor):
        self.patente = patente
        self.modelo = modelo
        if isinstance(motor, Motor):
            self.motor = motor
        else:
            raise TypeError('Entregaste un tipo de motor incorrecto')

    def encender(self):
        self.modelo.encender()


m1 = Motor()
v1 = Vehiculo('JJMN-25', 'Lada', 'm1')
