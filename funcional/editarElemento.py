from funciones.funcion import *
from diseño.design import *

coleccion = abrirArchivo(RUTA_COLECCION)
booksSave = abrirArchivo(RUTA_BOOK)
musicSave = abrirArchivo(RUTA_MUSIC)
moviesSave = abrirArchivo(RUTA_MOVIES)

def editarTitulo():
    idN = getInt('Escribe el identificador del elemento a editar: ')
    encontrado = False
    for colec in coleccion["libros"]:
        if colec["id"] == str(idN):  
            nuevoTitulo = input('Escribe el nuevo título: ').strip().lower()
            colec["titulo"] = nuevoTitulo
            guardarArchivo(RUTA_COLECCION, coleccion)
            guardarArchivo(RUTA_BOOK, booksSave)
            encontrado = True
            break
    for colec in coleccion["musica"]:
        if colec["id"] == str(idN):
            nuevoTitulo = input('Escribe el nuevo título: ').strip().lower()
            colec["titulo"] = nuevoTitulo
            guardarArchivo(RUTA_COLECCION, coleccion)
            guardarArchivo(RUTA_MUSIC, musicSave)
            encontrado = True
            break
    for colec in coleccion["peliculas"]:
        if colec["id"] == str(idN):
            nuevoTitulo = input('Escribe el nuevo título: ').strip().lower()
            colec["titulo"] = nuevoTitulo
            guardarArchivo(RUTA_COLECCION, coleccion)
            guardarArchivo(RUTA_MOVIES, moviesSave)
            encontrado = True
            break

    if not encontrado:
        print('No se encontró un elemento con ese identificador.')

def editarAutor():
    idN = getInt('Escribe el identificador del elemento a editar: ')
    encontrado = False
    for colec in coleccion["libros"]:
        if colec["id"] == str(idN):
            nuevoAutor = input('Escribe el nuevo autor: ').strip().lower()
            colec["autor"] = nuevoAutor
            guardarArchivo(RUTA_COLECCION, coleccion)
            guardarArchivo(RUTA_BOOK, booksSave)
            encontrado = True
            break
    for colec in coleccion["musica"]:
        if colec["id"] == str(idN):
            nuevoAutor = input('Escribe el nuevo autor: ').strip().lower()
            colec["autor"] = nuevoAutor
            guardarArchivo(RUTA_COLECCION, coleccion)
            guardarArchivo(RUTA_MUSIC, musicSave)
            encontrado = True
            break
    for colec in coleccion["peliculas"]:
        if colec["id"] == str(idN):
            nuevoAutor = input('Escribe el nuevo autor: ').strip().lower()
            colec["autor"] = nuevoAutor
            guardarArchivo(RUTA_COLECCION, coleccion)
            guardarArchivo(RUTA_MOVIES, moviesSave)
            encontrado = True
            break

    if not encontrado:
        print('No se encontró un elemento con ese identificador.')

def editarGenero():
    idN = getInt('Escribe el identificador del elemento a editar: ')
    encontrado = False
    for colec in coleccion["libros"]:
        if colec["id"] == str(idN):
            nuevoGenero = input('Escribe el nuevo género: ').strip().lower()
            colec["genero"] = nuevoGenero  
            guardarArchivo(RUTA_COLECCION, coleccion)
            guardarArchivo(RUTA_BOOK, booksSave)
            encontrado = True
            break
    for colec in coleccion["musica"]:
        if colec["id"] == str(idN):
            nuevoGenero = input('Escribe el nuevo género: ').strip().lower()
            colec["genero"] = nuevoGenero  
            guardarArchivo(RUTA_COLECCION, coleccion)
            guardarArchivo(RUTA_MUSIC, musicSave)
            encontrado = True
            break
    for colec in coleccion["peliculas"]:
        if colec["id"] == str(idN):
            nuevoGenero = input('Escribe el nuevo género: ').strip().lower()
            colec["genero"] = nuevoGenero  
            guardarArchivo(RUTA_COLECCION, coleccion)
            guardarArchivo(RUTA_MOVIES, moviesSave)
            encontrado = True
            break

    if not encontrado:
        print('No se encontró un elemento con ese identificador.')


def editarElemento():
    while True:
        print(editarElementoDiseño)  
        opc = getInt('__:')
        idN = getInt('Escribe el identificador del elemento a editar: ')
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
                print('Opción inválida.')
