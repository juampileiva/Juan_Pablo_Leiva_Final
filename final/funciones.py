

from archivo import *

def menu_opciones():
    opcion = input("1.Cargar datos del CSV\n2.ingresar numero de maximo 3 digitos\n3.secuencias de numeros sumados conforman su numero\n4.Mostrar la secuencia mas corta y mostrar los numeros\n5.Mostrar la secuencia mas larga y mostrar los numeros\n6.Salir\nElija una opcion: ")
    return opcion


#def lineas_horizontales(matriz: list[list]) -> list:
#    """Analiza todas las filas y devuelve una lista con las secuencias de numeros consecutivos
#
#    Args:
#        matriz (list[list]): Matriz que contiene los numeros
#
#    Returns:
#        list: Lista con las secuencias de numeros consecutivos que se encuentran en las filas (horizontal)
#    """
#    secuencias = []
#    for i in range(len(matriz)):
#        fila = matriz[i]
#        secuencia_actual = [fila[*0]]
#        for j in range(1, len(fila)):
#            if fila[j] == secuencia_actual[-1] + 1:   #No puede haber indice -1, por ende se refiere al ultimo numero de la lista
#                secuencia_actual.append(fila[j])
#            else:
#                if len(secuencia_actual) > 1:
#                    secuencias.append(secuencia_actual)
#                secuencia_actual = [fila[j]]
#        if len(secuencia_actual) > 1:
#            secuencias.append(secuencia_actual)
#    return secuencias
#
#
#
#def lineas_verticales(matriz: list[list]) -> list:
#    """Analiza todas las columnas y devuelve una lista con las secuencias de numeros consecutivos
#
#    Args:
#        matriz (list[list]): Matriz que contiene los numeros
#
#    Returns:
#        list: Lista con las secuencias de numeros consecutivos que se encuentran en las columnas (vertical)
#    """
#    secuencias = []
#    for i in range(len(matriz[0])):
#        columna = []
#        for j in range(len(matriz)):
#            columna.append(matriz[j][i])
#        secuencia_actual = [columna[0]]
#        for j in range(1, len(columna)):
#            if columna[j] == secuencia_actual[-1] + 1:
#                secuencia_actual.append(columna[j])
#            else:
#                if len(secuencia_actual) > 1:
#                    secuencias.append(secuencia_actual)
#                secuencia_actual = [columna[j]]
#        if len(secuencia_actual) > 1:
#            secuencias.append(secuencia_actual)
#    return secuencias
#
###############################################################3
def validar_numero():

    numero = int(input("Ingrese un número entero (de 1 a 999): "))
    if 1 <= numero <= 999:
        return numero
    else:
        print("El número debe estar entre 1 y 999.")
        

def buscar_secuencias_por_suma(matriz, numero):
    
    secuencias_encontradas = []

    for fila in matriz:
        for i in range(len(fila)):
            for j in range(i+2, len(fila)+1):  # Consideramos secuencias de al menos 2 números
                secuencia = fila[i:j]
                suma = sum(secuencia)
                if suma == numero:
                    secuencias_encontradas.append(secuencia)

                    
    # Buscar en columnas
    for columna in range(len(matriz[0])):
        columna = [fila[columna] for fila in matriz]
        for i in range(len(columna)):
            for j in range(i+2, len(columna)+1):
                secuencia = columna[i:j]
                suma = sum(secuencia)
                if suma == numero:
                    secuencias_encontradas.append(secuencia)
                
                

    if secuencias_encontradas:
        print( f"Se encontraron {len(secuencias_encontradas)} secuencias que suman {numero}: ellas son: {secuencias_encontradas}")
    else:
        print (f"No se encontraron secuencias que sumen {numero}")
    return secuencias_encontradas

def buscar_secuencia_mas_corta_y_larga(matriz, numero) :
    
# consecutivos_horizontales = lineas_horizontales(matriz)


#    consecutivos_verticales = lineas_verticales(matriz)
#
#    ocurrencias_totales = consecutivos_horizontales + consecutivos_verticales
#
    secuencias_totales = buscar_secuencias_por_suma(matriz,numero)
    ocurrencia_mas_corta = secuencias_totales[0]  # Inicializo ocurrencia mas corta con el primer elemento de la lista, para luego ir comparandolo con el resto de los elemento
#
#    for ocurrencia in ocurrencias_totales:
#        if len(ocurrencia) < len(ocurrencia_mas_corta):
#            ocurrencia_mas_corta = ocurrencia
#
#    mensaje = f"La secuencia mas corta tiene {len(ocurrencia_mas_corta)} numeros consecutivos y es: {ocurrencia_mas_corta}"
#
#    return mensaje



    for ocurrencia in secuencias_totales:
        if len(ocurrencia) < len(ocurrencia_mas_corta):
            ocurrencia_mas_corta = ocurrencia

    print( f"La secuencia mas corta tiene {len(ocurrencia_mas_corta)} numeros consecutivos y es: {ocurrencia_mas_corta}")

