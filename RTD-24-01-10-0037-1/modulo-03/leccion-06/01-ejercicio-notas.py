def promedio_notas(notas):
    return sum(notas) / 3


notas = [4.5, 6.2, 5.5]
promedio = promedio_notas(notas)
print(f"El promedio es: {promedio:.2f}")
