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
        print("\n***** Lista de todos los jugadores del Dream Team *****\nNombre Jugador - Posicion\n--------------")
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
            Retorna un diccionario vacio si algo salio mal, un diccionario con la informacion
            del jugador seleccionado en la opcion 2.
    """
    retorno = {}

    if len(lista) > 0:
        print("\n***** Lista de todos los jugadores del Dream Team *****\nIndice - Nombre Jugador\n-----------------------")
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
        print(f"\n ***** Todos los logros de {jugador_encontrado['nombre']} *****")
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

def controlador_opcion_dieciocho(lista:list) -> int:
    """
        Se encarga de contener todas las funciones necesarias para 
        realizar el algoritmo de la opcion 18 del menu principal.

        Parametros:
        lista : list
            Una lista de variables, en este caso serian jugadores del Dream Team.
        
        Returns:
        Retorna un numero entero (-1) si algo salio mal, (0) si la lista esta vacia o (1) si se pudo realizar la tarea con exito.
    """
    retorno = -1

    if len(lista) > 0:
        valor_ingresado = pedir_un_numero_flotante_regex("\nIngrese un valor: ", "ERROR! Ha ingresado un valor invalido.")
        lista_jugadores_encontrados = encontrar_jugadores_por_mayor_valor(lista, 'porcentaje_tiros_triples', valor_ingresado)
        print(f"\n***** Los jugadores que tienen un porcentaje de tiros triples superior al valo ingresado ({valor_ingresado}) *****")
        listar_nombres_jugadores(lista_jugadores_encontrados)
        retorno = 1
    else:
        print("\nERROR! No hay elementos cargados en la lista para realizar esta operacion.")
        retorno = 0

    return retorno

def controlador_opcion_diecinueve(lista:list) -> int:
    """
        Se encarga de contener todas las funciones necesarias para 
        realizar el algoritmo de la opcion 19 del menu principal.

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

def controlador_opcion_diecinueve(lista:list) -> int:
    """
        Se encarga de contener todas las funciones necesarias para 
        realizar el algoritmo de la opcion 19 del menu principal.

        Parametros:
        lista : list
            Una lista de variables, en este caso serian jugadores del Dream Team.
        
        Returns:
        Retorna un numero entero (-1) si algo salio mal, (0) si la lista esta vacia o (1) si se pudo realizar la tarea con exito.
    """
    retorno = -1

    if len(lista) > 0:
        jugador_encontrado = encontrar_jugador_por_mayor_valor(lista, 'temporadas')
        print(f"\nEl jugador con la mayor cantidad de temporadas jugadas es {jugador_encontrado['nombre']}, con un total de {jugador_encontrado['estadisticas']['temporadas']}.")
        retorno = 1
    else:
        print("\nERROR! No hay elementos cargados en la lista para realizar esta operacion.")
        retorno = 0

    return retorno

def controlador_opcion_veinte(lista:list) -> int:
    """
        Se encarga de contener todas las funciones necesarias para 
        realizar el algoritmo de la opcion 19 del menu principal.

        Parametros:
        lista : list
            Una lista de variables, en este caso serian jugadores del Dream Team.
        
        Returns:
        Retorna un numero entero (-1) si algo salio mal, (0) si la lista esta vacia o (1) si se pudo realizar la tarea con exito.
    """
    retorno = -1

    if len(lista) > 0:
        lista_ordenada = ordenar_lista(lista, 'porcentaje_tiros_de_campo')
        print("\n***** Lista ordenada por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a ese valor *****")
        print("\nNombre Jugador - Posicion - Porcentaje de Tiros de Campo")
        
        listar_jugadores_mas_dos_estadistica(lista_ordenada, 'posicion', 'porcentaje_tiros_de_campo')
        retorno = 1
    else:
        print("\nERROR! No hay elementos cargados en la lista para realizar esta operacion.")
        retorno = 0

    return retorno

def controlador_opcion_veintitres(lista:list) -> int:
    """
        Se encarga de guardar un archivo csv con los puntos totales
        de cada jugador.

        Parametros:
        lista : list
            Una lista de variables, en este caso serian jugadores del Dream Team.
        
        Returns:
        Retorna un numero entero (-1) si algo salio mal, (0) si la lista esta vacia o (1) si se pudo realizar la tarea con exito.
    """
    retorno = -1

    if len(lista) > 0:
        guardar_nueva_lista_en_csv(lista, "jugadores_del_DT_y_sus_puntos.csv")
        retorno = 1
    else:
        print("\nERROR! No hay elementos cargados en la lista para realizar esta operacion.")
        retorno = 0

    return retorno

def controlador_opcion_veinticuatro(lista:list) -> int:
    """
        Calcula y muestra la cantidad de jugadores por posicion

        Parametros:
        lista : list
            Una lista de variables, en este caso serian jugadores del Dream Team.
        
        Returns:
        Retorna un numero entero (-1) si algo salio mal, (0) si la lista esta vacia o (1) si se pudo realizar la tarea con exito.
    """
    retorno = -1
    posiciones = ["Escolta","Base","Ala-Pivot","Alero","Pivot"]

    if len(lista) > 0:
        print(f"Escolat: {contar_jugadores_por_posicion(lista, posiciones[0])}")
        print(f"Base: {contar_jugadores_por_posicion(lista, posiciones[1])}")
        print(f"Ala-Pivot: {contar_jugadores_por_posicion(lista, posiciones[2])}")
        print(f"Alero: {contar_jugadores_por_posicion(lista, posiciones[3])}")
        print(f"Escolat: {contar_jugadores_por_posicion(lista, posiciones[4])}")
        retorno = 1
    else:
        print("\nERROR! No hay elementos cargados en la lista para realizar esta operacion.")
        retorno = 0

    return retorno

