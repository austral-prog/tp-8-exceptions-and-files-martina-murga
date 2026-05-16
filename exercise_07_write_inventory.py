# Ejercicio 7 - Escribir un inventario ordenado


def write_inventory(filename, inventory):
    """
    Escribe el inventario en un archivo, una línea por item, ordenadas
    alfabéticamente por nombre de item, con el formato:

        item:cantidad

    Reglas:
    - Cada línea debe terminar con "\\n".
    - Si el diccionario está vacío, el archivo se crea vacío.
    - Si el archivo ya existía, se sobreescribe.
    - La función no retorna nada (None).

    Args:
        filename: str - nombre del archivo a escribir.
        inventory: dict[str, int] - item -> cantidad.

    Returns:
        None

    Ejemplo:
        write_inventory("stock.txt", {"wood": 10, "coal": 3, "iron": 7})
        # El archivo stock.txt queda con:
        # coal:3
        # iron:7
        # wood:10
    """
    
    with open(filename, "r") as archivo:
        content = archivo.read()
        lista_palabras = content.split()
        longest_word = ""
        cantidad = 0
        
        if lista_palabras == []:
            raise ValueError("file has no words")
        for palabra in lista_palabras:
            if len(palabra) > cantidad:
                longest_word = palabra
                cantidad = len(palabra)
        return longest_word
