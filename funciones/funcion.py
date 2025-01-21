from datos.importJSON import *
import random

def getInt(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except Exception:
            print('Opcion Invalida, ingrese un valor valido.')


def IdDefault():
    while True:
        colections = abrirArchivo(RUTA_COLECCION)
        idElement = random.randint(1000, 9999)
        resultado = str(idElement)

        encontrado1 = False
        encontrado2 = False
        encontrado3 = False

        for colection in colections["libros"]:
            if colection["id"] == resultado:
                encontrado1 = True
                break
        for colection in colections["musica"]:
            if colection["id"] == resultado:
                encontrado2 = True
                break
        for colection in colections["peliculas"]:
            if colection["id"] == resultado:
                encontrado3 = True
                break
        if not encontrado1 and not encontrado2 and not encontrado3:
            return resultado
        
def pressEnter ():
    print("Exito")
    input('Presiona Enter para continuar...')