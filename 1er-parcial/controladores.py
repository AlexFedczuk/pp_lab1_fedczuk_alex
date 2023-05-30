from funciones import *


def controlador_opcion_uno(lista:list) -> int:
    """
        Se encarga de contener todas las funciones necesarias para 
        realizar el algoritmo de la opcion 1 del menu principal.

        Parametros:
        lista : list
            Una lista de variables, en este caso serian jugadores del Dream Team.
        
        Returns:
        Retorna un numero entero (-1) si algo salio mal, (0) si la lista esta vacia o (1) si se pudo realizar la tarea con exito.
    """
    retorno = -1

    if len(lista) > 0:
        print("\n***** Lista de todos los jugadores del Dream Team *****\nNombre Jugador\n--------------")
        listar_nombres_jugadores_con_posiciones(lista)
        retorno = 1
    else:
        print("\nERROR! No hay elementos cargados en la lista para mostrar.")
        retorno = 0

    return retorno

def controlador_opcion_dos(lista:list) -> dict:
    """
        Se encarga de contener todas las funciones necesarias para 
        realizar el algoritmo de la opcion 2 del menu principal.

        Parametros:
        lista : list
            Una lista de variables, en este caso serian jugadores del Dream Team.
        
        Returns:
        Retorna un diccionario vacio ({}) si algo salio mal, un diccionario con la informacion
            del jugador seleccionado en la opcion 2.
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
        Se encarga de contener todas las funciones necesarias para 
        realizar el algoritmo de la opcion 3 del menu principal.

        Parametros:
        jugador : dict
            Un diccionario con la informacion del jugador seleccionado en la opcion 2.
        
        Returns:
        Retorna un numero entero (-1) si algo salio mal, (0) si la lista esta vacia o (1) si se pudo realizar la tarea con exito.
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
        Se encarga de contener todas las funciones necesarias para 
        realizar el algoritmo de la opcion 4 del menu principal.

        Parametros:
        lista : list
            Una lista de variables, en este caso serian jugadores del Dream Team.
        
        Returns:
        Retorna un numero entero (-1) si algo salio mal, (0) si la lista esta vacia o (1) si se pudo realizar la tarea con exito.
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
        Se encarga de contener todas las funciones necesarias para 
        realizar el algoritmo de la opcion 5 del menu principal.

        Parametros:
        lista : list
            Una lista de variables, en este caso serian jugadores del Dream Team.
        
        Returns:
        Retorna un numero entero (-1) si algo salio mal, (0) si la lista esta vacia o (1) si se pudo realizar la tarea con exito.
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
        Se encarga de contener todas las funciones necesarias para 
        realizar el algoritmo de la opcion 6 del menu principal.

        Parametros:
        lista : list
            Una lista de variables, en este caso serian jugadores del Dream Team.
        
        Returns:
        Retorna un numero entero (-1) si algo salio mal, (0) si la lista esta vacia o (1) si se pudo realizar la tarea con exito.
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
        Se encarga de contener todas las funciones necesarias para 
        realizar el algoritmo de la opcion 7 del menu principal.

        Parametros:
        lista : list
            Una lista de variables, en este caso serian jugadores del Dream Team.
        
        Returns:
        Retorna un numero entero (-1) si algo salio mal, (0) si la lista esta vacia o (1) si se pudo realizar la tarea con exito.
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
        Se encarga de contener todas las funciones necesarias para 
        realizar el algoritmo de la opcion 8 del menu principal.

        Parametros:
        lista : list
            Una lista de variables, en este caso serian jugadores del Dream Team.
        
        Returns:
        Retorna un numero entero (-1) si algo salio mal, (0) si la lista esta vacia o (1) si se pudo realizar la tarea con exito.
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
        Se encarga de contener todas las funciones necesarias para 
        realizar el algoritmo de la opcion 9 del menu principal.

        Parametros:
        lista : list
            Una lista de variables, en este caso serian jugadores del Dream Team.
        
        Returns:
        Retorna un numero entero (-1) si algo salio mal, (0) si la lista esta vacia o (1) si se pudo realizar la tarea con exito.
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

def controlador_opcion_diez(lista:list) -> int:
    """
        Se encarga de contener todas las funciones necesarias para 
        realizar el algoritmo de la opcion 10 del menu principal.

        Parametros:
        lista : list
            Una lista de variables, en este caso serian jugadores del Dream Team.
        
        Returns:
        Retorna un numero entero (-1) si algo salio mal, (0) si la lista esta vacia o (1) si se pudo realizar la tarea con exito.
    """
    retorno = -1

    if len(lista) > 0:
        valor_ingresado = pedir_un_numero_flotante_regex("\nIngrese un valor: ", "ERROR! Ha ingresado un valor invalido.")
        lista_jugadores_encontrados = encontrar_jugadores_por_mayor_valor(lista, 'promedio_puntos_por_partido', valor_ingresado)
        print(f"\n***** Los jugadores que han promediado más puntos por partido que el valor ingresado: ({valor_ingresado}) *****")
        listar_nombres_jugadores(lista_jugadores_encontrados)
        retorno = 1
    else:
        print("\nERROR! No hay elementos cargados en la lista para realizar esta operacion.")
        retorno = 0

    return retorno

def controlador_opcion_once(lista:list) -> int:
    """
        Se encarga de contener todas las funciones necesarias para 
        realizar el algoritmo de la opcion 11 del menu principal.

        Parametros:
        lista : list
            Una lista de variables, en este caso serian jugadores del Dream Team.
        
        Returns:
        Retorna un numero entero (-1) si algo salio mal, (0) si la lista esta vacia o (1) si se pudo realizar la tarea con exito.
    """
    retorno = -1

    if len(lista) > 0:
        valor_ingresado = pedir_un_numero_flotante_regex("\nIngrese un valor: ", "ERROR! Ha ingresado un valor invalido.")
        lista_jugadores_encontrados = encontrar_jugadores_por_mayor_valor(lista, 'promedio_rebotes_por_partido', valor_ingresado)
        print(f"\n***** Los jugadores que han promediado más rebotes por partido que el valor ingresado: ({valor_ingresado}) *****")
        listar_nombres_jugadores(lista_jugadores_encontrados)
        retorno = 1
    else:
        print("\nERROR! No hay elementos cargados en la lista para realizar esta operacion.")
        retorno = 0

    return retorno

def controlador_opcion_doce(lista:list) -> int:
    """
        Se encarga de contener todas las funciones necesarias para 
        realizar el algoritmo de la opcion 12 del menu principal.

        Parametros:
        lista : list
            Una lista de variables, en este caso serian jugadores del Dream Team.
        
        Returns:
        Retorna un numero entero (-1) si algo salio mal, (0) si la lista esta vacia o (1) si se pudo realizar la tarea con exito.
    """
    retorno = -1

    if len(lista) > 0:
        valor_ingresado = pedir_un_numero_flotante_regex("\nIngrese un valor: ", "ERROR! Ha ingresado un valor invalido.")
        lista_jugadores_encontrados = encontrar_jugadores_por_mayor_valor(lista, 'promedio_asistencias_por_partido', valor_ingresado)
        print(f"\n***** Los jugadores que han promediado más asistencias por partido que el valo ingresado ({valor_ingresado}) *****")
        listar_nombres_jugadores(lista_jugadores_encontrados)
        retorno = 1
    else:
        print("\nERROR! No hay elementos cargados en la lista para realizar esta operacion.")
        retorno = 0

    return retorno

def controlador_opcion_trece(lista:list) -> int:
   """
        Se encarga de contener todas las funciones necesarias para 
        realizar el algoritmo de la opcion 13 del menu principal.

        Parametros:
        lista : list
            Una lista de variables, en este caso serian jugadores del Dream Team.
        
        Returns:
        Retorna un numero entero (-1) si algo salio mal, (0) si la lista esta vacia o (1) si se pudo realizar la tarea con exito.
    """
    retorno = -1

    if len(lista) > 0:
        jugador_encontrado = encontrar_jugador_por_mayor_valor(lista, 'robos_totales')
        print(f"\nEl jugador con la mayor cantidad de robos totales es {jugador_encontrado['nombre']}, con un total de {jugador_encontrado['estadisticas']['robos_totales']}.")
        retorno = 1
    else:
        print("\nERROR! No hay elementos cargados en la lista para realizar esta operacion.")
        retorno = 0

    return retorno

def controlador_opcion_catorce(lista:list) -> int:
    """
        Se encarga de contener todas las funciones necesarias para 
        realizar el algoritmo de la opcion 14 del menu principal.

        Parametros:
        lista : list
            Una lista de variables, en este caso serian jugadores del Dream Team.
        
        Returns:
        Retorna un numero entero (-1) si algo salio mal, (0) si la lista esta vacia o (1) si se pudo realizar la tarea con exito.
    """
    retorno = -1

    if len(lista) > 0:
        jugador_encontrado = encontrar_jugador_por_mayor_valor(lista, 'bloqueos_totales')
        print(f"\nEl jugador con la mayor cantidad de bloqueos totales es {jugador_encontrado['nombre']}, con un total de {jugador_encontrado['estadisticas']['bloqueos_totales']}.")
        retorno = 1
    else:
        print("\nERROR! No hay elementos cargados en la lista para realizar esta operacion.")
        retorno = 0

    return retorno

def controlador_opcion_quince(lista:list) -> int:
    """
        Se encarga de contener todas las funciones necesarias para 
        realizar el algoritmo de la opcion 15 del menu principal.

        Parametros:
        lista : list
            Una lista de variables, en este caso serian jugadores del Dream Team.
        
        Returns:
        Retorna un numero entero (-1) si algo salio mal, (0) si la lista esta vacia o (1) si se pudo realizar la tarea con exito.
    """
    retorno = -1

    if len(lista) > 0:
        valor_ingresado = pedir_un_numero_flotante_regex("\nIngrese un valor: ", "ERROR! Ha ingresado un valor invalido.")
        lista_jugadores_encontrados = encontrar_jugadores_por_mayor_valor(lista, 'porcentaje_tiros_libres', valor_ingresado)
        print(f"\n***** Los jugadores que tienen un porcentaje de tiros libres superio al valo ingresado ({valor_ingresado}) *****")
        listar_nombres_jugadores(lista_jugadores_encontrados)
        retorno = 1
    else:
        print("\nERROR! No hay elementos cargados en la lista para realizar esta operacion.")
        retorno = 0

    return retorno

def controlador_opcion_dieciseis(lista:list) -> int:
    """
        Se encarga de contener todas las funciones necesarias para 
        realizar el algoritmo de la opcion 16 del menu principal.

        Parametros:
        lista : list
            Una lista de variables, en este caso serian jugadores del Dream Team.
        
        Returns:
        Retorna un numero entero (-1) si algo salio mal, (0) si la lista esta vacia o (1) si se pudo realizar la tarea con exito.
    """
    retorno = -1

    if len(lista) > 0:
        promedio = calcular_promedio_excluyendo(lista, calcular_jugador_con_menor_valor(lista, 'promedio_puntos_por_partido'))
        print(f"\nEl promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido es: {promedio}")
        retorno = 1
    else:
        print("\nERROR! No hay elementos cargados en la lista para realizar esta operacion.")
        retorno = 0

    return retorno

def controlador_opcion_diecisiete(lista:list) -> int:
    """
        Se encarga de contener todas las funciones necesarias para 
        realizar el algoritmo de la opcion 17 del menu principal.

        Parametros:
        lista : list
            Una lista de variables, en este caso serian jugadores del Dream Team.
        
        Returns:
        Retorna un numero entero (-1) si algo salio mal, (0) si la lista esta vacia o (1) si se pudo realizar la tarea con exito.
    """
    retorno = -1

    if len(lista) > 0:
        jugador_mayores_logros = encontrar_jugador_mayores_logros(lista)
        print(f"\nEl jugador con la mayor cantidad de logros obtenidos es {jugador_mayores_logros['nombre']} con un total de {contar_cantidad_logros_un_jugador(jugador_mayores_logros)}")
        retorno = 1
    else:
        print("\nERROR! No hay elementos cargados en la lista para realizar esta operacion.")
        retorno = 0

    return retorno
