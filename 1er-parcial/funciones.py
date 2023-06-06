from funciones_calculos import *
from funciones_validaciones import *

"""def formatear_datos_lista(lista:list) -> list:
    lista_retorno = []

    print("len: ", len(lista))

    for item in lista:
        print(item)
        item_aux = formatear_datos_item(item)
        lista.append(item_aux)
        contador+=1
        print("contador: ", contador)
        if contador == len(lista): 
            break
    return lista_retorno"""

"""def formatear_datos_item(item:dict) -> dict:
    
    
    diccionario_retorno = {}
    diccionario_aux = item

    for clave, valor in diccionario_aux.items():
        if type(valor) == str:
            if validar_numero_entero(valor) == True:
                diccionario_aux[clave] = int(valor)
            elif validar_numero_flotante(valor) == True:
                diccionario_aux[clave] = float(valor)
        elif type(valor) == int:
            continue
        elif type(valor) == float:
            continue
        else:
            print("Error!")

    diccionario_retorno = diccionario_aux
    return diccionario_retorno"""

def encontrar_jugador_por_indice(lista:list, indice_a_buscar:int) -> dict:
    """
        Busca en la lista de jugadores del DT por un indice ingresado por parametros. 

        Parametros:
        lista:list
            La lista con los jugadores del DT.
        indice_a_buscar:int
            El indice del jugador a buscar.
        
        Returns:
        tipo : int
            Retorna un diccionario vacio si algo salio mal, devuelve el diccionario del jugador
            en el caso que se haya realizado la tarea con exito.
    """
    retorno = {}
    contador = 0

    if (len(lista)) > 0 and (indice_a_buscar > -1 and indice_a_buscar < len(lista)):
        for jugador in lista:
            if contador == indice_a_buscar:
                retorno = jugador
                break
            contador+=1
    else:
        print("\nERROR! No hay elementos cargados en la lista como para buscar un jugador.")

    return retorno
        



def formalizar_nombre_completo(nombre_completo:str) -> str:
    """
        Formaliza el nombre completo ingresado por parametros.

        Parametros:
        nombre_completo:str
            El nombre a formalizar.
        
        Returns:
        tipo : int
            Retorna el nombre formalizado.
    """
    nombre_completo = nombre_completo.lower()
    nombres = nombre_completo.split(" ")
    nombre_completo_aux = []

    for nombre_aux in nombres:
        nombre_completo_aux.append(nombre_aux.capitalize())
    nombre_formalizado = " ".join(nombre_completo_aux)

    return nombre_formalizado

def encontrar_jugador_por_nombre(lista:list, nombre_a_buscar:str) -> dict:
    """
        Busca en la lista de jugadores del DT por un nombre ingresado por parametros. 

        Parametros:
        lista:list
            La lista con los jugadores del DT.
        nombre_a_buscar:str
            El nombre del jugador a buscar.
        
        Returns:
        tipo : int
            Retorna un diccionario vacio si algo salio mal, devuelve el diccionario del jugador
            encontrado en el caso que se haya realizado la tarea con exito.
    """
    retorno = {}

    if len(lista) > 0:
        for jugador in lista:
            if jugador['nombre'] == nombre_a_buscar:
                retorno = jugador
                break
    else:
        print("\nERROR! No hay elementos cargados en la lista como para buscar un jugador.")

    return retorno

def encontrar_jugador_por_mayor_valor(lista:list, clave:str) -> dict:
    """
        Busca al jugador con el valor mas alto de la estadistica indicada por una clave.

        Parametros:
        lista:list
            La lista con los jugadores el DT.
        clave:str
            La estadistica indicada a por clave.
        
        Returns:
        tipo : int
            Devuelve el jugador encontrado mediante un diccionarion en el caso que no
            se haya podido encontrar devuleve un diccionario vacio.
    """
    retorno = {}

    if len(lista) > 0:
        jugador_maximo = calcular_jugador_con_mayor_valor(lista, clave)
        retorno = jugador_maximo
    else:
        print(f"ERROR! No hay datos en la lista como para encontrar un jugador por {clave}.")

    return retorno


def encontrar_jugadores_por_mayor_valor(lista:list, clave:str, valor:float or int) -> list:
    """
        Busca en la lista de jugadores del DT, por una clave estadistica y valor indicado 
        ingresados por parametros, los jugadores que la superen. 

        Parametros:
        lista:list
            La lista con los jugadores del DT.
        clave:str
            La clave estadistica utilizada para realizar la busqueda.
        valor:float or int
            El valor utilizado para realizar la busqueda.

        Returns:
        tipo : int
            Retorna una lista de lus jugadores que superen ese valor, en el caso que no 
            se haya podido realizar con exito, se devuelve una lista vacia.
    """
    retorno = []
    lista_aux = []

    if len(lista) > 0:
        for jugador in lista:
            if jugador['estadisticas'][clave] > valor:
                lista_aux.append(jugador)
        retorno = lista_aux
    else:
        print(f"ERROR! No hay datos en la lista como para encontrar jugadores con {clave}.")

    return retorno

def comprobar_valor_mayor_a_otro(valor_uno, valor_dos) -> bool:
    """
        Comprueba si el primer valor es mayor al segundo.

        Parametros:
        valor_uno:int or float
            Primer valor.        
        valor_dos:int or float
            Segundo valor.
        
        Returns:
        tipo : bool
            Devuelve True en el caso que el primer valor sea mayor que el segundo, de lo contrario False.
    """
    retorno = False

    if valor_uno > valor_dos:
        retorno = True
    return retorno

