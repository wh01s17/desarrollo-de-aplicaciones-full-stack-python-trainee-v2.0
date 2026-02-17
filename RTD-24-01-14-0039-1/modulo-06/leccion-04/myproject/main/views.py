from django.shortcuts import render

# Create your views here.


PRODUCTOS = {
    1:{
        'nombre':'manzana',
        'precio':1500,
        'descripcion':'manzana roja'
    },
    2:{
        'nombre':'Platano',
        'precio':100,
        'descripcion':'platano amarillo'
    },
    3:{
        'nombre':'Naranja',
        'precio':1200,       
        'descripcion':'naranja naranja'
    }
}

def index(request):
    return render(request, 'index.html',context={
        'productos':PRODUCTOS
    })


def detalle_producto(request):
    id_producto = int(request.GET['id_producto'])
    producto = PRODUCTOS[id_producto]

    return render(request, 'detalle_producto.html',context={'producto':producto})


def detalle_producto(request, id_producto):

    producto = PRODUCTOS[id_producto]

    return render(request, 'detalle_producto.html',context={'producto':producto})


eval('1 + 1')