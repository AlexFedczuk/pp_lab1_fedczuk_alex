import json
import re
import csv

def mostrar_menu_principal():
    """
    """
    print("\n ---------- Menú Principal del 'Dream Team' ----------\n")
    print("1. Mostrar la lista de todos los jugadores del Dream Team.")
    print("2. Mostrar un jugador con sus estadisticas completas.")
    print("3. Guardar las estadisticas del jugador selecionado (en la opcion 2) en un archivo CSV.")
    print("4. Mostrar los logros de un jugador.")
    print("5. Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team.")
    print("6. Mostrar si ese jugador es miembro del Salón de la Fama del Baloncesto.")
    print("7. Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.")
    print("8. Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.")
    print("9. Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.")
    print("10. Mostrar los jugadores que han promediado más puntos por partido que X valor.")
    print("11. Mostrar los jugadores que han promediado más rebotes por partido que X valor.")
    print("12. mostrar los jugadores que han promediado más asistencias por partido que X valor.")
    print("13. Calcular y mostrar el jugador con la mayor cantidad de robos totales.")
    print("14. Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales.")
    print("15. Mostrar los jugadores que hayan tenido un porcentaje de tiros libres superior a X valor.")
    print("16. Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al jugador con la menor cantidad de puntos por partido.")
    print("17. Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos.")
    print("18. Mostrar los jugadores que hayan tenido un porcentaje de tiros triples superior a X valor.")
    print("19. Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas.")
    print("20. Mostrar los jugadores, ordenados por posición en la cancha, que hayan tenido un porcentaje de tiros de campo superior a X valor.")
    print("23. Calcular de cada jugador cuál es su posición en cada uno de los siguientes ranking: ● Puntos ● Rebotes ● Asistencias ● Robos.")
    print("0. Salir del programa")

def cargar_lista_json(nombre_archivo_json:str) -> list:
    """
    """
    with open(nombre_archivo_json) as archivo:
        lista_cargada = json.load(archivo)
    return lista_cargada

def formatear_datos_lista(lista:list) -> list:
    """
    """
    lista_retorno = []

    print("len: ", len(lista))

    for item in lista:
        print(item)
        """item_aux = formatear_datos_item(item)
        lista.append(item_aux)
        contador+=1
        print("contador: ", contador)
        if contador == len(lista): 
            break"""
    return lista_retorno

def formatear_datos_item(item:dict) -> dict:
    """
    """
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
    return diccionario_retorno

def pedir_un_numero_entero(mensaje:str) -> int:
    """
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
    contador_de_signos = 0

    for caracter in cadena:
        if caracter in signos:
            contador_de_signos+=1
    return contador_de_signos

def validar_numero_entero(cadena:str) -> bool:
    """
    El patrón verifica si la cadena comienza opcionalmente con un signo "-",
    seguido de uno o más dígitos, y no contiene ningún otro carácter antes
    o después del número. Si la cadena coincide con este patrón, se
    considera un número entero válido.
    """
    patron = r"^-?\d+$"

    if re.match(patron, cadena):
        retorno = True
    else:
        retorno = False
    return retorno

def validar_numero_flotante(cadena:str) -> bool:
    """
    """
    patron = r"^-?\d+(\.\d+)?$"

    if re.match(patron, cadena):
        retorno = True
    else:
        retorno = False
    return retorno

def listar_nombres_jugadores(lista:list) -> int:
    """
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
    """
    retorno = -1

    if len(lista) > 0:
        print("\n***** Lista de todos los jugadores del Dream Team *****\nNombre Jugador - Posición\n-------------------------")
        for jugador in lista:
            print(f"{jugador['nombre']} - {jugador['posicion']}")
    else:
        print("\nERROR! No hay elementos cargados en la lista para mostrar.")
        retorno = 0
    return retorno

def listar_nombres_jugadores_con_indice(lista:list) -> int:
    """
    """
    retorno = -1
    contador = 0

    if len(lista) > 0:
        print("\n***** Lista de todos los jugadores del Dream Team *****\nIndice - Nombre Jugador\n-----------------------")
        for jugador in lista:
            print(f"{contador} - {jugador['nombre']}")
            contador+=1
    else:
        print("\nERROR! No hay elementos cargados en la lista para mostrar.")
        retorno = 0
    return retorno

def pedir_indice_jugador(lista:list) -> int:
    """
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

def encontrar_jugador_por_indice(lista:list, indice_a_buscar:int) -> dict:
    """
    """
    retorno = {}
    contador = 0

    if len(lista) > 0:
        for jugador in lista:
            if contador == indice_a_buscar:
                retorno = jugador
                break
            contador+=1
    else:
        print("\nERROR! No hay elementos cargados en la lista como para buscar un jugador.")

    print(retorno)

    return retorno
        

def mostrar_estadisticas_completas_un_jugador(jugador:dict) -> int:
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

