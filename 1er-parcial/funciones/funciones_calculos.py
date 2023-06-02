from funciones_validaciones import *

def calcular_promedio(lista:list) -> float:
    """
        Calcula el promedio de un total de una estadistica indicada por una clave por parametros.

        Parametros:
        lista : list
            La lista con los datos necesarios para calcular un promedio.
        clave:str
            La clave que indica de que estadistica hay que calcular el promedio.
        
        Returns:
        tipo : float
            Devuelve el promedio calculado.
    """
    retorno = -1

    if len(lista) > 0:
        acumulador = 0
        for jugador in lista:
            acumulador = acumulador + jugador['estadisticas']['promedio_puntos_por_partido']
        promedio = round(float(acumulador/len(lista)), 2)
        retorno = promedio
    else:
        print("ERROR! No hay datos en la lista como para realizar un promedio.")
        retorno = 0

    return retorno

def calcular_jugador_con_mayor_valor(lista:list, clave:str) -> dict:
    """
        Calcula cual es el jugador con el valor mas alto de la estadistica indicada por una clave.

        Parametros:
        lista:list
            La lista con los jugadores el DT.
        clave:str
            La estadistica indicada a por clave.
        
        Returns:
        tipo : int
            Devuelve el jugador calculado con el valor mas alto, en el caso que no
            se haya podido calcular devuleve un diccionario vacio.
    """
    retorno = {}
    jugador_maximo = {}
    bandera = 0

    if len(lista) > 0:
        for jugador in lista:
            if bandera == 0 or jugador_maximo['estadisticas'][clave] < jugador['estadisticas'][clave]:
                jugador_maximo = jugador
                bandera = 1
    else:
        print(f"ERROR! No hay datos en la lista como para encontrar un jugador por {clave}.")

    retorno = jugador_maximo

    return retorno

def calcular_promedio_excluyendo(lista:list, jugador_excluido:dict) -> float:
    """
        Calcula el promedio de un total de una estadistica indicada por una clave por parametros, excluyendo a un jugador.

        Parametros:
        lista : list
            La lista con los datos necesarios para calcular un promedio.
        clave:float or int
            La clave que indica de que estadistica hay que calcular el promedio.
        jugador_excluido:dict
            El jugador que hay que evitar en el calculo.
        
        Returns:
        tipo : float
            Devuelve el promedio calculado.
    """
    retorno = -1

    if len(lista) > 0:
        acumulador = 0
        for jugador in lista:
            if jugador != jugador_excluido:
                acumulador = acumulador + jugador['estadisticas']['promedio_puntos_por_partido']
        promedio = round(float(acumulador/len(lista) - 1), 2)
        retorno = promedio
    else:
        print("ERROR! No hay datos en la lista como para realizar un promedio.")
        retorno = 0

    return retorno

def calcular_jugador_con_menor_valor(lista:list, clave:str) -> dict:
    """
        Calcula cual es el jugador con el valor mas bajo de la estadistica indicada por una clave.

        Parametros:
        lista:list
            La lista con los jugadores el DT.
        clave:str
            La estadistica indicada a por clave.
        
        Returns:
        tipo : int
            Devuelve el jugador calculado con el valor mas bajo, en el caso que no
            se haya podido calcular devuleve un diccionario vacio.
    """
    retorno = {}
    jugador_menor = {}
    bandera = 0

    if len(lista) > 0:
        for jugador in lista:
            if bandera == 0 or jugador_menor['estadisticas'][clave] > jugador['estadisticas'][clave]:
                jugador_menor = jugador
                bandera = 1
    else:
        print(f"ERROR! No hay datos en la lista como para encontrar un jugador por {clave}.")

    retorno = jugador_menor

    return retorno

def contar_jugadores_por_posicion(lista:list, posicion:str) -> int:
    retorno = -1
    contador = 0

    if len(lista) > 0:
        for jugador in lista:
            if jugador['posicion'] == posicion:
                contador+=1
        retorno = contador
    else:
        print("\nERROR! No hay elementos cargados en la lista para contar por posicion.")

    return retorno

def sumar_enteros_en_lista(lista:list) -> int:
    """
        Suma todos los valores que hay en una lista de numeros enteros.

        Parametros:
        lista:list
            La lista a usar para sumar.
        
        Returns:
        tipo : int
            Devuelve el valor calculado en la suma total de todos los valore de la lista.
    """
    acumulador = 0
    if len(lista) > 0:
        for numero_entero in lista:
            acumulador+=numero_entero
    else:
        print("ERROR! No se puede sumar elementos de una lista vacia.")

    return acumulador

def contar_cantidad_logros_un_jugador(jugador:dict) -> int:
    """
        Cuenta la cantidad de logros que tiene un jugador del DT y cuantas veces lo gano. 

        Parametros:
        jugador:dict
            El jugador del DT a analizar.
        
        Returns:
        tipo : int
            Retorna (-1) si algo salio mal, devuleve la cantidad de logros si se pudo realizar la tarea con exito.
    """
    retorno = -1
    cantidad_logros = []

    if jugador != {}:
        for logro in jugador['logros']:
            cantidad_logros.append(identificar_numero_entero(logro))
        retorno = sumar_enteros_en_lista(cantidad_logros)
    else:
        print("ERROR! No hay datos cargados en el jugador indicado.")
    return retorno

def contar_logros_un_jugador(jugador:dict) -> int:
    """
        Cuenta la cantidad de logros que tiene un jugador del DT. 

        Parametros:
        jugador:dict
            El jugador del DT a analizar.
        
        Returns:
        tipo : int
            Retorna (-1) si algo salio mal, devuleve la cantidad de logros si se pudo realizar la tarea con exito.
    """
    retorno = -1

    if jugador != {}:
        retorno = len(jugador['logros'])
    else:
        print("ERROR! No hay datos cargados en el jugador indicado.")
    return retorno