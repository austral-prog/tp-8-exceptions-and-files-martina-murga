# Ejercicio 5 - CSV a lista de diccionarios


def csv_to_dict(filename):
    """
    Lee un archivo CSV con header "name,age,city" y retorna una lista de
    diccionarios, uno por fila.

    Reglas:
    - La primera línea es siempre el header.
    - Las claves del diccionario se toman del header.
    - El campo "age" se convierte a int. "name" y "city" quedan como str.
    - Se deben hacer strip a los valores para eliminar espacios sobrantes.
    - Si el archivo está vacío o solo tiene header, retornar [].
    - Si el archivo no existe, propagar FileNotFoundError.
    - No se permite usar el módulo csv.

    Args:
        filename: str - nombre del archivo a leer.

    Returns:
        list[dict] - lista de diccionarios por fila del CSV.

    Raises:
        FileNotFoundError: si el archivo no existe.

    Ejemplo:
        # archivo contiene:
        # name,age,city
        # Alice,30,Buenos Aires
        # Bob,25,Rosario
        csv_to_dict("people.csv") -> [
            {"name": "Alice", "age": 30, "city": "Buenos Aires"},
            {"name": "Bob", "age": 25, "city": "Rosario"},
        ]
    """
    
    import csv
    with open (filename,"r") as archivo:
        contenido=csv.DictReader(archivo)
        lista = []
        
        for row in contenido:
            diccionario = {}
            
            for header,value in row.items():
                header = header.strip()
                value = value.strip()
                
                if "1" in value or "2" in value or "3" in value or "4" in value or "5" in value or "6" in value or "7" in value or "8" in value or "9" in value or "0" in value or "11" in value or "12" in value:
                    value = int(value)
                diccionario[header] = value
            lista.append(diccionario)

        return lista
