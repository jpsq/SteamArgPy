from PIL import Image,ImageTk
import requests

def cargarImagen(direccion_imagen):

    """
    Function that generates the ImageTk object from a image direction
    
        Parameter:
            direccion_imagen: string ,  image local direction 
        
        Returns:
            render : ImageTk object from the image
    """
    imagen = Image.open(direccion_imagen)
    render = ImageTk.PhotoImage(imagen)

    return render

def descargarImagen(url_imagen, nombre_juego):

    """_summary_

    Args:
        url_imagen (str): url of the image 
        nombre_juego (str_): name of game, used for the image archive
    Return:
        direction local of the image
    """

    direccion_local_imagen = f"./images/{nombre_juego}.jpg" # El nombre con el que queremos guardarla
    imagen = requests.get(url_imagen).content
    with open(direccion_local_imagen, 'wb') as handler:
	    handler.write(imagen)
    return direccion_local_imagen

