from tkinter import *
from im import imagenes as im
from modulo import juego as mod
from modulo import scrapper as sc

class Window:

    def __init__(self):
        self.ventana=Tk()
        self.ventana.title("Steam Arg Py")
        self.ventana.geometry("500x400")
        self.ventana.resizable(0,0)

        self.lista_juegos = list()

        self.entrada = StringVar()
        Entry(self.ventana, textvariable=self.entrada).pack()
        self.bBusqueda = Button(self.ventana,text="Agregar juego", command=self.agregar).pack()

        self.frame = LabelFrame(self.ventana)

        self.mycanvas = Canvas(self.frame)
        self.mycanvas.pack(side=LEFT,fill="both", expand="yes")

        self.yscrollbar = Scrollbar (self.frame, orient="vertical", command=self.mycanvas.yview )
        self.yscrollbar.pack(side=RIGHT, fill="y")

        self.mycanvas.configure(yscrollcommand=self.yscrollbar.set)
        #cuando el canva cambie de tamaño, tmb ajusto la region de desplazamiento del scroll (creo que esta linea en este caso no funciona, por eso la agregue en el metodo agregar)
        self.mycanvas.bind('<Configure>', lambda e: self.mycanvas.configure(scrollregion = self.mycanvas.bbox('all')))

        self.myframe = Frame(self.mycanvas)

        self.mycanvas.create_window((0,0), window=self.myframe, anchor="nw")

        self.frame.pack(fill="both", expand="yes", padx=10, pady=10)

    def getFrameGrid(self):
        return self.myframe
    
    def iniciar(self):
        self.ventana.mainloop()

    def agregar(self):

        datos_juego = sc.obtener(self.entrada.get())
        render = im.cargarImagen( im.descargarImagen(datos_juego[2], self.entrada.get().replace(" ", "_") ) )
        self.lista_juegos.insert( len(self.lista_juegos), mod.Juego(datos_juego[0], render, datos_juego[1],  self.getFrameGrid())) 
        
        self.mycanvas.configure(scrollregion = self.mycanvas.bbox('all'))
        self.frame.pack(fill="both", expand="yes", padx=10, pady=10)
    
