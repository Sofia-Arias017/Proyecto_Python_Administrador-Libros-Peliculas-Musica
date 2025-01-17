import json

DATA_FILE = "data/music.json"

def load_music():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_music(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def add_music():
    music = load_music()
    title = input("Título de la canción: ")
    artist = input("Artista: ")
    genre = input("Género: ")
    rating = input("Valoración (opcional): ")
    music.append({"title": title, "artist": artist, "genre": genre, "rating": rating})
    save_music(music)
    print("Música añadida exitosamente.")

# Función para mostrar toda la música
def findAll_pe():
    music = load_music()
    if not music:
        print("No hay música en la colección.")
    else:
        for song in music:
            print(f"- {song['title']} | Artista: {song['artist']} | Género: {song['genre']} | Valoración: {song.get('rating', 'N/A')}")

# Función para buscar por artista
def search_by_artist():
    artist_name = input("Introduce el nombre del artista: ")
    music = load_music()
    found = False
    for song in music:
        if artist_name.lower() in song['artist'].lower():
            print(f"- {song['title']} | Artista: {song['artist']} | Género: {song['genre']} | Valoración: {song.get('rating', 'N/A')}")
            found = True
    if not found:
        print("No se encontraron canciones de ese artista.")

# Función para buscar por género
def search_by_genre():
    genre_name = input("Introduce el nombre del género: ")
    music = load_music()
    found = False
    for song in music:
        if genre_name.lower() in song['genre'].lower():
            print(f"- {song['title']} | Artista: {song['artist']} | Género: {song['genre']} | Valoración: {song.get('rating', 'N/A')}")
            found = True
    if not found:
        print("No se encontraron canciones de ese género.")
