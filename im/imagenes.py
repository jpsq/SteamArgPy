from PIL import Image,ImageTk
from customtkinter import CTkImage
import requests

def cargarImagen(direccion_imagen):

    """
    Funcion que genera el objeto ImageTk de una direccion de imagen
    
        Parametros:
            direccion_imagen: string ,  direccion local de la imagen
        
        Returna:
            render : ImageTk de la imagen
    """
    imagen = CTkImage(dark_image=Image.open(direccion_imagen))
    #render = ImageTk.PhotoImage(imagen)

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

    direccion_local_imagen = f"./images/{nombre_juego}.jpg" # El nombre con el que queremos guardarla
    imagen = requests.get(url_imagen).content

    file = open(direccion_local_imagen, 'wb')
    try:
        file.write(imagen)
    finally:
        file.close()

    return direccion_local_imagen

