from diseño.design import *
from funciones.funcion import *
from importa import *
from datos.importJSON import *
from funcional.añadirElemento import *


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
             menu_elemento()
        case 3:
            buscarElemento()
        case 4:
            editarElemento()
        case 5:
            eliminarElemento(coleccion)
        case 6:
            verElementoCategoria()
        case 7:
            saveLoadElement(libros, peliculas, musica, coleccion)
        case 8:
            print('Chaooo')
            validacion = False
        case _:
            print('Opcion Invalida')

