from datos.importJSON import *
def verElementos():
    print("""
    ===============================
          ver todo los elementos
    ===============================
          1. libros
          2. musica
          3. peliculas
          4. salir
    ===============================
    """)
    opc2 = input("")
    match opc2:
        case "1":
            RUTA_BOOK()
        case "2":
            RUTA_MUSIC()
        case "3":
            RUTA_MOVIES()  # Added parentheses to call the function
        case "4":
            print("pon enter para continuar")
        case _:
            print("Esta opción no es válida")