import re
import os

def validar_numero_entero(cadena:str) -> bool:
    """
        Valida si la cadena pasada por parametros representa un numero entero.

        Parametros:
        cadena:str
            La cadena a validar.
        
        Returns:
        tipo : bool
            Devuelve True en el caso que la cadena represente un numero entero, False en el caso de que no.
    """
    patron = r"^-?\d+$"

    if re.match(patron, cadena):
        retorno = True
    else:
        retorno = False
    return retorno

def validar_numero_flotante(cadena:str) -> bool:
    """
        Valida si la cadena pasada por parametros representa un numero flotante.

        Parametros:
        cadena:str
            La cadena a validar.
        
        Returns:
        tipo : bool
            Devuelve True en el caso que la cadena represente un numero flotante, False en el caso de que no.
    """
    patron = r"^-?\d+(\.\d+)?$"

    if re.match(patron, cadena):
        retorno = True
    else:
        retorno = False
    return retorno

def comprobar_logro_en_un_jugador(jugador:dict, palabra_clave:str) -> bool:
    """
        Comprueba si el jugador del DT tiene x logro usando una palabra o frase clave.

        Parametros:
        jugador:dict
            El jugador a analizar.
        palabra_clave:str
            Palabra clave para chequear en sus logros.

        Returns:
        tipo : bool
            Deveulve True en el caso que se compruebe que el jugador tiene x logro indicado, False en el caso que no
    """
    for logros in jugador["logros"]:
        if palabra_clave.lower() in logros.lower():
            retorno = True
            break
        else:
            retorno = False
    return retorno

def identificar_numero_entero(cadena:str) -> int:
    """
        Identifica numeros enteros en una cadena de caracteres.

        Parametros:
        cadena:str
            La cadena a analizar.
        
        Returns:
        tipo : int
            Retorna el numero entero que haya encontrado en la cadena o (1) 
            en el caso que ningun numero entero haya sido encontrado.
    """      
    retorno = -1
    patron = r'\d+'
    resultado = re.match(patron, cadena)

    if resultado:
        retorno = int(resultado.group())
    else:
        retorno = 1
    return retorno