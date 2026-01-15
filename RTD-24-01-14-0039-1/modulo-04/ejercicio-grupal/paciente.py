class Paciente:
    def __init__(self, nombre: str, apellido: str, peso: int, talla: int) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.peso = peso
        self.talla = talla

        peso_kg = self.peso / 1000
        talla_m = self.talla / 100
        self.imc = round(peso_kg / (talla_m**2), 1)

    def clasificar_imc(self) -> str:
        if self.imc <= 18.5:
            return "Bajo peso"
        elif self.imc < 25:
            return "Normal"
        elif self.imc < 30:
            return "Sobrepeso"
        elif self.imc < 35:
            return "Obesidad I"
        elif self.imc < 40:
            return "Obesidad II"
        else:
            return "Obesidad III"
