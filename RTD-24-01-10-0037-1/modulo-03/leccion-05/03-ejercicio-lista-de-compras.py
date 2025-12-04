# Tupla
productos_base = ("pan", "leche", "huevos")

print("Prosuductos base (tupla):", productos_base)
print("Primer producto:", productos_base[0])
print("Cantidad de 'leche' en la tupla:", productos_base.count("leche"))

# Lista de compras
lista_compras = list(productos_base)
print("\nLista de compras inicial:", lista_compras)

lista_compras.append("arroz")
lista_compras.append("aceite")
print("Después de agregar arroz y aceite:", lista_compras)

lista_compras.insert(1, "cafe")
print("Despues de agregar con insert, cafe:", lista_compras)

lista_compras.remove("huevos")
print("Después de remover huevos:", lista_compras)

ultimo = lista_compras.pop()
print("Elemento eliminado con pop():", ultimo)
print("Lista final de compras", lista_compras)

print("Tamaño de la lista:", len(lista_compras))

# set de productos unicos
productos_unicos = set(lista_compras)
print("\nProductos únicos (set):", productos_unicos)

productos_unicos.add("fideos")
print("Después de add('fideos'):", productos_unicos)

productos_unicos.add("pan")
print("Después de add('pan') duplicado:", productos_unicos)

productos_unicos.discard("leche")
print("Después de discard('leche'):", productos_unicos)

# Diccionario de precio y cálculo de total
precios = {
    "pan": 1200,
    "leche": 1000,
    "cafe": 2500,
    "arroz": 1800,
    "aceite": 3000,
    "fideos": 1500,
}

print("\nDiccionario de precios:", precios)
print("Precio del pan:", precios.get("Pan", "No disponible"))
print("Precio de la leche:", precios.get("leche", "No disponible"))

total = 0
print("\nDetalle de compra")

for producto in lista_compras:
    precio = precios.get(producto, 0)
    print(f" - {producto}: {precio}")
    total += precio

print("Total a pagar aproximado:", total)
