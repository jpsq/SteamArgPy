from tkinter import *

class Window:

    def __init__(self,controlador):

        self.__controlador = controlador

        self.__ventana=Tk()
        self.__ventana.title("Steam Arg Py")
        self.__ventana.geometry("450x300")
        self.__ventana.resizable(1,0)
        self.__ancho = 400

        self.__total = 0

        self.__label_total = Label(self.__ventana, text= f"Total: ${self.__total}")
        self.__label_total.pack()

        self.__entrada = StringVar()
        self.__campo_entrada = Entry(self.__ventana, textvariable=self.__entrada)
        self.__campo_entrada.bind('<Return>', self.agregar)
        self.__campo_entrada.pack()

        self.__boton_busqueda = Button(self.__ventana,text="Agregar juego", command=lambda: controlador.agregar(self.__entrada) ).pack()

        self.__frame = LabelFrame(self.__ventana)
        self.__frame.config(bg= "#16202D")

        self.__canvas = Canvas(self.__frame)
        self.__canvas.pack(side=LEFT,fill="both", expand="yes")
        self.__canvas.config(bg= "#16202D")

        self.__scrollbar = Scrollbar (self.__frame, orient="vertical", command=self.__canvas.yview )
        self.__scrollbar.pack(side=RIGHT, fill="y")

        self.__canvas.configure(yscrollcommand=self.__scrollbar.set)
        #cuando el canva cambie de tamaño, tmb ajusto la region de desplazamiento del scroll (creo que esta linea en este caso no funciona, por eso la agregue en el metodo agregar)
        #self.mycanvas.bind('<Configure>', lambda e: self.mycanvas.configure(scrollregion = self.mycanvas.bbox('all')))

        self.__frame_canva = Frame(self.__canvas)
        self.__frame_canva.config(bg= "#16202D")

        self.__canvas.create_window((0,0), window=self.__frame_canva, anchor="nw")

        self.__frame.pack(fill="both", expand="yes", padx=10, pady=10)

    def getFrameGrid(self):
        return self.__frame_canva
    
    def iniciar(self):
        self.__ventana.mainloop()

    def ajustar_ancho_ventana(self, ancho_juego_agregado):
        """
        Funcion que checkea si el ancho viejo de la ventana necesita ajustarse al agregar un juego de ancho mayor

        Parametros:
            ancho_juego_agregado int: ancho del ultimo juego agregado
        Retorna: None
        """
        self.__ancho = self.__canvas.winfo_reqwidth()
        if(ancho_juego_agregado > self.__ancho):
            self.__ventana.geometry(f"{ancho_juego_agregado+40}x300") #40 extra por el scrollbar

    def actualizarFrames(self):
        #es necesario asctualizar para evitar retrasos en la actualizacion del scrollbar
        self.__frame.update()
        self.__canvas.update()
        self.__frame_canva.update()

        #reconfiguro el scrollbar para el nuevo tamaño del canvas y re renderizo el frame
        self.__canvas.configure(scrollregion = self.__canvas.bbox("all"))
        self.__frame.pack(fill="both", expand="yes", padx=10, pady=10)

    def sumar_a_total(self, precio):
        """
        La funcion actualiza el valor del total, y el label de la ventana que lo muestra

        Parametros:
            precio (int): precio del ultimo juego agregado

        Retorna:
            None
        """
        self.__total += precio
        self.__label_total.config(text=f"Total: ${format(self.__total, '0.2f')}")

    def quitar_a_total(self, precio):

        self.__total -= precio
        self.__label_total.config(text=f"Total: ${format(self.__total, '0.2f')}")
        
    def agregar(self, event):
    #esta funcion es especifica para el bindeo del enter
        self.__controlador.agregar(self.__entrada)