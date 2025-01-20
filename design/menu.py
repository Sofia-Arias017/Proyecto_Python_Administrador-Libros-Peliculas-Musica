from design.books import tableBooks, formularyAddBook
from logic.books import findAll as findAllBooks
from design.movie import tableMovies, formularyAddMovie
from logic.movie import findAll as findAllMovies
from design.music import tableMusic, formularyAddSong
from logic.music import findAll as findAllMusic

def addCollections():
    while True:
        print("""
===========================================
        Añadir un Nuevo Elemento
===========================================
¿Qué tipo de elemento deseas añadir?
1. Libro
2. Película
3. Música
4. Regresar al Menú Principal
===========================================
""")
        opc = int(input("Selecciona una opción (1-4): "))
        match opc:
            case 1:
                formularyAddBook()
            case 2:
                formularyAddMovie()
            case 3:
                formularyAddSong()
            case 4:
                print("")
            case _:
                print("Opcion invalida")

def tableCollections():
    while True:
        print("""
===========================================
           Ver Todos los Elementos
===========================================
¿Qué categoría deseas ver?
1. Ver Todos los Libros
2. Ver Todas las Películas
3. Ver Toda las canciones
4. Regresar al Menú Principal
===========================================
""")
        opc = int(input("Selecciona una opción (1-4): "))
        match  opc:
            case 1:
                tableBooks()
            case 2:
                tableMovies()
            case 3:
                tableMusic()
            case 4:
                print("")
            case _:
                print("Opcion invalida")


