import json

class Book:
    def __init__(self, title, author, genre, rating=None):
        self.title = title
        self.author = author
        self.genre = genre
        self.rating = rating

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "rating": self.rating
        }

    @staticmethod
    def from_dict(data):
        return Book(data['title'], data['author'], data['genre'], data.get('rating'))


def save_books(books, filepath='data/books.json'):
    with open(filepath, 'w') as file:
        json.dump([book.to_dict() for book in books], file, indent=4)


def load_books(filepath='data/books.json'):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return [Book.from_dict(item) for item in data]
    except FileNotFoundError:
        return []


    