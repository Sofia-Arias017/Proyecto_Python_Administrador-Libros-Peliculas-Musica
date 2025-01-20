from logic.movie import findAll, addMovie
from tabulate import tabulate

def tableMovies():
    data = findAll()
    print(tabulate(data, headers= "keys", tablefmt="double_grid", numalign="center"))

def formularyAddMovie():
    data = findAll()
    titulo = input("Ingrese el título de la película: ").capitalize()
    autor = input("Ingrese el director de la película: ").capitalize()
    categoria = input("Ingrese la categoria de la pelicula: ").capitalize()
    genero = input("Ingrese el género de la película: ").capitalize()
    valoracion = float(input("Ingrese la valoración de la pelicula: "))
    findMovie = list(filter(lambda element: element.get("titulo").capitalize() == titulo, data))
    if(not len(findMovie)):
        for indice, product in enumerate(data):
            data[indice] = product.get("codigo")
        formulary = dict({
            "codigo": data[-1] + 1,
            "titulo": titulo,
            "autor": autor,
            "genero": genero,
            "categoria": categoria,
            "valoracion": valoracion
        })
        response = addMovie(formulary)
        print(response)
    else:
        print("La película ya existe")
