from funciones.funcion import *
from diseño.design import *
from tabulate import tabulate

peliculas = abrirArchivo(RUTA_MOVIES)
libros = abrirArchivo(RUTA_BOOK)
musica = abrirArchivo(RUTA_MUSIC)

def buscarTitulo():
    titulo = input('Escribe el título a buscar: ').strip().lower()
    print(f"Buscando título: {titulo}")

    coleccion = {
        "libros": libros,
        "musica": musica,
        "peliculas": peliculas
    }

    for categoria in ['libros', 'musica', 'peliculas']:
        for colec in coleccion[categoria]:
            print(f"Comparando con: {colec['titulo'].lower()}")  
            if titulo == colec["titulo"].lower():
                print(f"\nTítulo encontrado en la categoría '{categoria.capitalize()}':")
                print(tabulate([colec], headers="keys", tablefmt="grid"))
                pressEnter()
                return


    print('No se ha encontrado')
    pressEnter()

coleccion = abrirArchivo(RUTA_COLECCION)

def buscarAutor():
    autor = input('Escribe el autor a buscar: ').strip().lower()
    print(f"Buscando autor: {autor}")

    coleccion = {
        "libros": libros,
        "musica": musica,
        "peliculas": peliculas
    }

    for categoria in ['libros', 'musica', 'peliculas']:
        for colec in coleccion[categoria]:
            print(f"Comparando con: {colec['autor'].lower()}")  
            if autor == colec["autor"].lower():
                print(f"\Autor encontrado en la categoria '{categoria.capitalize()}':")
                print(tabulate([colec], headers="keys", tablefmt="grid"))
                pressEnter()
                return

    print('No se ha encontrado')
    pressEnter()

def buscarGenero():
    genero = input('Escribe el genero a buscar: ').strip().lower()
    print(f"Buscando genero: {genero}")

    coleccion = {
        "libros": libros,
        "musica": musica,
        "peliculas": peliculas
    }

    for categoria in ['libros', 'musica', 'peliculas']:
        for colec in coleccion[categoria]:
            print(f"Comparando con: {colec['genero'].lower()}")  
            if genero == colec["genero"].lower():
                print(f"\Genero encontrado en la categoria '{categoria.capitalize()}':")
                print(tabulate([colec], headers="keys", tablefmt="grid"))
                pressEnter()
                return

    print('No se ha encontrado')
    pressEnter()

def buscarElemento():
    while True:
        print(buscarElementoDiseño)
        opc = getInt('___: ')
        match opc:
            case 1:
                 buscarTitulo()
            case 2:
                 buscarAutor()
            case 3:
                 buscarGenero()
            case 4:
                break
            case _:
                print('Opcion Invalida')

