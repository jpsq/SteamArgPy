from im import cargaImagen as im
from modulo import juego as mod
from tkinter import Tk


window = Tk()

render = im.imagen("./logo.png")
juego1 = mod.Juego("Elden Ring",render,101,window)

window.mainloop()