def controlador_opcion_veinticinco(lista:list) -> int:
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
        listar_jugadores_all_star(lista)
        retorno = 1
    else:
        print("\nERROR! No hay elementos cargados en la lista para realizar esta operacion.")
        retorno = 0

    return retorno

def controlador_opcion_veintiseis(lista:list) -> int:
    """
        determina en una lista los jugadores con las mejores estadisticas.

        Parametros:
        lista : list
            Una lista de variables, en este caso serian jugadores del Dream Team.
        
        Returns:
        Retorna un numero entero (-1) si algo salio mal, (0) si la lista esta vacia o (1) si se pudo realizar la tarea con exito.
    """
    retorno = -1
    
    jugador_maximo_puntos_totales = calcular_jugador_con_mayor_valor(lista, 'puntos_totales')
    jugador_maximo_promedio_puntos_por_partido = calcular_jugador_con_mayor_valor(lista, 'promedio_puntos_por_partido')
    jugador_maximo_rebotes_totales = calcular_jugador_con_mayor_valor(lista, 'rebotes_totales')
    jugador_maximo_promedio_rebotes_por_partido = calcular_jugador_con_mayor_valor(lista, 'promedio_rebotes_por_partido')
    jugador_maximo_asistencias_totales = calcular_jugador_con_mayor_valor(lista, 'asistencias_totales')
    jugador_maximo_promedio_asistencias_por_partido = calcular_jugador_con_mayor_valor(lista, 'promedio_asistencias_por_partido')
    jugador_maximo_robos_totales = calcular_jugador_con_mayor_valor(lista, 'robos_totales')
    jugador_maximo_bloqueos_totales = calcular_jugador_con_mayor_valor(lista, 'bloqueos_totales')
    jugador_maximo_porcentaje_tiros_de_campo = calcular_jugador_con_mayor_valor(lista, 'porcentaje_tiros_de_campo')
    jugador_maximo_porcentaje_tiros_libres = calcular_jugador_con_mayor_valor(lista, 'porcentaje_tiros_libres')
    jugador_maximo_porcentaje_tiros_triples = calcular_jugador_con_mayor_valor(lista, 'porcentaje_tiros_triples')

    if len(lista) > 0:
        print("\n***** Lista de los jugadores con las mejores estadisticas *****")
        print(f"Puntos totales: {jugador_maximo_puntos_totales['nombre']} ({jugador_maximo_puntos_totales['estadisticas']['puntos_totales']})")
        print(f"promedio puntos por partido: {jugador_maximo_promedio_puntos_por_partido['nombre']} ({jugador_maximo_promedio_puntos_por_partido['estadisticas']['promedio_puntos_por_partido']})")
        print(f"rebotes totales: {jugador_maximo_rebotes_totales['nombre']} ({jugador_maximo_rebotes_totales['estadisticas']['rebotes_totales']})")
        print(f"promedio rebotes por partido: {jugador_maximo_promedio_rebotes_por_partido['nombre']} ({jugador_maximo_promedio_rebotes_por_partido['estadisticas']['promedio_rebotes_por_partido']})")
        print(f"asistencias totales: {jugador_maximo_asistencias_totales['nombre']} ({jugador_maximo_asistencias_totales['estadisticas']['asistencias_totales']})")
        print(f"promedio asistencias por partido: {jugador_maximo_promedio_asistencias_por_partido['nombre']} ({jugador_maximo_promedio_asistencias_por_partido['estadisticas']['promedio_asistencias_por_partido']})")
        print(f"robos totales: {jugador_maximo_robos_totales['nombre']} ({jugador_maximo_robos_totales['estadisticas']['robos_totales']})")
        print(f"bloqueos totales: {jugador_maximo_bloqueos_totales['nombre']} ({jugador_maximo_bloqueos_totales['estadisticas']['bloqueos_totales']})")
        print(f"porcentaje tiros de campo: {jugador_maximo_porcentaje_tiros_de_campo['nombre']} ({jugador_maximo_porcentaje_tiros_de_campo['estadisticas']['porcentaje_tiros_de_campo']})")
        print(f"porcentaje tiros libres: {jugador_maximo_porcentaje_tiros_libres['nombre']} ({jugador_maximo_porcentaje_tiros_libres['estadisticas']['porcentaje_tiros_libres']})")
        print(f"porcentaje tiros triples: {jugador_maximo_porcentaje_tiros_triples['nombre']} ({jugador_maximo_porcentaje_tiros_triples['estadisticas']['porcentaje_tiros_triples']})")

        retorno = 1
    else:
        print("\nERROR! No hay elementos cargados en la lista para realizar esta operacion.")
        retorno = 0

    return retorno

def controlador_opcion_veintisiete(lista:list) -> int:
    """
        Determina cual es el mejor jugador estadisticamente.

        Parametros:
        lista : list
            Una lista de variables, en este caso serian jugadores del Dream Team.
        
        Returns:
        Retorna un numero entero (-1) si algo salio mal, (0) si la lista esta vacia o (1) si se pudo realizar la tarea con exito.
    """
    retorno = -1
    if len(lista) > 0:
        mejor_jugador = determinar_el_mejor_jugador(lista)
        print(f"\nEl mejor jugador es {mejor_jugador['nombre']}.")
        retorno = 1
    else:
        print("\nERROR! No hay elementos cargados en la lista para realizar esta operacion.")
        retorno = 0

    return retorno