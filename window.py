from tkinter import *
from im import imagenes as im
from modulo import juego as mod
from modulo import scrapper as sc

class Window:

    def __init__(self):
        self.ventana=Tk()
        self.ventana.title("Steam Arg Py")
        self.ventana.geometry("450x300")
        self.ventana.resizable(1,0)
        self.ancho = 400

        self.total = 0
        self.lista_juegos = list()

        self.label_total = Label(self.ventana, text= f"Total: ${self.total}")
        self.label_total.pack()

        self.entrada = StringVar()
        Entry(self.ventana, textvariable=self.entrada).pack()
        self.bBusqueda = Button(self.ventana,text="Agregar juego", command=self.agregar).pack()

        self.frame = LabelFrame(self.ventana)
        self.frame.config(bg= "#16202D")

        self.mycanvas = Canvas(self.frame)
        self.mycanvas.pack(side=LEFT,fill="both", expand="yes")
        self.mycanvas.config(bg= "#16202D")

        self.yscrollbar = Scrollbar (self.frame, orient="vertical", command=self.mycanvas.yview )
        self.yscrollbar.pack(side=RIGHT, fill="y")

        self.mycanvas.configure(yscrollcommand=self.yscrollbar.set)
        #cuando el canva cambie de tamaño, tmb ajusto la region de desplazamiento del scroll (creo que esta linea en este caso no funciona, por eso la agregue en el metodo agregar)
        #self.mycanvas.bind('<Configure>', lambda e: self.mycanvas.configure(scrollregion = self.mycanvas.bbox('all')))

        self.myframe = Frame(self.mycanvas)
        self.myframe.config(bg= "#16202D")

        self.mycanvas.create_window((0,0), window=self.myframe, anchor="nw")

        self.frame.pack(fill="both", expand="yes", padx=10, pady=10)

    def getFrameGrid(self):
        return self.myframe
    
    def iniciar(self):
        self.ventana.mainloop()

    def ajustar_ancho_ventana(self, ancho_juego_agregado):
        """
        Funcion que checkea si el ancho viejo de la ventana necesita ajustarse al agregar un juego de ancho mayor

        Parametros:
            ancho_juego_agregado int: ancho del ultimo juego agregado
        Retorna: None
        """
        self.ancho = self.mycanvas.winfo_reqwidth()
        if(ancho_juego_agregado > self.ancho):
            self.ventana.geometry(f"{ancho_juego_agregado+40}x300") #40 extra por el scrollbar

    def agregar(self):
        """
        Funcion que agrega a la lista de juegos de la clase un juego nuevo, tomando los datos del campo de entrada
        y haciendo scraping con la clase scrapper ("sc"), descargando y generando la imagen para luego crear
        el juego con su constructor (el juego renderiza su propia vista en esta ventana).
    
        Parameter:
            None
        
        Returns:
            None
        """

        datos_juego = sc.obtener(self.entrada.get())
        render = im.cargarImagen( im.descargarImagen(datos_juego[2], self.entrada.get().replace(" ", "_") ) )
        self.lista_juegos.insert( len(self.lista_juegos), mod.Juego(datos_juego[0], render, datos_juego[1],  self.getFrameGrid())) 
        
        #es necesario asctualizar para evitar retrasos en la actualizacion del scrollbar
        self.frame.update()
        self.mycanvas.update()
        self.myframe.update()

        #reconfiguro el scrollbar para el nuevo tamaño del canvas y re renderizo el frame
        self.mycanvas.configure(scrollregion = self.mycanvas.bbox("all"))
        self.frame.pack(fill="both", expand="yes", padx=10, pady=10)

        #actualizar ancho de la ventana   
        self.ajustar_ancho_ventana(self.lista_juegos[-1].getFrame().winfo_reqwidth())

        self.actualizar_total(self.lista_juegos[-1].getPrecioFinal())

    def actualizar_total(self, precio):
        """
        La funcion actualiza el valor del total, y el label de la ventana que lo muestra

        Parametros:
            precio (int): precio del ultimo juego agregado

        Retorna:
            None
        """
        self.total += precio
        self.label_total.config(text=f"Total: ${format(self.total, '0.2f')}")
        

        
