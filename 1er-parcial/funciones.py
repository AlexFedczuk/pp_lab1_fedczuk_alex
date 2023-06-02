import json
import re
import csv

def mostrar_menu_principal():
    """
        Muestra las opciones del menu principal.

        Parametros
        ----------
        void
        
        Returns
        -------
        void
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
    print(" ------------ CONSIGNAS EXTRA! ------------")
    print("24. Determinar la cantidad de jugadores que hay por cada posición")
    print("25. Mostrar la lista de jugadores ordenadas por la cantidad de All-Star de forma descendente")
    print("26. Determinar qué jugador tiene las mejores estadísticas en cada valor.")
    print("27. Determinar qué jugador tiene las mejores estadísticas de todos.")
    print("0. Salir del programa")

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
    with open(nombre_archivo_json) as archivo:
        lista_cargada = json.load(archivo)
    return lista_cargada

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

def generar_archivo_csv(jugador:dict) -> int:
    """
        Genera un archivo tipo csv con toda las estadisticas de un jugar del DT.

        Parametros:
        jugador:dict
            El jugador a guardar sus estadisticas estadisticas.
        
        Returns:
        tipo : int
            Retorna un numero entero (-1) si salio algo mal, (1) en el caso que se haya podido generar el archivo con exito.
    """
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
        print("\nEl archivo CSV ya se ha generado con exito!")
        retorno = 1
    else:
        print("\nERROR! No hay elementos cargados como para ejecutar esta opción. Realice una operación en la opción 2 antes de realizar una operación en la opción 3.")
        retorno = 0
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

def guardar_nueva_lista_en_csv(lista:list, nombre_del_archivo:str) -> int:
    """
        Genera un archivo de tipo CSV con los puntos totales de cada jugador. 

        Parametros:
        lista : list
            La lista con los nombres a listar con sus posiciones.
        nombre_del_archivo:str
            nombre del archivo
        
        Returns:
        tipo : int
            Retorna un numero entero (-1) si algo salio mal, (0) si la lista esta vacia o (1) si se pudo realizar la tarea con exito.
    """
    retorno = -1

    if len(lista) > 0 and nombre_del_archivo != "":
        titulos = ["Jugador","Puntos","Rebotes","Asistencias","Robos"]

        with open(nombre_del_archivo, 'w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerow(titulos)
            for jugador in lista:
                lista_datos = [jugador['nombre'],
                               jugador['estadisticas']['puntos_totales'],
                               jugador['estadisticas']['rebotes_totales'],
                               jugador['estadisticas']['asistencias_totales'],
                               jugador['estadisticas']['robos_totales']]
                escritor_csv.writerow(lista_datos)
        print("\nEl archivo CSV se pudo generar con exito!")
        retorno = 1
    else:
        print("\nERROR! No hay elementos cargados en la lista para mostrar.")
        retorno = 0
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