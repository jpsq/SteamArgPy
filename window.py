from tkinter import Tk,Frame

class Window:
    __ventana = ""
    __frameGrid= ""

    def __init__(self):
        self.ventana=Tk()
        self.ventana.title("Steam Arg Py")
        self.ventana.geometry("800x600")
        self.ventana.resizable(0,0)

        self.frameGrid = Frame(self.ventana)
        self.frameGrid.pack()

    def getFrameGrid(self):
        return self.frameGrid
    
    def iniciar(self):
        self.ventana.mainloop()
