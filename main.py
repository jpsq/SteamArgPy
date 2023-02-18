from im import imagenes as im
from modulo import juego as mod
from modulo import scrapper as sc
from tkinter import Tk


window = Tk()

lista = sc.obtener("battlefront")
render = im.cargarImagen( im.descargarImagen(lista[2], "starwars") )
juego1 = mod.Juego(lista[0],render,lista[1],window)

lista = sc.obtener("elden ring")
render = im.cargarImagen( im.descargarImagen(lista[2], "eldenring") )
juego2 = mod.Juego(lista[0],render,lista[1],window)

window.mainloop()
