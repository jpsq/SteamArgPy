from tkinter import Frame,Label

class Juego:

    __precio_original = ""
    __precio_final = ""
    __nombre = ""
    __render_logo = ""
    __frame = ""


    def __init__(self,nombre,render_logo,precio_original,ventana):
        self.precio_original = precio_original
        self.precio_final = self.precio_original * 1.65 #esto dsp hacer con scraping de impuestos
        self.nombre = nombre
        self.render_logo = render_logo

        #agrego los elementos a el frame del juego q desp se cargara en la ventana
        self.frame = Frame(ventana)
        Label(self.frame, image=self.render_logo).pack(anchor="w",side="left", padx=5)
        Label(self.frame, text=self.nombre).pack(anchor="n", side="top")
        Label(self.frame, text=format(self.precio_final, '0.2f')).pack(anchor="s", side="bottom")
        self.frame.pack()

    def getPrecioFinal(self):
        return self.precio_final