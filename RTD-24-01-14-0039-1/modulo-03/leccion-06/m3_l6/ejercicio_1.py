input_user = int(input("Ingrese un numero entre 1 y 100:\n"))

while input_user < 1 or input_user > 100:
    input_user = int(input("Error, ingrese un numero entre 1 y 100:\n"))

for i in range(input_user, 101, 2):
    print(i, end=" ")
