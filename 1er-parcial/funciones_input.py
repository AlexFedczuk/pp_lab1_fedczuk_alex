
from funciones import *

def pedir_un_numero_entero(mensaje:str) -> int:
    """
        Pide un numero de tipo int al usuario y lo valida.

        Parametros:
        mensaje:str
            El mensaje para instruir al usuario.
        
        Returns:
        tipo : int
            El valor ingresado por el usuario validado.
    """
    numeros_decimales = ["1","2","3","4","5","6","7","8","9","0"]
    signos = ["+","-"]
    mensaje_de_error = "ERROR! Debe ingresar un número de tipo entero."

    while True:
        valor_ingresado = str(input(mensaje))
        contador_de_signos = contar_signos(valor_ingresado, signos)
        i = 0

        if contador_de_signos == 1 and valor_ingresado[0] in signos:
            for caracter in valor_ingresado:
                if i == 0 or caracter in numeros_decimales:
                    bandera = True
                else:
                    bandera = False
                    break
                i+=1
            if bandera == True:
                valor_ingresado = int(valor_ingresado)
                break
            else:
                print(mensaje_de_error)
        elif contador_de_signos == 0:
            for caracter in valor_ingresado:
                if caracter in numeros_decimales:
                    bandera = True
                else:
                    bandera = False
                    break
            if bandera == True:
                valor_ingresado = int(valor_ingresado)
                break
            else:
                print(mensaje_de_error)
        else:
            print(mensaje_de_error)
    return valor_ingresado

def pedir_un_numero_entero_regex(mensaje:str, mensaje_error:str) -> int:
    """
        Pide un numero de tipo entero usando expresiones regulares.

        Parametros:
        mensaje:str
            El mensaje para instruir al usuario.
        mensaje_error:str
            El mensaje para instruir al usuario en caso de un error.
        
        Returns:
        tipo : int
            El valor ingresado por el usuario validado.
    """
    while True:
        data_ingresada = input(mensaje)
        resultado = validar_numero_entero(data_ingresada)
        if resultado == True:
            retorno = int(data_ingresada)
            break
        else:
            print(mensaje_error)
    return retorno

def contar_signos(cadena, signos):
    """
        Cuanta la cantidad de signos que hay en una cadena.

        Parametros:
        cadena:str
            La cadena a analizar.
        signos:list
            Los 'signos' a contar en la cadena.
        
        Returns:
        tipo : int
            Devuelve la cantidad de signos encontrados en la cadena.
    """
    contador_de_signos = 0

    for caracter in cadena:
        if caracter in signos:
            contador_de_signos+=1
    return contador_de_signos

def pedir_un_numero_flotante_regex(mensaje:str, mensaje_error:str) -> float:
    """
        Pide un numero de tipo flotante usando expresiones regulares.

        Parametros:
        mensaje:str
            El mensaje para instruir al usuario.
        mensaje_error:str
            El mensaje para instruir al usuario en caso de un error.
        
        Returns:
        tipo : int
            El valor ingresado por el usuario validado.
    """
    while True:
        valor_ingresado = input(mensaje)
        if validar_numero_flotante(valor_ingresado):
            retorno = float(valor_ingresado)
            break
        else:
            print(mensaje_error)
    return retorno

def pedir_indice_jugador(lista:list) -> int:
    """
        Pide al usuario que ingrese por la terminal el indice de un jugador del DT. 

        Parametros:
        lista : list
            La lista con los jugadores del DT.
        
        Returns:
        tipo : int
            Retorna un numero entero (-1) si algo salio mal, el indice del jugador si se pudo realizar la tarea con exito.
    """
    retorno = -1

    if len(lista) > 0:
        while True:
            indice_ingresado = pedir_un_numero_entero_regex("Ingrese el indice del jugador que quiere mostrar sus estadisticas: ", "ERROR! Ha ingresado un valor invalido.")

            if indice_ingresado > -1 and indice_ingresado < len(lista):
                retorno = indice_ingresado
                break
            else:
                print("ERROR! Ha ingresado un indice invalido, ingrese un indice que este dentro de la lista.")
    else:
        print("\nERROR! No hay elementos cargados en la lista como para pedir un indice.")
    return retorno

"""def pedir_un_nombre(mensaje:str, mensaje_de_error:str) -> str:
    
    
    while True:
        nombre_ingresado = input(mensaje)

        if nombre_ingresado.isalpha() == False:
            print(mensaje_de_error)
        else:
            nombre_ingresado = nombre_ingresado.lower()
            nombre_ingresado = nombre_ingresado.capitalize()
            break
    return nombre_ingresado"""

def pedir_un_nombre_regex(mensaje:str, mensaje_de_error:str) -> str:
    """
        Pide un numero nombre al usuario por la terminal.

        Parametros:
        mensaje:str
            El mensaje para instruir al usuario.
        mensaje_error:str
            El mensaje para instruir al usuario en caso de un error.
        
        Returns:
        tipo : int
            Retorna una variable tipo string vacia si sale algo mal, retorna una cadena con un nombre en el cas oque este bien validado.
    """
    retorno = ""
    patron = r"^[A-Za-z\s]+$"    

    while True:
        nombre_ingresado = input(mensaje)

        if re.match(patron, nombre_ingresado):
            retorno = formalizar_nombre_completo(nombre_ingresado)
            break
        else:
            print(mensaje_de_error)            
    return retorno