from funciones import *

def mostrar_estadisticas_completas_un_jugador(jugador:dict) -> int:
    """
        Muestar todas las estadisticas del jugador ingresado por parametros.

        Parametros:
        jugador:dict
            El jugador a mostrar sus estadisticas.
        
        Returns:
        tipo : int
            Retorna un numero entero (-1) si salio algo mal, (0) si el diccionario esta vacio (1) si se pudo realizar la tarea con exito.
    """
    retorno = -1

    print(f"\n ***** Estadisticas completas de {jugador['nombre']} *****")
    print(f"Temporadas jugadas: {jugador['estadisticas']['temporadas']}")
    print(f"Puntos totales: {jugador['estadisticas']['puntos_totales']}")
    print(f"Promedio de puntos por partido: {jugador['estadisticas']['promedio_puntos_por_partido']}")
    print(f"Rebotes totales: {jugador['estadisticas']['rebotes_totales']}")
    print(f"Promedio de rebotes por partido: {jugador['estadisticas']['promedio_rebotes_por_partido']}")
    print(f"Asistencias totales: {jugador['estadisticas']['asistencias_totales']}")
    print(f"Promedio de asistencias por partido: {jugador['estadisticas']['promedio_asistencias_por_partido']}")
    print(f"Robos totales: {jugador['estadisticas']['robos_totales']}")
    print(f"Bloqueos totales: {jugador['estadisticas']['bloqueos_totales']}")
    print(f"Porcentaje de tiros de campo: {jugador['estadisticas']['porcentaje_tiros_de_campo']}")
    print(f"Porcentaje de tiros libres: {jugador['estadisticas']['porcentaje_tiros_libres']}")
    print(f"Porcentaje de tiros triples: {jugador['estadisticas']['porcentaje_tiros_triples']}")
    
    return retorno

def mostrar_logros_un_jugador(jugador:dict) -> int:
    """
        Muestar todos los logros del jugador ingresado por parametros.

        Parametros:
        jugador:dict
            El jugador a mostrar sus logros.
        
        Returns:
        tipo : int
            Retorna un numero entero (-1) si salio algo mal, (0) si el diccionario esta vacio (1) si se pudo realizar la tarea con exito.
    """
    retorno = -1

    if jugador != {}:
        for logro in jugador['logros']:
            print(f"{logro}")
        retorno = 1
    else:
        print("ERROR! No se han encontrado logros del jugador indicado.")
        retorno = 0
    
    return retorno

def listar_nombres_jugadores(lista:list) -> int:
    """
        Lista todos los nombres de una lista. 

        Parametros:
        lista : list
            La lista con los nombres a listar.
        
        Returns:
        tipo : int
            Retorna un numero entero (-1) si algo salio mal, (0) si la lista esta vacia o (1) si se pudo realizar la tarea con exito.
    """
    retorno = -1

    if len(lista) > 0:
        for jugador in lista:
            print(f"{jugador['nombre']}")
    else:
        print("\nERROR! No hay elementos cargados en la lista para mostrar.")
        retorno = 0
    return retorno

def listar_nombres_jugadores_con_posiciones(lista:list) -> int:
    """
        Lista todos los nombres de los jugadores del Dream Team con sus posiciones. 

        Parametros:
        lista : list
            La lista con los nombres a listar con sus posiciones.
        
        Returns:
        tipo : int
            Retorna un numero entero (-1) si algo salio mal, (0) si la lista esta vacia o (1) si se pudo realizar la tarea con exito.
    """
    retorno = -1

    if len(lista) > 0:
        for jugador in lista:
            print(f"{jugador['nombre']} - {jugador['posicion']}")
    else:
        print("\nERROR! No hay elementos cargados en la lista para mostrar.")
        retorno = 0
    return retorno

def listar_nombres_jugadores_con_indice(lista:list) -> int:
    """
        Lista todos los nombres de los jugadores del Dream Team con sus indices correspondientes. 

        Parametros:
        lista : list
            La lista con los nombres a listar con sus indices.
        
        Returns:
        tipo : int
            Retorna un numero entero (-1) si algo salio mal, (0) si la lista esta vacia o (1) si se pudo realizar la tarea con exito.
    """
    retorno = -1
    contador = 0

    if len(lista) > 0:
        for jugador in lista:
            print(f"{contador} - {jugador['nombre']}")
            contador+=1
    else:
        print("\nERROR! No hay elementos cargados en la lista para mostrar.")
        retorno = 0
    return retorno

def listar_jugadores_mas_estadistica(lista:list, clave:str) -> int:
    """
        Lista todos los nombres de los jugadores del Dream Team con una estadistica indicada. 

        Parametros:
        lista : list
            La lista con los nombres a listar con sus posiciones.
        clave:str
            La clave indicando la estadistica a mostrar
        
        Returns:
        tipo : int
            Retorna un numero entero (-1) si algo salio mal, (0) si la lista esta vacia o (1) si se pudo realizar la tarea con exito.
    """
    retorno = -1

    if len(lista) > 0:
        for jugador in lista:
            print(f"{jugador['nombre']} - {jugador['estadisticas'][clave]}")
    else:
        print("\nERROR! No hay elementos cargados en la lista para mostrar.")
        retorno = 0
    return retorno

def listar_jugadores_mas_dos_estadistica(lista:list, clave_uno:str, clave_dos:str) -> int:
    """
        Lista todos los nombres de los jugadores del Dream Team con dos estadisticas indicadas. 

        Parametros:
        lista : list
            La lista con los nombres a listar con sus posiciones.
        clave_uno:str
            La clave indicada
        clave_dos:str
            La clave indicando la estadistica a mostrar
        
        Returns:
        tipo : int
            Retorna un numero entero (-1) si algo salio mal, (0) si la lista esta vacia o (1) si se pudo realizar la tarea con exito.
    """
    retorno = -1

    if len(lista) > 0:
        for jugador in lista:
            print(f"{jugador['nombre']} - {jugador[clave_uno]} - {jugador['estadisticas'][clave_dos]}")
    else:
        print("\nERROR! No hay elementos cargados en la lista para mostrar.")
        retorno = 0
    return retorno

def listar_jugadores_all_star(lista:list) -> int:
    """
        Muestra de forma ordenada los jugadores con mas All-Star.

        Parametros:
        lista : list
            Una lista de variables, en este caso serian jugadores del Dream Team.
        
        Returns:
        Retorna un numero entero (-1) si algo salio mal, (0) si la lista esta vacia o (1) si se pudo realizar la tarea con exito.
    """
    retorno = -1

    if len(lista) > 0:
        lista_ordenada = ordenar_jugadores_all_star(lista)

        print("************** lista de jugadores ordenadas por la cantidad de All-Star ****************")
        for jugador in lista_ordenada:
            print(f"{jugador['nombre']} {jugador['cantidad_all_star']} veces All Star")
        retorno = 1   
    else:
        print("ERROR! N o se puede listar los jugadores con mayores All-Star, sa la lista esta vacia.")
        retorno = 0

    return retorno