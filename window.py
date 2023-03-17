from tkinter import *
from customtkinter import *



class Window:

    def __init__(self,controlador):

        set_appearance_mode("dark")
        set_default_color_theme("dark-blue")

        self.__controlador = controlador

        self.__ventana=CTk()
        self.__ventana.title("Steam Arg Py")
        self.__ventana.geometry("600x600")
        self.__ventana.resizable(1,1)

        self.__total = 0

        self.__label_total = CTkLabel(master=self.__ventana, text= f"Total: ${self.__total}")
        self.__label_total.pack()

        self.__entrada = StringVar()
        self.__campo_entrada = CTkEntry(master=self.__ventana, textvariable=self.__entrada)
        self.__campo_entrada.bind('<Return>', self.agregar)
        self.__campo_entrada.pack()

        self.__boton_busqueda = CTkButton(master=self.__ventana,text="Agregar juego", command=lambda: controlador.agregar(self.__entrada)).pack()

        self.__frame = CTkFrame(master=self.__ventana)

        self.__canvas = Canvas(self.__frame)
        self.__canvas.config(bg="#1A1A1A")
        self.__canvas.pack(side=LEFT,fill="both", expand="yes")
        #scrollbar
        self.__scrollbar = Scrollbar(self.__frame, orient="vertical", command=self.__canvas.yview)
        self.__scrollbar.pack(side=RIGHT, fill="y")
        #config scrollbar to canva
        self.__canvas.configure(yscrollcommand=self.__scrollbar.set)

        self.__frame_canva = Frame(master=self.__canvas,bg="#1A1A1A")

        self.__canvas.create_window((0,0), window=self.__frame_canva, anchor="nw")

        self.__frame.pack(fill="both", expand="yes", padx=10, pady=10)

    def getFrameGrid(self):
        return self.__frame_canva
    
    def iniciar(self):
        self.__ventana.mainloop()

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
        La funcion suma al valor del total actual la del parametro precio,
        y actualiza el label de la ventana que lo muestra.

        Parametros:
            precio (int): precio del ultimo juego agregado

        Retorna:
            None
        """
        self.__total += precio
        self.__label_total.configure(text=f"Total: ${format(self.__total, '0.2f')}")

    def quitar_a_total(self, precio):
        """
        La funcion resta al valor del total actual la del parametro precio,
        y actualiza el label de la ventana que lo muestra.

        Parametros:
            precio (int): precio del ultimo juego agregado

        Retorna:
            None
        """
        self.__total -= precio
        self.__label_total.config(text=f"Total: ${format(self.__total, '0.2f')}")
        
    def agregar(self, event):
    #esta funcion es especifica para el bindeo del enter
        self.__controlador.agregar(self.__entrada)
