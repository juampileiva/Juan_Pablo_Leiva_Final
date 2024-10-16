'''
1  Crear una función para cargar el archivo data_final_20241015.csv y transformarlo a una matriz de
10 filas por 10 columnas.
Luego de la carga del archivo (ítem 1):
2  Ingresar por consola un número entero de uno, dos o tres dígitos. Validar el ingreso, que el mismo
sea del tipo número entero.
Buscar e informar:
3  Cuántas secuencias de números consecutivos (por ejemplo 0, 1 , 2) suman el número ingresado
previamente por consola. Los cuales pueden estar de manera horizontal o vertical.
Cabe aclarar que cada secuencia de números consecutivos se debe tomar completa, no se divide en
varias secuencias.
Por ejemplo: la secuencia 0, 1, 2 no admite las secuencias 0, 1 o 1, 2.
4  Cuál es la secuencia de números consecutivos que suman el número ingresado por consola que
tiene la cantidad mínima de elementos (números consecutivos).
5  Cuál es la secuencia de números consecutivos que suman el número ingresado por consola que
tiene la cantidad máxima de elementos (números consecutivos).
6  Salir.

'''


from os import system
from archivo import *
from funciones import *

bandera_menu = True
bandera_seguir = False
bandero_numero = False
while bandera_menu:
    opcion = menu_opciones()
    match opcion:
        case "1":
            matriz = extraer_info("final\data_final_20241015.csv")
            print("El archivo CSV ha sido cargado correctamente.")
            bandera_seguir = True
        case "2":
            if bandera_seguir == False:
                print("Primero debe cargar el archivo CSV")
                
            else:
                numero = validar_numero()
                bandero_numero == True
        case "3":
            if bandera_seguir == False: #or bandero_numero == False:
                print("Primero debe cargar el archivo CSV")
            else:
                buscar_secuencias_por_suma(matriz,numero)

        case "4":
            if bandera_seguir == False: # and bandero_numero == False:
                print("Primero debe cargar el archivo CSV")
            else:
                secuencia_mas_corta = buscar_secuencia_mas_corta(matriz,numero)
        case "5":
            if bandera_seguir == False:# and bandero_numero == False:
                print("Primero debe cargar el archivo CSV")
            else:
                secuencia_mas_larga = buscar_secuencia_mas_larga(matriz,numero)
        case "6":
            bandera_menu = False
            print("¡Gracias por utlizar el programa!")
        case _ :
            print("Valor invalido, seleccione una opcion entre 1 y 6")

   
   # system("pause")
    # system("cls")


