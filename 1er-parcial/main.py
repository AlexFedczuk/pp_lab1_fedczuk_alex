from funciones import *
from controladores import *

mensaje_de_desarollo = "Esta opcion esta en desarrollo..."
ubicacion_archivo_dt_json = "C:/Users/Alex Yago Fedczuk/Desktop/1er-parcial/dt.json"

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
        print(mensaje_de_desarollo)
    elif opcion_de_menu_ingresada == 7:
        print(mensaje_de_desarollo)
    elif opcion_de_menu_ingresada == 8:
        print(mensaje_de_desarollo)
    elif opcion_de_menu_ingresada == 9:
        print(mensaje_de_desarollo)
    elif opcion_de_menu_ingresada == 10:
        print(mensaje_de_desarollo)
    elif opcion_de_menu_ingresada == 11:
        print(mensaje_de_desarollo)
    elif opcion_de_menu_ingresada == 12:
        print(mensaje_de_desarollo)
    elif opcion_de_menu_ingresada == 13:
        print(mensaje_de_desarollo)
    elif opcion_de_menu_ingresada == 14:
        print(mensaje_de_desarollo)
    elif opcion_de_menu_ingresada == 15:
        print(mensaje_de_desarollo)
    elif opcion_de_menu_ingresada == 16:
        print(mensaje_de_desarollo)
    elif opcion_de_menu_ingresada == 17:
        print(mensaje_de_desarollo)
    elif opcion_de_menu_ingresada == 18:
        print(mensaje_de_desarollo)
    elif opcion_de_menu_ingresada == 19:
        print(mensaje_de_desarollo)
    elif opcion_de_menu_ingresada == 20:
        print(mensaje_de_desarollo)
    elif opcion_de_menu_ingresada == 23:
        print(mensaje_de_desarollo)
    elif opcion_de_menu_ingresada == 0:
        print("\nSaliendo del programa...")
        break
    else:
        print("\nERROR! Ingreso un valor invalido en el menu principal.")