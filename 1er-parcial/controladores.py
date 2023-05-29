from funciones import *


def controlador_opcion_uno(lista:list) -> int:
    """
    """
    retorno = -1

    if len(lista) > 0:
        listar_nombres_jugadores_con_posiciones(lista)
        retorno = 1
    else:
        print("\nERROR! No hay elementos cargados en la lista para mostrar.")
        retorno = 0

    return retorno

def controlador_opcion_dos(lista:list) -> dict:
    """
    """
    retorno = {}

    if len(lista) > 0:
        listar_nombres_jugadores_con_indice(lista)
        indice_elegido = pedir_indice_jugador(lista)
        jugador_encontrado = encontrar_jugador_por_indice(lista, indice_elegido)
        mostrar_estadisticas_completas_un_jugador(jugador_encontrado)
        retorno = jugador_encontrado
    else:
        print("\nERROR! No hay elementos cargados en la lista para realizar esta operacion.")

    return retorno

def controlador_opcion_tres(jugador:dict) -> int:
    """
    """
    retorno = -1    

    if jugador != {}:
        generar_archivo_csv(jugador)
        retorno = 1
    else:
        print("\nERROR! No hay elementos cargados como para ejecutar esta opción. Realice una operación en la opción 2 antes de realizar una operación en la opción 3.")
        retorno = 0
    return retorno

def controlador_opcion_cuatro(lista:list) -> int:
    """
    """
    retorno = -1

    if len(lista) > 0:
        nombre_ingresado = pedir_un_nombre_regex("\nIngrese el nombre del jugador que quiere buscar: ",
                                                 "\nERROR! Ha ingresado un valor invalido. Ingrese caracteres alfabeticos.")
        jugador_encontrado = encontrar_jugador_por_nombre(lista, nombre_ingresado)
        mostrar_logros_un_jugador(jugador_encontrado)
        retorno = 1
    else:
        print("\nERROR! No hay elementos cargados en la lista para realizar esta operacion.")
        retorno = 0

    return retorno

def controlador_opcion_cinco(lista:list) -> int:
    """
    """
    retorno = -1

    if len(lista) > 0:
        promedio = calcular_promedio(lista)
        print(f"\nEl promedio de puntos por partido de todo el equipo del Dream Team: {promedio}")
        retorno = 1
    else:
        print("\nERROR! No hay elementos cargados en la lista para realizar esta operacion.")
        retorno = 0

    return retorno

def controlador_opcion_seis(lista:list) -> int:
    """
    """
    retorno = -1

    if len(lista) > 0:
        nombre_ingresado = pedir_un_nombre_regex("\nIngrese el nombre del jugador que quiere buscar: ",
                                                 "\nERROR! Ha ingresado un valor invalido. Ingrese caracteres alfabeticos.")
        palabra_clave = "Salon de la Fama del Baloncesto"
        jugador_encontrado = encontrar_jugador_por_nombre(lista, nombre_ingresado)
        if comprobar_logro_en_un_jugador(jugador_encontrado, palabra_clave):
            print(f"\nEl jugador {jugador_encontrado['nombre']} es perteneciente al {palabra_clave}.")
        else:
            print(f"\nEl jugador {jugador_encontrado['nombre']} no es perteneciente al {palabra_clave}.")
        retorno = 1
    else:
        print("\nERROR! No hay elementos cargados en la lista para realizar esta operacion.")
        retorno = 0

    return retorno

def controlador_opcion_siete(lista:list) -> int:
    """
    """
    retorno = -1

    if len(lista) > 0:
        jugador_encontrado = encontrar_jugador_por_mayor_valor(lista, 'rebotes_totales')
        print(f"\nEl jugador con la mayor cantidad de rebotes totales es {jugador_encontrado['nombre']}, con un total de {jugador_encontrado['estadisticas']['rebotes_totales']}.")
        retorno = 1
    else:
        print("\nERROR! No hay elementos cargados en la lista para realizar esta operacion.")
        retorno = 0

    return retorno

def controlador_opcion_ocho(lista:list) -> int:
    """
    """
    retorno = -1

    if len(lista) > 0:
        jugador_encontrado = encontrar_jugador_por_mayor_valor(lista, 'porcentaje_tiros_de_campo')
        print(f"\nEl jugador con el mayor porcentaje de tiros de campo es {jugador_encontrado['nombre']}, con un total de {jugador_encontrado['estadisticas']['porcentaje_tiros_de_campo']}.")
        retorno = 1
    else:
        print("\nERROR! No hay elementos cargados en la lista para realizar esta operacion.")
        retorno = 0

    return retorno

def controlador_opcion_nueve(lista:list) -> int:
    """
    """
    retorno = -1

    if len(lista) > 0:
        jugador_encontrado = encontrar_jugador_por_mayor_valor(lista, 'asistencias_totales')
        print(f"\nEl jugador con la mayor cantidad de asistencias totales es {jugador_encontrado['nombre']}, con un total de {jugador_encontrado['estadisticas']['asistencias_totales']}.")
        retorno = 1
    else:
        print("\nERROR! No hay elementos cargados en la lista para realizar esta operacion.")
        retorno = 0

    return retorno