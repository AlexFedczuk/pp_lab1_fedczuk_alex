from funciones.funciones_json import *
from funciones.funciones_menus import *
from controladores import *

# Ubicacion del archivo en mi PC: C:/Users/Alex Yago Fedczuk/Desktop/1er-parcial/dt.json
# Ubicacion del archivo JSON en mi notebook: C:/Users/afedczuk/OneDrive - indecok/Escritorio/pp_lab1_fedczuk_alex/1er-parcial/dt.json
ubicacion_archivo_dt_json = "C:/Users/Alex Yago Fedczuk/Desktop/pp_lab1_fedczuk_alex/1er-parcial/dt.json"

mensaje_de_desarollo = "\nEsta opcion esta en desarrollo..."

lista_dt = cargar_lista_json(ubicacion_archivo_dt_json)
lista_jugadores = lista_dt['jugadores']
ultimo_jugador_opcion_dos = {}

while True:
    mostrar_menu_principal()
    opcion_de_menu_ingresada = pedir_un_numero_entero_regex("Ingrese una opcion del menu: ", "ERROR! Ha ingresado un valor invalido.")
    
    if opcion_de_menu_ingresada == 1:
        controlador_opcion_uno(lista_jugadores)
    elif opcion_de_menu_ingresada == 2:
        ultimo_jugador_opcion_dos = controlador_opcion_dos(lista_jugadores)
    elif opcion_de_menu_ingresada == 3:
        controlador_opcion_tres(ultimo_jugador_opcion_dos)
    elif opcion_de_menu_ingresada == 4:
        controlador_opcion_cuatro(lista_jugadores)
    elif opcion_de_menu_ingresada == 5:
        controlador_opcion_cinco(lista_jugadores)
    elif opcion_de_menu_ingresada == 6:
        controlador_opcion_seis(lista_jugadores)
    elif opcion_de_menu_ingresada == 7:
        controlador_opcion_siete(lista_jugadores)
    elif opcion_de_menu_ingresada == 8:
        controlador_opcion_ocho(lista_jugadores)
    elif opcion_de_menu_ingresada == 9:
        controlador_opcion_nueve(lista_jugadores)
    elif opcion_de_menu_ingresada == 10:
        controlador_opcion_diez(lista_jugadores)
    elif opcion_de_menu_ingresada == 11:
        controlador_opcion_once(lista_jugadores)
    elif opcion_de_menu_ingresada == 12:
        controlador_opcion_doce(lista_jugadores)
    elif opcion_de_menu_ingresada == 13:
        controlador_opcion_trece(lista_jugadores)
    elif opcion_de_menu_ingresada == 14:
        controlador_opcion_catorce(lista_jugadores)
    elif opcion_de_menu_ingresada == 15:
        controlador_opcion_quince(lista_jugadores)
    elif opcion_de_menu_ingresada == 16:
        controlador_opcion_dieciseis(lista_jugadores)
    elif opcion_de_menu_ingresada == 17:
        controlador_opcion_diecisiete(lista_jugadores)
    elif opcion_de_menu_ingresada == 18:
        controlador_opcion_dieciocho(lista_jugadores)
    elif opcion_de_menu_ingresada == 19:
        controlador_opcion_diecinueve(lista_jugadores)
    elif opcion_de_menu_ingresada == 20:
        controlador_opcion_veinte(lista_jugadores)
    elif opcion_de_menu_ingresada == 23:
        controlador_opcion_veintitres(lista_jugadores)
    elif opcion_de_menu_ingresada == 24:
        controlador_opcion_veinticuatro(lista_jugadores)
    elif opcion_de_menu_ingresada == 25:
        controlador_opcion_veinticinco(lista_jugadores)
    elif opcion_de_menu_ingresada == 26:
        controlador_opcion_veintiseis(lista_jugadores)
    elif opcion_de_menu_ingresada == 27:
        controlador_opcion_veintisiete(lista_jugadores)
    elif opcion_de_menu_ingresada == 0:
        print("\nSaliendo del programa...")
        break
    else:
        print("\nERROR! Ingreso un valor invalido en el menu principal.")