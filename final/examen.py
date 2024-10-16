def validar_numero():
    """Función para validar que el usuario ingrese un número entero válido de 1 a 999"""
    while True:
        try:
            numero = int(input("Ingrese un número entero (de 1 a 999): "))
            if 1 <= numero <= 999:
                return numero
            else:
                print("El número debe estar entre 1 y 999.")
        except ValueError:
            print("Valor no válido. Ingrese un número entero.")

def buscar_secuencias_por_suma(matriz: list[list], numero: int) -> str:
    """Busca secuencias de números consecutivos que sumen el número ingresado tanto en filas como columnas

    Args:
        matriz (list[list]): Matriz que contiene los números
        numero (int): Número a buscar mediante sumas de secuencias

    Returns:
        str: Mensaje con la cantidad de secuencias encontradas que sumen el número ingresado
    """
    secuencias_encontradas = []

    # Buscar en filas
    for fila in matriz:
        for i in range(len(fila)):
            for j in range(i+2, len(fila)+1):  # Consideramos secuencias de al menos 2 números
                secuencia = fila[i:j]
                if sum(secuencia) == numero:
                    secuencias_encontradas.append(secuencia)

    # Buscar en columnas
    for columna in range(len(matriz[0])):
        columna = [fila[columna] for fila in matriz]
        for i in range(len(columna)):
            for j in range(i+2, len(columna)+1):
                secuencia = columna[i:j]
                if sum(secuencia) == numero:
                    secuencias_encontradas.append(secuencia)

    if secuencias_encontradas:
        return f"Se encontraron {len(secuencias_encontradas)} secuencias que suman {numero}: {secuencias_encontradas}"
    else:
        return f"No se encontraron secuencias que sumen {numero}"

def buscar_secuencia_mas_corta_y_larga(matriz: list[list], numero: int) -> tuple:
    """Busca las secuencias de números consecutivos que sumen el número ingresado y determina cuál es la más corta y la más larga

    Args:
        matriz (list[list]): Matriz que contiene los números
        numero (int): Número a buscar mediante sumas de secuencias

    Returns:
        tuple: Mensajes que indican la secuencia más corta y la más larga
    """
    secuencias_encontradas = []

    # Buscar en filas
    for fila in matriz:
        for i in range(len(fila)):
            for j in range(i+2, len(fila)+1):
                secuencia = fila[i:j]
                if sum(secuencia) == numero:
                    secuencias_encontradas.append(secuencia)

    # Buscar en columnas
    for col in range(len(matriz[0])):
        columna = [fila[col] for fila in matriz]
        for i in range(len(columna)):
            for j in range(i+2, len(columna)+1):
                secuencia = columna[i:j]
                if sum(secuencia) == numero:
                    secuencias_encontradas.append(secuencia)

    if secuencias_encontradas:
        secuencia_mas_corta = min(secuencias_encontradas, key=len)
        secuencia_mas_larga = max(secuencias_encontradas, key=len)
        mensaje_corta = f"La secuencia más corta que suma {numero} tiene {len(secuencia_mas_corta)} elementos: {secuencia_mas_corta}"
        mensaje_larga = f"La secuencia más larga que suma {numero} tiene {len(secuencia_mas_larga)} elementos: {secuencia_mas_larga}"
        return mensaje_corta, mensaje_larga
    else:
        return f"No se encontraron secuencias que sumen {numero}", f"No se encontraron secuencias que sumen {numero}"
