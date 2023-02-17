from PIL import Image,ImageTk

def imagen(direccion_imagen):

    """
    Function that generates the ImageTk object from a image direction
    
        Parameter:
            direccion_imagen: string ,  image direction
        
        Returns:
            render : ImageTk object from the image
    """
    imagen = Image.open(direccion_imagen)
    render = ImageTk.PhotoImage(imagen)

    return render
