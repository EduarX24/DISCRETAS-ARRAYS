#Calculadora final
from functools import cache
from ln import ElWAWA
from os import system as PC
import pyfiglet

txt = pyfiglet.figlet_format("Hasta pronto :D")
ms =  pyfiglet.figlet_format("DISCRETAS")

def menu():
    calcular = ElWAWA()
    menu = "nada"
    
    while menu != "4":
        PC("cls")
        print(ms)
        print("|****************************************|")
        print("|        CALCULADORA 2M1-C0              |")
        print("|----------------------------------------|")
        print("|   **POR FAVOR SELECCIONE UNA OPCIÓN**  |")
        print("|----------------------------------------|")
        print("| 1. SUMA DE ARRAYS                      |")
        print("|----------------------------------------|")
        print("| 2. ELEMENTOS REPETIDOS EN ARRAY        |")
        print("|----------------------------------------|")
        print("| 3. DIFERENCIA ELEMENTOS ARRAYS         |")
        print("|----------------------------------------|")
        print("| 4. SALIR      ===>                EXIT |")
        print("|****************************************|")

        menu = input("INGRESE UNA OPCION: ")

        if menu == "1":
            calcular.SumaArray() 
           
        elif menu == "2":
           calcular.ContArray()

        elif menu == '3':
            calcular.DifArray()

    return menu

                 
# Funcion prnicipal
if __name__ == "__main__": 

    while True:
        try:
            menu()
            PC("cls")
            print(txt)
            break
        except (EOFError, KeyboardInterrupt):
            print("ERRROR")