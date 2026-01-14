"""
-----------------------------------------------------------
🧬 DESCRIPCIÓN DE CLASES Y RESPONSABILIDADES
-----------------------------------------------------------

🧍 Clase Personaje (CLASE BASE)

Representa a cualquier mutante que participe en el combate.

Características comunes:
- Nombre
- Puntos de vida
- Fuerza de ataque base
- Estado (vivo / derrotado)

Comportamiento esperado:
- Atacar a otro personaje
- Recibir daño
- Verificar si sigue con vida
- Mostrar su estado actual

⚠️ Esta clase NO debe utilizarse directamente para el combate
final, solo como base para los personajes concretos.
"""


class Personaje:
    def __init__(self, nombre, hp, pa):
        self.nombre = nombre
        self.hp = hp
        self.pa = pa
        self.esta_vivo = True

    def atacar(self, other, damage):
        other.recibir_damage(damage)
        other.verificar_vida()
        print(other.mostrar_estado())

    def recibir_damage(self, damage):
        self.hp -= damage

    def verificar_vida(self):
        if self.hp <= 0:
            self.esta_vivo = False

    def mostrar_estado(self):
        return f"""
{self.nombre.upper()}
Puntos de vida = {round(self.hp, 2)}
Estado = {"Vivo" if self.esta_vivo else "Muerto"}
"""
