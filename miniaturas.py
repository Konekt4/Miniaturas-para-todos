#Konekt4
#Fecha: 25/07/2024
#Versión: 0.1

from os import system
import time

def mini():
    print("Para descargar la miniatura, debes de colocar el VIDEO_ID del enlace")
    print("Por ejemplo: https://www.youtube.com/watch?v=VIDEO_ID")
    video_id = input("VIDEO_ID: ")
    miniatura_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
    system(f"curl -o {video_id}.jpg {miniatura_url}")
    print("\nMiniatura descargada")
    input("Presiona enter para continuar")

def programa(encendido):
    while encendido == True:
        print("Hecho por Konekt4")
        print("Bienvenido a mi programa")
        print("1. Descargar miniatura")
        print("2. Salir")
        opcion = int(input("Opción: "))
        if opcion == 1:
            system("cls")
            mini()
            time.sleep(2)
            system("cls")

        elif opcion == 2:
            encendido = False
        else:
            system("cls")
            print("Opción no válida")
            time.sleep(2)

def imprimir():
    encendido = True
    programa(encendido)

imprimir()