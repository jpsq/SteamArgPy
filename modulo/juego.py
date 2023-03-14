from tkinter import Frame,Label

class Juego:

    def __init__(self,nombre,render_logo,precio_original,ventana):
        """
        Constructor de clase:
            Carga valores a la instancia y crea el Tkinter frame para este objeto
            
        Parametro:
            nombre: string
            render_logo = ImageTk object , not work create the ImageTk in the class with de direction of image
            precio_original = float
            ventana = Tk

        Retorna:
            None
        """

        self.precio_original = precio_original
        self.precio_final = self.precio_original * 1.65 #esto dsp hacer con scraping de impuestos
        self.nombre = nombre
        self.render_logo = render_logo

        #agrego los elementos a el frame del juego q desp se cargara en la ventana pasada por parametro
        self.frame = Frame(ventana)
        self.frame.config(
            bg= "#16202D",
        )

        #label imagen
        labelImagen = Label(self.frame, image=self.render_logo)
        labelImagen.config(bg="black")
        labelImagen.pack(anchor="w",side="left", padx=5)
        #label titulo del juego
        labelNombre = Label(self.frame, text=self.nombre)
        labelNombre.config(bg="#16202D", fg="white", font=("",14))
        labelNombre.pack(anchor="n", side="top")

        #label precio original
        labelPrecioOriginal=Label(self.frame, text=f"PRECIO ORIGINAL = ARS $"+format(self.precio_original, '0.2f'))
        labelPrecioOriginal.config(bg="#16202D",fg="#C5C3C0")
        labelPrecioOriginal.pack(anchor="s", side="bottom")

        #label precio final  
        labelPrecioFinal = Label(self.frame, text=f"PRECIO FINAL = ARS $"+format(self.precio_final, '0.2f'))
        labelPrecioFinal.config(fg="#C5C3C0",bg="#16202D")
        labelPrecioFinal.pack(anchor="s", side="bottom")
        
        self.frame.pack(fill="x", expand="yes",anchor="n")

    def getPrecioFinal(self):

        return self.precio_final