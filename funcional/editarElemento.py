from funciones.funcion import *
from diseño.design import *



coleccion = abrirArchivo(RUTA_COLECCION)
booksSave = abrirArchivo(RUTA_BOOK)
musicSave = abrirArchivo(RUTA_MUSIC)
moviesSave = abrirArchivo(RUTA_MOVIES)

def editarTitulo():
    idN = getInt('Escribe el identificador del elemento a editar :')
    for colec in coleccion["libros"]:
        if colec["id"] == idN:
            nuevoTitulo = input('Escribe el nuevo titulo :').lower()
            colec["titulo"] = nuevoTitulo
            guardarArchivo(RUTA_COLECCION,coleccion)
            guardarArchivo(RUTA_BOOK, booksSave)
            break
    for colec in coleccion["musica"]:
        if colec["id"] == idN:
            nuevoTitulo = input('Escribe el nuevo titulo :').lower()
            colec["titulo"] = nuevoTitulo
            guardarArchivo(RUTA_COLECCION,coleccion)
            guardarArchivo(RUTA_MUSIC, musicSave)
            break
    for colec in coleccion["peliculas"]:
        if colec["id"] == idN:
            nuevoTitulo = input('Escribe el nuevo titulo :').lower()
            colec["titulo"] = nuevoTitulo
            guardarArchivo(RUTA_COLECCION,coleccion)
            guardarArchivo(RUTA_MOVIES, moviesSave)
            break

    print('No Encontrado')


def editarAutor():
    idN = getInt('Escribe el identificador del elemento a editar :')
    for colec in coleccion["libros"]:
        if colec["id"] == idN:
            nuevoAutor = input('Escribe el nuevo Autor :').lower()
            colec["autor"] = nuevoAutor
            guardarArchivo(RUTA_COLECCION,coleccion)
            guardarArchivo(RUTA_BOOK, booksSave)
            break
    for colec in coleccion["musica"]:
        if colec["id"] == idN:
            nuevoAutor = input('Escribe el nuevo Autor :').lower()
            colec["autor"] = nuevoAutor
            guardarArchivo(RUTA_COLECCION,coleccion)
            guardarArchivo(RUTA_MUSIC, musicSave)
            break
    for colec in coleccion["peliculas"]:
        if colec["id"] == idN:
            nuevoAutor = input('Escribe el nuevo Autor :').lower()
            colec["autor"] = nuevoAutor
            guardarArchivo(RUTA_COLECCION,coleccion)
            guardarArchivo(RUTA_MOVIES, moviesSave)
            break

    print('No Encontrado')


def editarGenero():
    idN = getInt('Escribe el identificador del elemento a editar :')
    for colec in coleccion["libros"]:
        if colec["id"] == idN:
            nuevoGenero = input('Escribe el nuevo Genero :').lower()
            colec["autor"] = nuevoGenero
            guardarArchivo(RUTA_COLECCION,coleccion)
            guardarArchivo(RUTA_BOOK, booksSave)
            break
    for colec in coleccion["musica"]:
        if colec["id"] == idN:
            nuevoGenero = input('Escribe el nuevo Genero :').lower()
            colec["autor"] = nuevoGenero
            guardarArchivo(RUTA_COLECCION,coleccion)
            guardarArchivo(RUTA_MUSIC, musicSave)
            break
    for colec in coleccion["peliculas"]:
        if colec["id"] == idN:
            nuevoGenero = input('Escribe el nuevo Genero :').lower()
            colec["autor"] = nuevoGenero
            guardarArchivo(RUTA_COLECCION,coleccion)
            guardarArchivo(RUTA_MOVIES, moviesSave)
            break

def editarElemento():
    while True:
        print(editarElementoDiseño)
        opc = getInt('__:')
        idN = getInt('Escribe el identificador del elemento a editar :')
        match opc:
            case 1:
                 editarTitulo()
            case 2:
                 editarAutor()
            case 3:
                 editarGenero()
            case 4:
                pressEnter()
                break
            case _:
                print('Opcion Invalida')

