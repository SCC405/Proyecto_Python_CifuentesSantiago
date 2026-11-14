#Modulo de datos

import json
import os

carpeta = os.path.dirname(os.path.abspath(__file__))


def cargar(nombre_archivo):
    ruta = os.path.join(carpeta, nombre_archivo)
    archivo = open(ruta, "r", encoding="utf-8")
    datos = json.load(archivo)
    archivo.close()
    return datos


def guardar(nombre_archivo, datos):
    ruta = os.path.join(carpeta, nombre_archivo)
    archivo = open(ruta, "w", encoding="utf-8")
    json.dump(datos, archivo, indent=4, ensure_ascii=False)
    archivo.close()
