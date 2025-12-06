import statistics as st

nums = input("Ingrese una secuencia de numeros separados por una coma (,):\n").split(
    ","
)

nums = [int(n.strip()) for n in nums]

media = st.mean(nums)

desviacion_tipica = st.stdev(nums, media)

print(f"Media: {media}")
print(f"Desviación típica: {desviacion_tipica}")
