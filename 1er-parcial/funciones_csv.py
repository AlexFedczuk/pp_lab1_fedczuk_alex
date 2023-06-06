import csv

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