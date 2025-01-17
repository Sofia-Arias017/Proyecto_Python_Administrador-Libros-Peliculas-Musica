from design.opciones_menu import *

def mostrar_menu():
    print("=" * 43)
    print("        Administrador de Colección")
    print("=" * 43)
    print("1. Añadir un Nuevo Elemento")
    print("2. Ver Todos los Elementos")
    print("3. Buscar un Elemento")
    print("4. Editar un Elemento")
    print("5. Eliminar un Elemento")
    print("6. Ver Elementos por Categoría")
    print("7. Guardar y Cargar Colección")
    print("8. Salir")
    print("=" * 43)

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
        print("Función no implementada.")
    elif opcion == "7":
        guardar_cargar()
    elif opcion == "8":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Inténtalo de nuevo.")
