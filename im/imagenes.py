from PIL import Image
from customtkinter import CTkImage
import requests


def cargarImagen(direccion_imagen):
    """
    Funcion que genera el objeto CTkImage (customtkinter object) a partir de una direccion de imagen

        Parametros:
            direccion_imagen: string , direccion local de la imagen       
        Returna:
            imagen : CTkImage de la imagen
    """

    imagen = CTkImage(dark_image=Image.open(direccion_imagen), size=(120, 45))
    return imagen


def descargarImagen(url_imagen, nombre_juego):
    """
    Funcion que descarga una imagen de una url mediante libreria request

    Parametros:
        url_imagen (str): url de la image 
        nombre_juego (str_): nombre del juego, usado para el archivo de la imagen
    Retorna:
        direccion local de la imagen descargada
    """

    # El nombre con el que queremos guardarla
    direccion_local_imagen = f"./images/{nombre_juego}.jpg"
    imagen = requests.get(url_imagen, timeout=10).content

    file = open(direccion_local_imagen, 'wb')
    try:
        file.write(imagen)
    finally:
        file.close()

    return direccion_local_imagen
