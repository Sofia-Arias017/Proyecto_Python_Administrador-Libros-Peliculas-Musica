# Importación de módulos necesarios
from desing.general_menus import main_menu
from desing.books import FindAll_libro, saveaLL_libro

def run_program():
    main_menu()  
    libros = FindAll_libro()  
    saveaLL_libro(libros)  

if __name__ == "__main__":
    run_program()
