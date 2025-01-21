from funciones.funcion import *
from diseño.design import *


def loadColection():
    colectionSave = abrirArchivo(RUTA_COLECCION)
    booksSave = abrirArchivo(RUTA_BOOK)
    musicSave = abrirArchivo(RUTA_MUSIC)
    moviesSave = abrirArchivo(RUTA_MOVIES)
    pressEnter()
    return colectionSave, booksSave, musicSave, moviesSave 


def saveColection(books, movies, music, colection, colectionSave, booksSave, musicSave, moviesSave):
    booksSave.extend(books)
    musicSave.extend(music)
    moviesSave.extend(movies)
    colectionSave["libros"].extend(colection["libros"])
    colectionSave["musica"].extend(colection["musica"])
    colectionSave["peliculas"].extend(colection["peliculas"])
    guardarArchivo(RUTA_BOOK, booksSave)
    guardarArchivo(RUTA_MUSIC, musicSave)
    guardarArchivo(RUTA_MOVIES, moviesSave)
    guardarArchivo(RUTA_COLECCION, colectionSave)
    pressEnter()


def saveLoadElement(books, movies, music, colection):
    colectionSave, booksSave, musicSave, moviesSave = None, None, None, None

    while True:
        print(guardarCargarColeccionDiseño)
        opc = getInt(':) ')
        match opc:
            case 1:
                if colectionSave is None or booksSave is None or musicSave is None or moviesSave is None:
                    print("No has cargado la colección. Primero debes cargarla antes de guardar.")
                    pressEnter()
                else:
                    saveColection(books, movies, music, colection, colectionSave, booksSave, musicSave, moviesSave)
            case 2:
                colectionSave, booksSave, musicSave, moviesSave = loadColection()
            case 3:
                pressEnter()
                break
            case _:
                print('Ingresa una opcion valida!!!')