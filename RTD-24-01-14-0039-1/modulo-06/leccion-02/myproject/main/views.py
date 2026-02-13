from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


#una vista es una funcion que recibe a la request
# y retorna una respuesta
def index(request):
    return HttpResponse('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Hola Christian Donoso</h1>
    <p>Profesion</p>
    <ul>
        <li>Kinesiologo</li>
        <li>Ingeniero civil industrial</li>
    </ul>
</body>
</html>
''')


def perfil(request):
    fullname = 'Christian Donoso'
    profesiones = ['Kinesiologo', 'Ingeniero Civil Industrial', 'pintor']
    return render(request, 'perfil.html', context={
        'fullname':fullname,
        'profesiones':profesiones
    })