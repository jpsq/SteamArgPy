from tkinter import Checkbutton,IntVar
from customtkinter import CTkFrame,CTkLabel,CTkButton

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
        self.__free_to_play = False
        self.__precio_original = precio_original
        if(type(self.__precio_original)==float):
            self.__precio_final = self.__precio_original * 1.75
        else:
            self.__free_to_play = True
        self.__nombre = nombre
        self.__render_logo = render_logo
        self.__controlador = controlador

        #agrego los elementos a el frame del juego q desp se cargara en la ventana pasada por parametro
        self.__frame = CTkFrame(master=ventana)

        #label imagen
        labelImagen = CTkLabel(master=self.__frame, text="",image=self.__render_logo)
        labelImagen.pack(anchor="w",side="left", padx=5,pady=3)

        #label titulo del juego
        labelNombre = CTkLabel(master=self.__frame, text=self.__nombre, font=("",22))
        labelNombre.pack(anchor="w",side="left",padx=7)

        self.__frame_de_labels = CTkFrame(master=self.__frame,fg_color="#212121")

        if(self.__free_to_play==True):
            #label precio original
            labelPrecioOriginal=CTkLabel(master=self.__frame_de_labels, text="Free to Play")
        else:
            #checkbutton activar/desactivar
            self.__check_estado = IntVar()
            self.__check_estado.set(1)
            self.__check = Checkbutton(self.__frame,variable=self.__check_estado ,command=self.cambiar_estado)
            self.__check.config(bg= "#212121")
            self.__check.pack(anchor="center",side="left")

            labelPrecioOriginal=CTkLabel(master=self.__frame_de_labels, text=f"Precio base: ARS $"+format(self.__precio_original, '0.2f'))
            #label precio final  
            self.__labelPrecioFinal = CTkLabel(master=self.__frame_de_labels, text=f"Precio final: ARS $"+format(self.__precio_final, '0.2f'))
            self.__labelPrecioFinal.pack(anchor="w",side="bottom", pady=2)
            
        labelPrecioOriginal.pack(anchor="w",side="top", pady=2)

        self.__frame_de_labels.pack(anchor="w",side="left",padx=7)

        #boton quitar
        if(self.__free_to_play==True):
            CTkButton(master=self.__frame, text="Quitar", command=self.__frame.destroy).pack(anchor="e",side="left", padx=7)
        else:
            CTkButton(master=self.__frame, text="Quitar", command=self.borrar).pack(anchor="e",side="left", padx=7)

        self.__frame.pack(fill="x", expand="yes",anchor="n")

    def getPrecioFinal(self):
        return self.__precio_final
    
    def getFrame(self):
        return self.__frame

    def borrar(self):
        self.__frame.destroy()
        self.__controlador.borrar_juego(self)

    def cambiar_estado(self):
        if self.__check_estado.get()==0:
            self.__controlador.desactivar_juego(self)
        elif self.__check_estado.get()==1:
            self.__controlador.activar_juego(self)
    
    def getCheck_estado(self):
        return self.__check_estado.get()
