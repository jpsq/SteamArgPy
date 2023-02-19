from tkinter import *
from im import imagenes as im
from modulo import juego as mod
from modulo import scrapper as sc

class Window:
    __ventana = ""
    __frameGrid= ""
    __bBusqueda = "" #boton para agregar
    __lEntrada = "" #label para ingresar el nombre del juego
    __entrada = ""
    __lista_juegos = ""

    def __init__(self):
        self.ventana=Tk()
        self.ventana.title("Steam Arg Py")
        self.ventana.geometry("800x600")
        self.ventana.resizable(0,0)

        self.lista_juegos = list()

        self.entrada = StringVar()
        campo2 = Entry(self.ventana, textvariable=self.entrada).pack()
        self.bBusqueda = Button(self.ventana,text="Agregar juego", command=self.agregar).pack()

        self.frameGrid = Frame(self.ventana)
        self.frameGrid.pack()
        self.frameGrid.pack_propagate(False)

    def getFrameGrid(self):
        return self.frameGrid
    
    def iniciar(self):
        self.ventana.mainloop()

    def agregar(self):

        datos_juego = sc.obtener(self.entrada.get())
        render = im.cargarImagen( im.descargarImagen(datos_juego[2], self.entrada.get().replace(" ", "_") ) )
        self.lista_juegos.insert( len(self.lista_juegos), mod.Juego(datos_juego[0], render, datos_juego[1],  self.getFrameGrid(), len(self.lista_juegos) )) 

    
