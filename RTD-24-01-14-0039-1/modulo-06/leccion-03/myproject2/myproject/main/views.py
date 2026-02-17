from django.shortcuts import render

# Create your views here.

USUARIO = {
    'username':'christian',
    'password':1234
}

## ESTO ES UN LOGIN FICTICIO ASI NO SE HACE !!! ##
def login(request):

    if request.method == 'GET':
        return render(request, 'login.html')
    
    else:
        username = request.POST['username']
        pswd = request.POST['password']
        pswd = int(pswd) if pswd else ''

        if not (username and pswd):
            return render(request, 'login.html',context={
                'mensaje':'ingresa el usuario y la contraseña'
            })
        
        if username == USUARIO['username'] and pswd == USUARIO['password']:
            return render(request, 'perfil.html', context={'usuario':USUARIO})
        else:
            return render(request, 'login.html',context={
                'mensaje':'usuario o contraseña incorrecta'
            })