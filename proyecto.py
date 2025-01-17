import json
coleccion = []

def entrada_usuario(mensaje):
    try:
        return input(mensaje)
    except OSError:
        print("La entrada no está soportada en este entorno. Por favor, ejecute el código en una consola interactiva.")
        return ""

def mostrar_menu():
    print("-" * 43)
    print("        Administrador de Colección")
    print("-" * 43)
    print("1. Añadir un Nuevo Elemento")
    print("2. Ver Todos los Elementos")
    print("3. Buscar un Elemento")
    print("4. Editar un Elemento")
    print("5. Eliminar un Elemento")
    print("6. Ver Elementos por Categoría")
    print("7. Guardar y Cargar Colección")
    print("8. Salir")
    print("-" * 43)

def mostrar_submenu():
    print("-" * 43)
    print("        Añadir un Nuevo Elemento")
    print("-" * 43)
    print("¿Qué tipo de elemento deseas añadir?")
    print("1. Libro")
    print("2. Película")
    print("3. Música")
    print("4. Regresar al Menú Principal")
    print("-" * 43)
    return entrada_usuario("Selecciona una opción (1-4): ")

def añadir_elemento():
    while True:
        tipo = mostrar_submenu()
        if tipo == "4":
            return

        categorias = {"1": "Libro", "2": "Película", "3": "Música"}
        categoria = categorias.get(tipo)
        if not categoria:
            print("Opción inválida. Inténtalo de nuevo.")
            continue

        titulo = entrada_usuario("Título: ")
        autor_director_artista = entrada_usuario(f"{categoria == 'Libro' and 'Autor' or categoria == 'Película' and 'Director' or 'Artista'}: ")
        genero = entrada_usuario("Género: ")
        valoracion = entrada_usuario("Valoración (1-5): ")

        elemento = {
            "tipo": categoria,
            "titulo": titulo,
            "autor_director_artista": autor_director_artista,
            "genero": genero,
            "valoracion": valoracion
        }

        coleccion.append(elemento)
        print(f"{categoria} añadido con éxito.")

def ver_todos():
    if not coleccion:
        print("La colección está vacía.")
        return

    for idx, elemento in enumerate(coleccion, start=1):
        print(f"{idx}. [{elemento['tipo']}] {elemento['titulo']} - {elemento['autor_director_artista']} ({elemento['genero']}, {elemento['valoracion']}/5)")

def buscar_elemento():
    termino = entrada_usuario("Ingresa el título, autor/director/artista o género a buscar: ").lower()
    resultados = [e for e in coleccion if termino in e['titulo'].lower() or termino in e['autor_director_artista'].lower() or termino in e['genero'].lower()]

    if resultados:
        for elemento in resultados:
            print(f"[{elemento['tipo']}] {elemento['titulo']} - {elemento['autor_director_artista']} ({elemento['genero']}, {elemento['valoracion']}/5)")
    else:
        print("No se encontraron resultados.")

def editar_elemento():
    titulo = entrada_usuario("Ingresa el título del elemento que deseas editar: ").lower()
    for elemento in coleccion:
        if elemento['titulo'].lower() == titulo:
            print("Elemento encontrado. Ingresa los nuevos valores (deja vacío para mantener el valor actual):")
            nuevo_titulo = entrada_usuario(f"Título ({elemento['titulo']}): ") or elemento['titulo']
            nuevo_autor = entrada_usuario(f"Autor/Director/Artista ({elemento['autor_director_artista']}): ") or elemento['autor_director_artista']
            nuevo_genero = entrada_usuario(f"Género ({elemento['genero']}): ") or elemento['genero']
            nueva_valoracion = entrada_usuario(f"Valoración ({elemento['valoracion']}): ") or elemento['valoracion']

            elemento.update({
                "titulo": nuevo_titulo,
                "autor_director_artista": nuevo_autor,
                "genero": nuevo_genero,
                "valoracion": nueva_valoracion
            })
            print("Elemento actualizado con éxito.")
            return
    print("Elemento no encontrado.")

def eliminar_elemento():
    titulo = entrada_usuario("Ingresa el título del elemento que deseas eliminar: ").lower()
    global coleccion
    coleccion = [e for e in coleccion if e['titulo'].lower() != titulo]
    print("Elemento eliminado, si existía.")

def ver_por_categoria():
    categoria = entrada_usuario("¿Qué categoría deseas ver? (Libro, Película, Música): ").capitalize()
    resultados = [e for e in coleccion if e['tipo'] == categoria]

    if resultados:
        for elemento in resultados:
            print(f"[{elemento['tipo']}] {elemento['titulo']} - {elemento['autor_director_artista']} ({elemento['genero']}, {elemento['valoracion']}/5)")
    else:
        print(f"No hay elementos en la categoría {categoria}.")

def guardar_cargar():
    global coleccion
    opcion = entrada_usuario("¿Deseas guardar (1) o cargar (2) la colección? (3 para regresar): ")
    if opcion == "1":
        archivo = entrada_usuario("Nombre del archivo para guardar (ejemplo: coleccion.json): ")
        with open(archivo, "w") as f:
            json.dump(coleccion, f)
        print("Colección guardada con éxito.")
    elif opcion == "2":
        archivo = entrada_usuario("Nombre del archivo para cargar (ejemplo: coleccion.json): ")
        try:
            with open(archivo, "r") as f:
                coleccion = json.load(f)
            print("Colección cargada con éxito.")
        except FileNotFoundError:
            print("Archivo no encontrado.")
    elif opcion == "3":
        return
    else:
        print("Opción inválida.")

while True:
    mostrar_menu()
    opcion = entrada_usuario("Selecciona una opción (1-8): ")

    if opcion == "1":
        añadir_elemento()
    elif opcion == "2":
        ver_todos()
    elif opcion == "3":
        buscar_elemento()
    elif opcion == "4":
        editar_elemento()
    elif opcion == "5":
        eliminar_elemento()
    elif opcion == "6":
        ver_por_categoria()
    elif opcion == "7":
        guardar_cargar()
    elif opcion == "8":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Inténtalo de nuevo.")
