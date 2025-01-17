import json

class Movie:
    def __init__(self, title, director, genre, rating=None):
        self.title = title
        self.director = director
        self.genre = genre
        self.rating = rating

    def to_dict(self):
        return {
            "title": self.title,
            "director": self.director,
            "genre": self.genre,
            "rating": self.rating
        }

    @staticmethod
    def from_dict(data):
        return Movie(data['title'], data['director'], data['genre'], data.get('rating'))

def save_movies(movies, filepath='data/movie.json'):
    with open(filepath, 'w') as file:
        json.dump([movie.to_dict() for movie in movies], file, indent=4)

def load_movies(filepath='data/movie.json'):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return [Movie.from_dict(item) for item in data]
    except FileNotFoundError:
        return []
