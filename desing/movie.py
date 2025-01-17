import json

DATA_FILE = "data/movies.json"

def load_movies():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_movies(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def add_movie():
    movies = load_movies()
    title = input("Título de la película: ")
    director = input("Director: ")
    genre = input("Género: ")
    rating = input("Valoración (opcional): ")
    movies.append({"title": title, "director": director, "genre": genre, "rating": rating})
    save_movies(movies)
    print("Película añadida exitosamente.")


