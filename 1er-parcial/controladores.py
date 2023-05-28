import csv
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
        print("\nERROR! No hay elementos cargados en la lista para mostrar.")

    return retorno

def controlador_opcion_tres(jugador:dict) -> int:
    """
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
        print("El archivo CSV ya se ha generado con exito.")
        retorno = 1
    else:
        print("\nERROR! No hay elementos cargados como para ejecutar esta opción. Realice una operación en la opción 2 antes de realizar una operación en la opción 3.")
        retorno = 0

    return retorno