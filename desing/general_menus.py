from desing.books import FindAll_libro, saveaLL_libro
from desing.music import findAll_pe, search_by_artist, search_by_genre  # Asegúrate de que las funciones estén importadas correctamente

def main_menu():  # Definimos la función main_menu
    print("""
===========================================
        Menú Principal
===========================================
1. Añadir un Elemento
2. Ver Todos los Elementos
3. Buscar un Elemento
4. Editar un Elemento
5. Eliminar un Elemento
6. Ver Elementos por Categoría
7. Guardar y Cargar Colección
8. Salir
===========================================
          """)
    opc = input("Selecciona una opción: ")
    return opc

def menu_de_opciones_añadir():  # Menu de añadir elementos
    print("""
===========================================
        Añadir un Nuevo Elemento
===========================================
¿Qué tipo de elemento deseas añadir?
1. Libro
2. Película
3. Música
4. Regresar al Menú Principal
===========================================
          """)
    opcion_1 = input()
    return opcion_1

def menu_opcion_todos_elementos():  # Ver todos los elementos
    print("""
===========================================
        Ver Todos los Elementos
===========================================
¿Qué categoría deseas ver?
1. Ver Todos los Libros
2. Ver Todas las Películas
3. Ver Toda la Música
4. Regresar al Menú Principal
===========================================
          """)
    opc = input()
    if opc == "3":
        findAll_pe()  # Llama a la función para mostrar toda la música
    return opc 

def menu_opcion_buscar_un_elemento():  # Buscar un elemento
    print("""
===========================================
        Buscar un Elemento
===========================================
¿Cómo deseas buscar?
1. Buscar por Título
2. Buscar por Autor/Director/Artista
3. Buscar por Género
4. Regresar al Menú Principal
===========================================
            """)
    opc = input()
    if opc == "2":
        search_by_artist()  # Llama a la búsqueda por artista
    elif opc == "3":
        search_by_genre()  # Llama a la búsqueda por género
    return opc

def menu_opcion_editar_un_elemento():  # Editar un elemento
    print("""
===========================================
        Editar un Elemento
===========================================
¿Qué tipo de cambio deseas realizar?
1. Editar Título
2. Editar Autor/Director/Artista
3. Editar Género
4. Editar Valoración
5. Regresar al Menú Principal
===========================================
          """)
    opc = input()
    return opc

def menu_opcion_eliminar_un_elemento():  # Eliminar un elemento
    print("""
===========================================
        Eliminar un Elemento
===========================================
¿Cómo deseas eliminar?
1. Eliminar por Título
2. Eliminar por Identificador Único
3. Regresar al Menú Principal
===========================================
          """)
    opc = input()
    return opc

def menu_opcion_ver_elemento_por_categoria():  # Ver elementos por categoría
    print("""
===========================================
        Ver Elementos por Categoría
===========================================
¿Qué categoría deseas ver?
1. Ver Libros
2. Ver Películas
3. Ver Música
4. Regresar al Menú Principal
===========================================
          """)
    opc = input()
    if opc == "3":
        findAll_pe()  # Llama a la función para ver todos los elementos de música
    return opc

def menu_opcion_guardar_y_cargar_coleccion():  # Guardar y cargar colección
    print("""
===========================================
        Guardar y Cargar Colección
===========================================
¿Qué deseas hacer?
1. Guardar la Colección Actual
2. Cargar una Colección Guardada
3. Regresar al Menú Principal
===========================================
          """)
    opc = input()
    return opc
