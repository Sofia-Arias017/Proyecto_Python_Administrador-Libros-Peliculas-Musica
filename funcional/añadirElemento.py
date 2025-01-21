from funciones.funcion import * 
from diseño.design import * 
from tabulate import tabulate 




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
                break
            case _:
                print('Opcion Invalida')
def ver_elementos():
    print("""
    ===============================
          ver todo los elementos
    ===============================
          1. libros
          2. musica
          3. peliculas
          4. salir
    ===============================
    """)
    opc2 = input("")
    match opc2:
        case "1":
            RUTA_BOOK()
        case "2":
            RUTA_MUSIC()
        case "3":
            RUTA_MOVIES()  # Added parentheses to call the function
        case "4":
            print("pon enter para continuar")
        case _:
            print("Esta opción no es válida")


def buscar(ruta, campo, valor):
    data = abrirArchivo(ruta)  # Assuming this function exists
    found_items = list(filter(lambda item: campo in item and valor.lower() in item[campo].lower(), data))
    
    if found_items:
        print(f"Se encontraron resultados para '{valor}' en el campo '{campo}':")
        print(tabulate(found_items, headers="keys", tablefmt="grid", numalign="center", showindex="always"))
    else:
        print(f"No se encontraron resultados para '{valor}' en el campo '{campo}'.")

def menu_elemento():
    print("""
    ===============================
          ver todo los elementos
    ===============================
          1. libros
          2. musica
          3. peliculas
          4. salir
    ===============================
 """)
    opc_3 = input("")
    match opc_3:
        case "1":
            titulo = input("INGRESA EL TITULO DLE LIBRO: ")
            buscar(RUTA_BOOK, "titulo", titulo)
            pressEnter()
        case "2":
            titulo = input("INGRESA EL TITULO DE LA CANCION: ")
            buscar(RUTA_MUSIC, "titulo", titulo)
            pressEnter()
        case "3":
            titulo = input("INGRESA EL TITULO DE LA PELICULA: ")
            buscar(RUTA_MOVIES, "titulo", titulo)
            pressEnter()
        case "4":
            return
        case _:
                print('Opcion Invalida')
def eliminar(coleccion, tipoJson, ruta, tipo, texto):
    datos = cargar(ruta)
    nombre = input("Ingrese el nombre " + texto)

#Buscar en el archivo JSON y eliminar
    for A in datos:
        if A[tipoJson] == nombre:  # Se debe usar A para acceder al objeto
            datos.remove(A)  # Eliminar el objeto del JSON
            print("Elemento eliminado con éxito del archivo JSON.")
            # Guardar los cambios en el archivo JSON
            with open(ruta, 'w') as f:
                json.dump(datos, f, indent=4)
            return datos

#Buscar en la colección y eliminar
    for B in coleccion[tipo]:
        if B[tipo] == nombre:  # Se debe usar B para acceder al objeto
            coleccion[tipo].remove(B)  # Eliminar el objeto de la colección
            print("Elemento eliminado con éxito de la colección.")
            return coleccion

#Si no se encuentra el nombre
    print(" incorrecto o no encontrado.")
    return datos

def  eliminarElemento(coleccion):
    print("""
     ===============================
          ver todo los elementos
    ===============================
          1. libros
          2. musica
          3. peliculas
          4. salir
    ===============================
          """)
    opc_2 = input("")
    match opc_2:
        case "1":
             datos = eliminar(coleccion,  "titulo", RUTA_BOOK, "libros", "del titulo")
             guardar = (datos, RUTA_BOOK)
    
        case "2":
             datos = eliminar(coleccion,  "titulo", RUTA_MUSIC, "musica", "del titulo")
             guardar = (datos, RUTA_MUSIC)
        case "3":
             datos = eliminar(coleccion,  "titulo", RUTA_MOVIES, "pelicula", "del titulo")
             guardar = (datos, RUTA_MOVIES)
        case "4":
            return
        case _:
                print('Opcion Invalida')