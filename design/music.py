from logic.music import findAll, addSong
from tabulate import tabulate

def tableMusic():
    data = findAll()
    print(tabulate(data, headers= "keys", tablefmt="double_grid", numalign="center"))

def formularyAddSong():
    data = findAll()
    titulo= input("Ingrese el título de la canción: ").capitalize()
    autor = input("Ingrese el artista de la canción: ").capitalize()
    genero = input("Ingrese el género de la canción: ").capitalize()
    categoria = input("Ingrese la categoria de la canción: ").capitalize()
    valoracion = input("Ingrese el número de reproducciones de la cancion, ejemplo (2.4M): ").upper()
    findSong = list(filter(lambda element: element.get("titulo").capitalize() == titulo, data))
    if(not len(findSong)):
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
        response = addSong(formulary)
        print(response)
    else:
        print("La canción ya existe")
