from funciones.funcion import *
from diseño.design import *
from tabulate import tabulate

coleccion = abrirArchivo(RUTA_COLECCION)

def buscarTitulo():
    titulo = input('Escribe el titulo a buscar :').lower()
    for colec in coleccion['libros']:
        if titulo == colec["titulo"]:
            print(tabulate([colec], headers="keys", tablefmt="grid"))
            pressEnter()
            return
    for colec in coleccion['musica']:
        if titulo == colec["titulo"]:
            print(tabulate([colec], headers="keys", tablefmt="grid"))
            pressEnter()
            return
    for colec in coleccion['peliculas']:
        if titulo == colec["titulo"]:
            print(tabulate([colec], headers="keys", tablefmt="grid"))
            pressEnter()
            return
    print('No se ha encontrado.')
    pressEnter()


def buscarAutor():
    titulo = input('Escribe el Autor/Compositor/Director a buscar :').lower()
    for colec in coleccion['libros']:
        if titulo == colec["autor"]:
            print(tabulate([colec], headers="keys", tablefmt="grid"))
            pressEnter()
            return
    for colec in coleccion['musica']:
        if titulo == colec["autor"]:
            print(tabulate([colec], headers="keys", tablefmt="grid"))
            pressEnter()
            return
    for colec in coleccion['peliculas']:
        if titulo == colec["autor"]:
            print(tabulate([colec], headers="keys", tablefmt="grid"))
            pressEnter()
            return
    print('No se ha encontrado.')
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
                 #buscarTitulo()
                pass
            case 4:
                pressEnter()
            case _:
                print('Opcion Invalida')

