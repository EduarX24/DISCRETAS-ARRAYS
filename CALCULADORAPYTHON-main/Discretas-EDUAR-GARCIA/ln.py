import math 
from msvcrt import getch as STOP
from os import system as PC


class ElWAWA(): #clase para las operaciones
    def __init__(self):  #constructor 
        pass
    #inician todos los metodos
    def SumaArray(self):
        A = []
        B = []
        opc = ""
        PC("cls")
        while True:
            print("|----------------------------------------|")
            print("| 1. SUMA DE ARRAYS                      |")
            print("|----------------------------------------|")
            print("OPERACIÓN CON SUMA DE ARRAYS")
            valor = int(input("Ingrese valores: "))
            A.append(valor)
            print("Ingrese si para agregar O no para salir")

            while opc.lower() != 'si' and opc.lower() != 'no':
                opc = input("Desea agregar otro valor: ")
            
            if opc == 'no':
                break
            else:
                opc = ""
        PC("cls")
        opc2 = ""
        while True:
            print("Ingrese los valores del arreglo 2")
            valor2 = int(input("Ingrese valores: "))
            B.append(valor2)
            print("Ingrese si para agregar O no para salir")

            while opc2.lower() != 'si' and opc2.lower() != 'no':
                opc2 = input("Desea agregar otro valor: ")
            
            if opc2 == 'no':
                break
            else:
                opc2 = ""
        PC("cls")
        r = A + B
        print("El contenido de los arreglos son: ",r)
        STOP()

    def ContArray(self):
        A = []
        B = []
        Intersecion = []
        opc = ""
        PC("cls")
        while True:
            print("|----------------------------------------|")
            print("| 2. ELEMENTOS REPETIDOS EN ARRAY        |")
            print("|----------------------------------------|")
            valor = int(input("Ingrese valores: "))
            A.append(valor)
            print("Ingrese si para agregar O no para salir")

            while opc.lower() != 'si' and opc.lower() != 'no':
                opc = input("Desea agregar otro valor: ")
            
            if opc == 'no':
                break
            else:
                opc = ""
        
        opc2 = ""
        PC("cls")
        while True:
            print("Ingrese los valores del arreglo 2")
            valor2 = int(input("Ingrese valores: "))
            B.append(valor2)
            print("Ingrese si para agregar O no para salir")

            while opc2.lower() != 'si' and opc2.lower() != 'no':
                opc2 = input("Desea agregar otro valor: ")
            
            if opc2 == 'no':
                break
            else:
                opc2 = ""
        PC("cls")
        for i in A:
            for j in B:
             if i == j and i not in  Intersecion:
                 Intersecion.append(i)
        
        print("los elementos repetidos en los arrays son: ",Intersecion)
        STOP()

    def DifArray(self):
        A = []
        B = []
        Diferencia = []
        opc = ""
        PC("cls")
        while True:
            print("|----------------------------------------|")
            print("| 3. DIFERENCIA ELEMENTOS ARRAYS         |")
            print("|----------------------------------------|")
            valor = int(input("Ingrese valores: "))
            A.append(valor)
            print("Ingrese si para agregar O no para salir")

            while opc.lower() != 'si' and opc.lower() != 'no':
                opc = input("Desea agregar otro valor: ")
            
            if opc == 'no':
                break
            else:
                opc = ""

        opc2 = ""
        PC("cls")
        while True:
            print("|----------------------------------------|")
            print("| 3. DIFERENCIA ELEMENTOS ARRAYS         |")
            print("|----------------------------------------|")
            print("Ingrese los valores del arreglo 2")
            valor2 = int(input("Ingrese valores: "))
            B.append(valor2)
            print("Ingrese si para agregar O no para salir")

            while opc2.lower() != 'si' and opc2.lower() != 'no':
                opc2 = input("Desea agregar otro valor: ")
            
            if opc2 == 'no':
                break
            else:
                opc2 = ""

        Diferencia = set(A) - set(B)
        PC("cls")
        print("La direncia en los arreglos son: ", Diferencia)
        STOP()