from logic.books import findAll, addBook
from tabulate import tabulate

def tableBooks():
    data = findAll()
    print(tabulate(data, headers= "keys", tablefmt="double_grid", numalign="center"))

def formularyAddBook():
    data = findAll()
    titulo= input("Ingrese el título del libro: ").capitalize()
    autor = input("Ingrese el autor del libro: ").capitalize()
    genero = input("Ingrese el género del libro: ").capitalize()
    categoria = input("Ingrese la categoria de la pelicula: ").capitalize()
    valoracion = float(input("Ingrese la valoración del libro: "))
    findBook = list(filter(lambda element: element.get("titulo").capitalize() == titulo, data))
    if(not len(findBook)):
        for indice, product in enumerate(data):
            data[indice] = product.get("codigo")
        formulary = dict({
            "codigo": data[-1] + 1,
            "titulo": titulo,
            "autor": autor,
            "categoria": categoria,
            "genero": genero,
            "valoracion": valoracion
        })
        respuesta = addBook(formulary)
        print(respuesta)
    else:
        print("El libro ya existe")
