from funciones.funcion import * 
from diseño.design import * 




def añadirLibros(libros, coleccion):
    titulo = input('Escriba el titulo del libro :').lower()
    autor = input('Escriba el nombre del autor :').lower()
    genero = input('Escriba el genero del libro :').lower()
    valor = getInt('Ingrese la puntuacion del libro del (1-5) :')
    valoracion = str(valor)
    categoria = input('Escriba una categoria para el libro :').lower()
    id = IdDefault()

    g = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "valoracion": valoracion,
        "categoria": categoria,
        "id": id
    }
    pressEnter()
    libros.append(g)
    coleccion["libros"].append(g)

def añadirMusica(musica, coleccion):
    titulo = input('Escriba el titulo de la musica :').lower()
    autor = input('Escriba el nombre del artista :').lower()
    genero = input('Escriba el genero del tema :').lower()
    valor = getInt('Ingrese la puntuacion de la cancion del (1-5) :')
    valoracion = str(valor)
    categoria = input('Escriba una categoria para la cancion :').lower()
    id = IdDefault()

    g = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "valoracion": valoracion,
        "categoria": categoria,
        "id": id
    }
    pressEnter()
    musica.append(g)
    coleccion["musica"].append(g)


def añadirPelicula(peliculas, coleccion):
    titulo = input('Escriba el titulo de la pelicula:').lower()
    autor = input('Escriba el nombre del director :').lower()
    genero = input('Escriba el genero de ñla pelicula :').lower()
    valor = getInt('Ingrese la puntuacion de la pelicula del (1-5) :')
    valoracion = str(valor)
    categoria = input('Escriba una categoria para la pelicula :').lower()
    id = IdDefault()

    g = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "valoracion": valoracion,
        "categoria": categoria,
        "id": id
    }
    pressEnter()
    peliculas.append(g)
    coleccion["peliculas"].append(g)


def añadirElemento(libros, musica, peliculas, coleccion):
    while True:
        print(añadirElementoDiseño)
        opcion = getInt('___: ')
        match opcion:
            case 1:
                añadirLibros(libros, coleccion)
            case 2:
                añadirPelicula(peliculas, coleccion)
            case 3:
                añadirMusica(musica, coleccion)
            case 4:
                pressEnter()
            case _:
                print('Opcion Invalida')
