import json

DATA_FILE = "data/books.json"

def load_books():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_books(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def add_book():
    books = load_books()
    title = input("Título del libro: ")
    author = input("Autor: ")
    genre = input("Género: ")
    rating = input("Valoración (opcional): ")
    books.append({"title": title, "author": author, "genre": genre, "rating": rating})
    save_books(books)
    print("Libro añadido exitosamente.")

def list_books():
    books = load_books()
    if not books:
        print("No hay libros en la colección.")
    else:
        for book in books:
            print(f"- {book['title']} | Autor: {book['author']} | Género: {book['genre']} | Valoración: {book.get('rating', 'N/A')}")

def FindAll_libro():
    return load_books()  # Devuelve todos los libros

# Función 'saveaLL_libro' agregada
def saveaLL_libro(data):
    save_books(data)  # Llama a 'save_books'
