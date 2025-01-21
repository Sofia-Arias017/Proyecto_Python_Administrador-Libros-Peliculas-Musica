from diseño.design import *
from funciones.funcion import *
from importa import *

validacion = True

libros = []
musica = []
peliculas = []


coleccion = {
    "libros": [],
    "musica": [],
    "peliculas": []
}



while validacion:
    print(menu)
    opcion = getInt('__: ')
    match opcion:
        case 1:
            añadirElemento(libros, musica, peliculas, coleccion)
        case 2:
            #verElementos()
            pass
        case 3:
            #buscarELemento()
            pass
        case 4:
            #editarELemento()
            pass
        case 5:
            #eliminarELemento()
            pass
        case 6:
            #verELementoCategoria()
            pass
        case 7:
            #guardarCargar()
            pass
        case 8:
            print('Chaooo')
            validacion = False
        case _:
            print('Opcion Invalida')

