import json

class Music:
    def __init__(self, title, artist, genre, rating=None):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.rating = rating

    def to_dict(self):
        return {
            "title": self.title,
            "artist": self.artist,
            "genre": self.genre,
            "rating": self.rating
        }

    @staticmethod
    def from_dict(data):
        return Music(data['title'], data['artist'], data['genre'], data.get('rating'))

def save_music(music, filepath='data/music.json'):
    with open(filepath, 'w') as file:
        json.dump([item.to_dict() for item in music], file, indent=4)

def load_music(filepath='data/music.json'):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return [Music.from_dict(item) for item in data]
    except FileNotFoundError:
        return []
