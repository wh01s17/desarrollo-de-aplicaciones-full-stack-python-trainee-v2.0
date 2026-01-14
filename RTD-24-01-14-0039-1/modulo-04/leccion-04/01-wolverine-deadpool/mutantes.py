"""
🐺 Clase Wolverine (HEREDA DE Personaje)

Representa a Wolverine, caracterizado por su resistencia y
factor de curación.

Características diferenciadoras:
- Mayor cantidad de vida base
- Daño físico constante (sin aleatoriedad)
- Regeneración automática de vida en cada turno

Comportamiento especial:
- Recupera una pequeña cantidad de vida de forma constante
- Su ataque es estable y predecible

Wolverine destaca por su DURABILIDAD.
"""
from personajes import Personaje
import random



class Wolverine(Personaje):

    def __init__(self, nombre, hp, pa):
        super().__init__(nombre, hp, pa)

    def regenerar(self):
        self.hp *= 1.1

    def get_damage(self):
        return self.pa * 0.5


"""
🤡 Clase Deadpool (HEREDA DE Personaje)

Representa a Deadpool, impredecible y caótico.

Características diferenciadoras:
- Menor vida base que Wolverine
- Ataques con daño variable (aleatorio)
- Posibilidad de golpes críticos o fallos

Comportamiento especial:
- Puede infligir daño extra o fallar ataques
- Su regeneración es inestable, pero potencialmente más alta

Deadpool destaca por su IMPREVISIBILIDAD.
"""


class Deadpool(Personaje):

    def __init__(self, nombre, hp, pa):
        super().__init__(nombre, hp, pa)

    def regenerar(self):
        self.hp *= random.choice([1, 1.1, 1.2, 1.3])

    def get_damage(self):
        return self.pa * random.choice([0, 0.3, 0.5, 1, 1.5])

    