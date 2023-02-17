from modulo import juego as mod
from tkinter import Tk
from PIL import Image,ImageTk

window = Tk()

imagen = Image.open('./logo.png')
render = ImageTk.PhotoImage(imagen)

juego1 = mod.Juego("Elden Ring",render,101,window)

window.mainloop()
