def mostrar_cartelera(peliculas: list) -> None:
    """
    Funcion que muestra la cartelera disponible

    :param peliculas: Description
    :type peliculas: list
    """
    for pelicula in peliculas:
        print(f"\nID: {pelicula['id']}")
        print(f"Titulo: {pelicula['titulo']}")
        print(f"Género: {pelicula['genero']}")
        print(f"Valor entrada: ${pelicula['precio_entrada']}")


def buscar_pelicula(peliculas: list, filtro: str) -> list:
    """
    Funcion que recibe el arreglo peliculas y un filtro, y retorna todas aquellas que contengan el filtro en su titulo o genero

    :param peliculas: Description
    :type peliculas: list
    :param filtro: Description
    :type filtro: str
    :return: Description
    :rtype: list
    """
    filtro = filtro.lower()
    resultado = []

    for pelicula in peliculas:
        if filtro in pelicula["titulo"].lower() or filtro in pelicula["genero"].lower():
            resultado.append(pelicula)

    return resultado


def buscador(peliculas: list) -> None:
    """
    Funcion que muestra el buscador

    :param peliculas: Description
    :type peliculas: list
    """
    filtro = input("Ingrese titulo o genero:\n")
    resultados = buscar_pelicula(peliculas, filtro)

    if not resultados:
        print("No se encontraron coincidencias")
    else:
        mostrar_cartelera(resultados)


def buscar_id(peliculas: list, id_pelicula: int) -> dict | None:
    """
    Funcion que retorna un diccionario de la pelicula que coincida con el ID ingresado

    :param peliculas: Description
    :type peliculas: list
    :param id_pelicula: Description
    :type id_pelicula: int
    :return: Description
    :rtype: dict | None
    """
    for pelicula in peliculas:
        if id_pelicula == pelicula["id"]:
            return {
                "id": pelicula["id"],
                "titulo": pelicula["titulo"],
                "cantidad": 0,
                "valor_unitario": pelicula["precio_entrada"],
                "subtotal": 0,
            }

    return None
