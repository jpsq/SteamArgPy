from tkinter import Frame,Label,Button

class Juego:

    __precio_original = 0
    __precio_final = 0
    __nombre = ""
    __render_logo = None
    __frame = None
    __controlador = None


    def __init__(self,nombre,render_logo,precio_original,ventana,controlador):
        """
        Constructor de clase:
            Carga valores a la instancia y crea el Tkinter frame para este objeto
            
        Parametro:
            nombre: string
            render_logo = ImageTk object , not work create the ImageTk in the class with de direction of image
            precio_original = float
            ventana = Tk Frame,  en en donde se inserta el frame del juego
            ventana_principal = clase window (w), 

        Retorna:
            None
        """

        self.__precio_original = precio_original
        self.__precio_final = self.__precio_original * 1.75
        self.__nombre = nombre
        self.__render_logo = render_logo
        self.__controlador = controlador

        #agrego los elementos a el frame del juego q desp se cargara en la ventana pasada por parametro
        self.__frame = Frame(ventana)
        self.__frame.config(
            bg= "#16202D",
            border=3,
            relief="solid"
        )
        #label imagen
        labelImagen = Label(self.__frame, image=self.__render_logo)
        labelImagen.config(bg="black")
        labelImagen.pack(anchor="w",side="left", padx=5)
        #label titulo del juego
        labelNombre = Label(self.__frame, text=self.__nombre)
        labelNombre.config(bg="#16202D", fg="white", font=("",14))
        labelNombre.pack(anchor="n", side="top")

        #label precio original
        labelPrecioOriginal=Label(self.__frame, text=f"PRECIO ORIGINAL = ARS $"+format(self.__precio_original, '0.2f'))
        labelPrecioOriginal.config(bg="#16202D",fg="#C5C3C0")
        labelPrecioOriginal.pack(anchor="s", side="bottom")

        #label precio final  
        labelPrecioFinal = Label(self.__frame, text=f"PRECIO FINAL = ARS $"+format(self.__precio_final, '0.2f'))
        labelPrecioFinal.config(fg="#C5C3C0",bg="#16202D")
        labelPrecioFinal.pack(anchor="s", side="bottom")

        #botones quitar y deshabilitar
        boton_borrar = Button(self.__frame, text="Quitar", command=self.borrar).pack()
        
        self.__frame.pack(fill="x", expand="yes",anchor="n")

    def getPrecioFinal(self):
        return self.__precio_final
    
    def getFrame(self):
        return self.__frame

    def borrar(self):
        self.__frame.destroy()
        self.__controlador.borrar_juego(self)