def encontrar_jugador_mayores_logros(lista:list) -> dict:
    """
        Busca en la lista con los mayores logros. 

        Parametros:
        lista:list
            La lista con los jugadores del DT.
        
        Returns:
        tipo : int
            Retorna un diccionario vacio si algo salio mal, el diccionario del jugador
            en el caso que se haya realizado la tarea con exito.
    """
    retorno = {}
    bandera = 0

    if len(lista) > 0:
        for jugador in lista:
            if bandera == 0 or contar_cantidad_logros_un_jugador(jugador_mayores_logros) < contar_cantidad_logros_un_jugador(jugador):
                jugador_mayores_logros = jugador
                bandera = 1
        retorno = jugador_mayores_logros
    else:
        print("ERROR! No se puede contar la cantidad de logros de los jugarores con una lista vacia.")

    return retorno

def ordenar_lista(lista:list, clave:str) -> list:
    """
        Ordena la lista de jugadores del DT por posicion y una estadistica indicada por una clave.

        Parametros:
        lista:list
            La lista de los jugadores del DT.
        clave:str
            La clave estadistica indicada.
        
        Returns:
        tipo : list
            Devuelve una lista ordenada o la lista como se paso originalemnte en el caso que haya pasado algo malo.
    """
    lista_aux = lista
    posiciones = ["Escolta","Base","Ala-Pivot","Alero","Pivot"]
    lista_aux_dos = []

    if len(lista_aux) > 0:        
        for i in range(0, len(lista_aux) - 1):
            if (lista_aux[i]['estadisticas'][clave] < lista_aux[i + 1]['estadisticas'][clave]):
                jugador_aux = lista_aux[i]
                lista_aux[i] = lista_aux[i + 1]
                lista_aux[i + 1] = jugador_aux
        for posicion in posiciones:
            for i in range(0, len(lista_aux)):
                if (lista_aux[i]['posicion'] == posicion):
                    lista_aux_dos.append(lista_aux[i])
    else:
        print("ERROR! No se puede ordena una lista vacia.")

    return lista_aux_dos

def determinar_el_mejor_jugador(lista:list) -> dict:
    retorno = {}
    mejor_jugador = {}

    if len(lista) > 0:
        for i in range(0, len(lista)):
            if i == 0 or (mejor_jugador['estadisticas']['temporadas'] < lista[i]['estadisticas']['temporadas'] and 
                          mejor_jugador['estadisticas']['puntos_totales'] < lista[i]['estadisticas']['puntos_totales'] and
                          mejor_jugador['estadisticas']['promedio_puntos_por_partido'] < lista[i]['estadisticas']['promedio_puntos_por_partido'] and
                          mejor_jugador['estadisticas']['rebotes_totales'] < lista[i]['estadisticas']['rebotes_totales'] and
                          mejor_jugador['estadisticas']['promedio_rebotes_por_partido'] < lista[i]['estadisticas']['promedio_rebotes_por_partido'] and
                          mejor_jugador['estadisticas']['asistencias_totales'] < lista[i]['estadisticas']['asistencias_totales'] and
                          mejor_jugador['estadisticas']['promedio_asistencias_por_partido'] < lista[i]['estadisticas']['promedio_asistencias_por_partido'] and
                          mejor_jugador['estadisticas']['robos_totales'] < lista[i]['estadisticas']['robos_totales'] and
                          mejor_jugador['estadisticas']['bloqueos_totales'] < lista[i]['estadisticas']['bloqueos_totales'] and
                          mejor_jugador['estadisticas']['porcentaje_tiros_de_campo'] < lista[i]['estadisticas']['porcentaje_tiros_de_campo'] and
                          mejor_jugador['estadisticas']['porcentaje_tiros_libres'] < lista[i]['estadisticas']['porcentaje_tiros_libres'] and
                          mejor_jugador['estadisticas']['porcentaje_tiros_triples'] < lista[i]['estadisticas']['porcentaje_tiros_triples']):
                mejor_jugador = lista[i]
        retorno = mejor_jugador
    elif len(lista) == 1:
        retorno = lista[0]
    else:
        print("\nERROR! No hay elementos cargados en la lista para contar por posicion.")

    return retorno

def encontrar_indice_un_logro(lista_logros:list) -> int:
    """
        Busca el indice de un logro dentro de la lista de logros

        Parametros:
        lista_logros : list
            lista de logros
        
        Returns:
        Retorna un numero entero (-1) si algo salio mal, el indice del logro si se pudo realizar la tarea con exito.
    """
    retorno = -1
    contador = 0

    for logro in lista_logros:
        if "All-Star" in logro:
            retorno = contador
            break
        contador+=1
    return retorno

def ordenar_jugadores_all_star(lista:list) -> list:
    """
        Ordenada los jugadores con mas All-Star.

        Parametros:
        lista : list
            Una lista de variables, en este caso serian jugadores del Dream Team.
        
        Returns:
        Devuelve la lista ordenada.
    """
    lista_aux = []
    jugador_aux_ord = {}

    for jugador in lista:
            if comprobar_logro_en_un_jugador(jugador, "All-Star"):
                jugador_aux = {"nombre": jugador['nombre'], "cantidad_all_star": identificar_numero_entero(jugador['logros'][encontrar_indice_un_logro(jugador['logros'])])}
                lista_aux.append(jugador_aux)        
    for i in range(0, len(lista_aux)):
        for j in range(0, len(lista_aux)):
                    if lista_aux[i]['cantidad_all_star'] > lista_aux[j]['cantidad_all_star']:
                        jugador_aux_ord = lista_aux[i]
                        lista_aux[i] = lista_aux[j]
                        lista_aux[j] = jugador_aux_ord
    return lista_aux