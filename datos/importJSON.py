import json

def abrirArchivo(archivo):
    with open(f"datos/{archivo}.json","r") as archivoAbrir:
        final = json.load(archivoAbrir)
    return final


def guardarArchivo(archivo,diccionario):
    objetoJson= json.dumps(diccionario, indent=4, ensure_ascii=False)
    with open(f'datos/{archivo}.json',"w") as archivoAbrir:
        archivoAbrir.write(objetoJson)



RUTA_COLECCION = 'coleccion' 
RUTA_BOOK = 'libros'
RUTA_MOVIES = 'peliculas'
RUTA_MUSIC = 'musica'