def generar_archivo_csv(jugador:dict) -> int:
    retorno = -1

    if jugador != {}:
        nombre_del_csv = jugador['nombre'] + ".csv"

        encabezado = ["Nombre",
                      "Posición", 
                      "Temporadas", 
                      "Puntos totales", 
                      "Promedio de puntos por partido", 
                      "Rebotes totales", 
                      "Promedio de rebotes por partido", 
                      "Asistencias totales", 
                      "Promedio de asistencias por partido", 
                      "Robos totales", 
                      "Bloqueos totales", 
                      "Porcentaje de tiros de campo", 
                      "Porcentaje de tiros libres", 
                      "Porcentaje de tiros triples"
                      ]
        estadisticas = [jugador["nombre"],
                        jugador['posicion'],
                        jugador['estadisticas']['temporadas'],
                        jugador['estadisticas']['puntos_totales'],
                        jugador['estadisticas']['promedio_puntos_por_partido'],
                        jugador['estadisticas']['rebotes_totales'],
                        jugador['estadisticas']['promedio_rebotes_por_partido'],
                        jugador['estadisticas']['asistencias_totales'],
                        jugador['estadisticas']['promedio_asistencias_por_partido'],
                        jugador['estadisticas']['robos_totales'],
                        jugador['estadisticas']['bloqueos_totales'],
                        jugador['estadisticas']['porcentaje_tiros_de_campo'],
                        jugador['estadisticas']['porcentaje_tiros_libres'],
                        jugador['estadisticas']['porcentaje_tiros_triples']
                        ]
        with open(nombre_del_csv, 'w', newline='') as archivo_csv:
            writer = csv.writer(archivo_csv)
            writer.writerow(encabezado)
            writer.writerow(estadisticas)
        print("El archivo CSV ya se ha generado con exito.")
        retorno = 1
    else:
        print("\nERROR! No hay elementos cargados como para ejecutar esta opción. Realice una operación en la opción 2 antes de realizar una operación en la opción 3.")
        retorno = 0
    return retorno

def pedir_un_nombre(mensaje:str, mensaje_de_error:str) -> str:
    """
    """
    while True:
        nombre_ingresado = input(mensaje)

        if nombre_ingresado.isalpha() == False:
            print(mensaje_de_error)
        else:
            nombre_ingresado = nombre_ingresado.lower()
            nombre_ingresado = nombre_ingresado.capitalize()
            break
    return nombre_ingresado

def pedir_un_nombre_regex(mensaje:str, mensaje_de_error:str) -> str:
    """
    """
    patron = r"^[A-Za-z\s]+$"
    retorno = ""

    while True:
        nombre_ingresado = input(mensaje)

        if re.match(patron, nombre_ingresado):
            retorno = formalizar_nombre_completo(nombre_ingresado)
            break
        else:
            print(mensaje_de_error)            
    return retorno

def formalizar_nombre_completo(nombre_completo:str) -> str:
    """
    """
    nombre_completo = nombre_completo.lower()

    nombres_aux = nombre_completo.split(" ")

    nombre_completo_aux = []
    # nombre_completo_aux = [nombres_aux.capitalize() for nombres_aux in nombres_aux]
    for nombre_aux in nombres_aux:

        nombre_completo_aux.append(nombre_aux.capitalize())

    nombre_formalizado = " ".join(nombre_completo_aux)

    return nombre_formalizado

def encontrar_jugador_por_nombre(lista:list, nombre_a_buscar:str) -> dict:
    """
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

def mostrar_logros_un_jugador(jugador:dict) -> int:
    retorno = -1

    if jugador != {}:
        print(f"\n ***** Todos los logros de {jugador['nombre']} *****")
        for logro in jugador['logros']:
            print(f"{logro}")
        retorno = 1
    else:
        print("ERROR! No se han encontrado logros del jugador indicado.")
        retorno = 0
    
    return retorno

def calcular_promedio(lista:list) -> float:
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

def comprobar_logro_en_un_jugador(jugador:dict, palabra_clave:str) -> bool:
    palabra_clave = "Salon de la Fama del Baloncesto"

    for logros in jugador["logros"]:
        if palabra_clave.lower() in logros.lower():
            retorno = True
            break
        else:
            retorno = False
    return retorno

def encontrar_jugador_por_mayor_valor(lista:list, clave:str) -> dict:
    retorno = {}

    if len(lista) > 0:
        jugador_maximo = calcular_jugador_con_mayor_valor(lista, clave)
        retorno = jugador_maximo
    else:
        print(f"ERROR! No hay datos en la lista como para encontrar un jugador por {clave}.")

    return retorno

def calcular_jugador_con_mayor_valor(lista:list, clave:str) -> dict:
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

def pedir_un_numero_flotante_regex(mensaje:str, mensaje_error:str) -> float:
    """
    """
    while True:
        valor_ingresado = input(mensaje)
        if validar_numero_flotante(valor_ingresado):
            retorno = float(valor_ingresado)
            break
        else:
            print(mensaje_error)
    return retorno

def validar_numero_flotante(cadena:str) -> bool:
    """
    """
    patron = r"^-?\d+(\.\d+)?$"

    if re.match(patron, cadena):
        retorno = True
    else:
        retorno = False
    return retorno

def encontrar_jugadores_por_mayor_valor(lista:list, clave:str, valor:float or int) -> list:
    """
    """
    retorno = []
    lista_aux = []

    if len(lista) > 0:
        # calcular_jugador_con_mayor_valor(lista:list, clave:str)
        for jugador in lista:
            if comprobar_valor_mayor_a_otro(jugador['estadisticas'][clave], valor):
                lista_aux.append(jugador)
        retorno = lista_aux
    else:
        print(f"ERROR! No hay datos en la lista como para encontrar jugadores con {clave}.")

    return retorno

def comprobar_valor_mayor_a_otro(valor_uno, valor_dos) -> bool:
    """
    """
    retorno = False

    if valor_uno > valor_dos:
        retorno = True
    return retorno