#    if secuencias_encontradas:
#        secuencia_mas_corta = min(secuencias_encontradas, key=len)
#        secuencia_mas_larga = max(secuencias_encontradas, key=len)
#        mensaje_corta = f"La secuencia más corta que suma {numero} tiene {len(secuencia_mas_corta)} elementos: {secuencia_mas_corta}"
#        mensaje_larga = f"La secuencia más larga que suma {numero} tiene {len(secuencia_mas_larga)} elementos: {secuencia_mas_larga}"
#        return mensaje_corta, mensaje_larga
#    else:
#        return f"No se encontraron secuencias que sumen {numero}", f"No se encontraron secuencias que sumen {numero}"

    
############################################################3
"""
secuencias_encontradas = []

    # Buscar en filas
    for fila in matriz:
        for i in range(len(fila)):
            for j in range(i+2, len(fila)+1):
                secuencia = fila[i:j]
                suma = 0
                for k in range(len(secuencia)):
                    suma += secuencia[k]
                    if suma == numero:
                        secuencias_encontradas.append(secuencia)

    # Buscar en columnas
    for col in range(len(matriz[0])):
        columna = [fila[col] for fila in matriz]
        for i in range(len(columna)):
            for j in range(i+2, len(columna)+1):
                secuencia = columna[i:j]
                if sum(secuencia) == numero:
                    secuencias_encontradas.append(secuencia) """
#def verificar_consecutivos(matriz: list[list]) -> str:
#    """Informa si existen numeros consecutivos o no tanto de forma vertical como horizontal
#
#    Args:
#        matriz (list[list]): Matriz que contiene los numeros
#
#    Returns:
#        str: Mensaje que indica que si existe o no numeros consecutivos
#    """
#    consecutivos_horizontales = lineas_horizontales(matriz)
#    consecutivos_verticales = lineas_verticales(matriz)
#    if consecutivos_horizontales or consecutivos_verticales:
#        mensaje = "Existen numeros consecutivos"
#    else:
#        mensaje = "No existen numeros consecutivos"
#
#    return mensaje
#
#def contar_ocurrencias(matriz: list[list]) -> str:
#    """Suma la cantidad de ocurrencias tanto horizontales como verticales e informa el total
#
#    Args:
#        matriz (list[list]): Matriz que contiene los numeros
#
#    Returns:
#        str: Mnesaje que informa el total de ocurrencias
#    """
#    consecutivos_horizontales = lineas_horizontales(matriz)
#    consecutivos_verticales = lineas_verticales(matriz)
#
#    ocurrencias_totales = len(consecutivos_horizontales) + len(consecutivos_verticales)
#
#    mensaje = f"La cantidad de ocurrencias es {ocurrencias_totales}"
#
#    return mensaje
#
#def buscar_secuencia_mas_corta(matriz: list[list]) ->  str:
#    """Busca la secuencia mas corta de numeros consecutivos
#
#    Args:
#        matriz (list[list]): Matriz que contiene los numeros
#
#    Returns:
#        str: Mensaje que muestra la cantidad de numeros y cual es la secuencia mas corta
#    """
#    consecutivos_horizontales = lineas_horizontales(matriz)
#    consecutivos_verticales = lineas_verticales(matriz)
#
#    ocurrencias_totales = consecutivos_horizontales + consecutivos_verticales
#
#    ocurrencia_mas_corta = ocurrencias_totales[0]  # Inicializo ocurrencia mas corta con el primer elemento de la lista, para luego ir comparandolo con el resto de los elemento
#
#    for ocurrencia in ocurrencias_totales:
#        if len(ocurrencia) < len(ocurrencia_mas_corta):
#            ocurrencia_mas_corta = ocurrencia
#
#    mensaje = f"La secuencia mas corta tiene {len(ocurrencia_mas_corta)} numeros consecutivos y es: {ocurrencia_mas_corta}"
#
#    return mensaje

#def buscar_secuencia_mas_larga(matriz: list[list]) ->  str:
#    """Busca la secuencia mas larga de numeros consecutivos
#
#    Args:
#        matriz (list[list]): Matriz que contiene los numeros
#
#    Returns:
#        str: Mensaje que muestra la cantidad de numeros y cual es la secuencia mas larga
#    """
#    consecutivos_horizontales = lineas_horizontales(matriz)
#    consecutivos_verticales = lineas_verticales(matriz)
#
#    ocurrencias_totales = consecutivos_horizontales + consecutivos_verticales
#
#    ocurrencia_mas_larga = ocurrencias_totales[0]  # Inicializo ocurrencia mas corta con el primer elemento de la lista, para luego ir comparandolo con el resto de los elemento
#
#    for ocurrencia in ocurrencias_totales:
#        if len(ocurrencia) > len(ocurrencia_mas_larga):
#            ocurrencia_mas_larga = ocurrencia
#
#    mensaje = f"La secuencia mas larga tiene {len(ocurrencia_mas_larga)} numeros consecutivos y es: {ocurrencia_mas_larga}"
#
#    return mensaje
#