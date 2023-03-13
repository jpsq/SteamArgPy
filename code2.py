from tkinter import *
from tkinter import ttk
from modulo import juego2 as mod
from modulo import scrapper as sc
from im import imagenes as im

def agregar(entrada):

    datos_juego = sc.obtener(entrada)
    render = im.cargarImagen( im.descargarImagen(datos_juego[2], entrada.replace(" ", "_") ) )
    juego = mod.Juego(datos_juego[0], render, datos_juego[1],  myframe)

ventana = Tk()
ventana.geometry("500x500")
ventana.resizable(1, 1)
ventana.title("ventana")

frame = LabelFrame(ventana)
#wrapper2 = LabelFrame(ventana)

mycanvas = Canvas(frame)
mycanvas.pack(side=LEFT,fill="both", expand="yes")

yscrollbar = ttk.Scrollbar (frame, orient="vertical", command=mycanvas.yview )
yscrollbar.pack(side=RIGHT, fill="y")

mycanvas.configure(yscrollcommand=yscrollbar.set)
mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion = mycanvas.bbox('all')))

myframe = Frame(mycanvas)

mycanvas.create_window((0,0), window=myframe, anchor="nw")

agregar("bioshock")
agregar("bioshock")
agregar("bioshock")
agregar("bioshock")
agregar("bioshock")
agregar("bioshock")
agregar("bioshock")
agregar("bioshock")
agregar("bioshock")


frame.pack(fill="both", expand="yes", padx=10, pady=10)
#wrapper2.pack(fill="both", expand="yes", padx=10, pady=10)
              
ventana.mainloop()


