from desing.books import Book, save_books, load_books
from desing.movie import save_movies, load_movies
from desing.music import Music, save_music, load_music

def display_menu():
    print("="*40)
    print("        Administrador de Colección")
    print("="*40)
    print("1. Añadir un Nuevo Elemento")
    print("2. Ver Todos los Elementos")
    print("3. Buscar un Elemento")
    print("4. Editar un Elemento")
    print("5. Eliminar un Elemento")
    print("6. Ver Elementos por Categoría")
    print("7. Guardar y Cargar Colección")
    print("8. Salir")
    print("="*40)

def add_new_item():
    print("="*40)
    print("        Añadir un Nuevo Elemento")
    print("="*40)
    print("¿Qué tipo de elemento deseas añadir?")
    print("1. Libro")
    print("2. Película")
    print("3. Música")
    print("4. Regresar al Menú Principal")
    option = input("Selecciona una opción (1-4): ")

    if option == "1":
        title = input("Título: ")
        author = input("Autor: ")
        genre = input("Género: ")
        rating = input("Valoración (opcional): ")
        books = load_books()
        books.append(Book(title, author, genre, rating))
        save_books(books)
    elif option == "2":
        title = input("Título: ")
        director = input("Director: ")
        genre = input("Género: ")
        rating = input("Valoración (opcional): ")
        movies = load_movies()
        movies.append(Movie(title, director, genre, rating))
        save_movies(movies)
    elif option == "3":
        title = input("Título: ")
        artist = input("Artista: ")
        genre = input("Género: ")
        rating = input("Valoración (opcional): ")
        music = load_music()
        music.append(Music(title, artist, genre, rating))
        save_music(music)
    elif option == "4":
        return

def view_all_items():
    print("="*40)
    print("        Ver Todos los Elementos")
    print("="*40)
    books = load_books()
    movies = load_movies()
    music = load_music()
    for book in books:
        print(f"Libro: {book.title} - {book.author} - {book.genre} - {book.rating}")
    for movie in movies:
        print(f"Película: {movie.title} - {movie.director} - {movie.genre} - {movie.rating}")
    for music_item in music:
        print(f"Música: {music_item.title} - {music_item.artist} - {music_item.genre} - {music_item.rating}")

def search_item():
    print("="*40)
    print("        Buscar un Elemento")
    print("="*40)
    print("¿Cómo deseas buscar?")
    print("1. Buscar por Título")
    print("2. Buscar por Autor/Director/Artista")
    print("3. Buscar por Género")
    print("4. Regresar al Menú Principal")
    option = input("Selecciona una opción (1-4): ")
    
    if option == "1":
        title = input("Introduce el título: ")
        
    elif option == "2":
        author_or_director_or_artist = input("Introduce el autor/director/artista: ")
        
    elif option == "3":
        genre = input("Introduce el género: ")
        

def main():
    while True:
        display_menu()
        option = input("Selecciona una opción (1-8): ")
        
        if option == "1":
            add_new_item()
        elif option == "2":
            view_all_items()
        elif option == "3":
            search_item()
        elif option == "4":
            pass  
        elif option == "5":
            pass  
        elif option == "6":
            pass  
        elif option == "7":
            pass  
        elif option == "8":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, por favor intenta nuevamente.")

if __name__ == "__main__":
    main()
