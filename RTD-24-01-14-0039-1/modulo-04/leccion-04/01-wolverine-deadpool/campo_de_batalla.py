"""
🏟️ Clase CampoDeBatalla

Representa el entorno donde ocurre la pelea.

Responsabilidades principales:
- Recibir a los personajes combatientes
- Controlar los turnos
- Ejecutar el flujo del combate
- Mostrar los eventos en consola
- Determinar cuándo termina la pelea y quién es el ganador

⚠️ El CampoDeBatalla NO ataca ni recibe daño.
Su rol es coordinar la interacción entre los objetos,
fomentando la COLABORACIÓN entre clases.
"""

from mutantes import Wolverine, Deadpool
from time import sleep


class CampoBatalla:
    def __init__(self, mutante1, mutante2):
        self.mutante1 = mutante1
        self.mutante2 = mutante2

    def run(self):
        while True:
            damage_w = self.mutante1.get_damage()
            self.mutante1.atacar(d, damage_w)
            d.regenerar()
            if not self.mutante2.esta_vivo:
                print("Ganó Wolverine")
                break
            sleep(1)

            damage_d = self.mutante2.get_damage()
            self.mutante2.atacar(w, damage_d)
            self.mutante1.regenerar()
            if not self.mutante1.esta_vivo:
                print("Ganó Deadpool")
                break
            sleep(1)


w = Wolverine("Logan", 500, 80)
d = Deadpool("Wade Wilson", 300, 80)
cb = CampoBatalla(w, d)

cb.run()
