def extraer_info(path: str) -> list[list]:
    """Extrae la informacion del CSV y crea una matriz con esa informacion

    Args:
        path (str): Ruta de acceso relativo del csv

    Returns:
        list[list]: Matriz con los datos del CSV
    """
    matriz = []
    with open(path, "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            separador = linea.strip().split(";")
            matriz.append([int(valor) for valor in separador])
    return matriz