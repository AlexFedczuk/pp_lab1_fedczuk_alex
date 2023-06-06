from funciones import *
import json
import os

def cargar_lista_json(nombre_archivo_json:str) -> list:
    """
        Se encarga de cargar toda la informacion que esta en el archivo json en una lista.

        Parametros
        ----------
        nombre_archivo_json : str
            El nombre del archivo json a cargar.
        
        Returns
        -------
        tipo : list
            Devuelve una lista vacia en caso de que no se haya podido cargar la lista.
            En el caso de que se ya haya realizado con exito la funcion, devuelve una lista caragda.
    """
    lista_cargada = []
    #if verificar_nombre_archivo(nombre_archivo_json): 
    with open(nombre_archivo_json) as archivo:
        lista_cargada = json.load(archivo)
    return lista_cargada

"""def verificar_nombre_archivo(nombre_archivo:str) -> bool:
        ...

        Parametros:
        nombre_archivo:str
            La cadena a validar.
        
        Returns:
        tipo : bool
            ...
    retorno = False

    if nombre_archivo == "":
        print("\nERROR! El nombre del archivo es incorrecto. Esta vacia (el nombre).")
    if os.path.exists(nombre_archivo):
        print("\nEl archivo ha sido encontrado!")
        retorno = True
    else:
        print("\nERROR! El archivo no ha sido encontrado.")

    for caracter in nombre_archivo:
        if caracter in r'\/:*?"<>|':
            print(f"\nERROR! El nombre de archivo contiene un carácter no permitido: {caracter}")

    return retorno"""