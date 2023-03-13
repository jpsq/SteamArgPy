import tkinter as tk
from modulo import juego as mod
from modulo import scrapper as sc
from im import imagenes as im

def agregar(entrada, column):

    datos_juego = sc.obtener(entrada)
    render = im.cargarImagen( im.descargarImagen(datos_juego[2], entrada.replace(" ", "_") ) )
    juego = mod.Juego(datos_juego[0], render, datos_juego[1],  frame_buttons, column )

    medidas = [juego.frame.winfo_width(),juego.frame.winfo_height()]
    return medidas


ventana = tk.Tk()
ventana.grid_rowconfigure(0, weight=1)
ventana.columnconfigure(0, weight=1)
ventana.geometry("600x600")

frame_grid = tk.Frame(ventana, bg="gray")
frame_grid.grid(sticky='news')

# Create a frame for the canvas with non-zero row&column weights
frame_canvas = tk.Frame(frame_grid)
frame_canvas.grid(row=2, column=0, pady=(5, 0), sticky='nw')
frame_canvas.grid_rowconfigure(0, weight=1)
frame_canvas.grid_columnconfigure(0, weight=1)

# Set grid_propagate to False to allow 5-by-5 buttons resizing later
frame_canvas.grid_propagate(False)

# Add a canvas in that frame
canvas = tk.Canvas(frame_canvas, bg="yellow")
canvas.grid(row=0, column=0, sticky="news")

# Link a scrollbar to the canvas
scroll = tk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
scroll.grid(row=0, column=1, sticky='ns')
canvas.configure(yscrollcommand=scroll.set)

# Create a frame to contain the buttons
frame_buttons = tk.Frame(canvas, bg="blue")
canvas.create_window((0, 0), window=frame_buttons, anchor='nw')

# Add 9-by-5 buttons to the frame
rows = 1
columns = 1
# buttons = [[tk.Button() for j in range(columns)] for i in range(rows)]
# for i in range(0, rows):
#     for j in range(0, columns):
#         buttons[i][j] = tk.Button(frame_buttons, text=("%d,%d" % (i+1, j+1)))
#         buttons[i][j].grid(row=i, column=j, sticky='news')

medidas = agregar("elden ring",1)

# Update buttons frames idle tasks to let tkinter calculate buttons sizes
frame_buttons.update_idletasks()

# Resize the canvas frame to show exactly 5-by-5 buttons and the scrollbar
# first5columns_width = sum([buttons[0][j].winfo_width() for j in range(0, 5)])
# first5rows_height = sum([buttons[i][0].winfo_height() for i in range(0, 5)])
frame_canvas.config(
                    width= medidas[0] + scroll.winfo_width(),
                    height=medidas[1]
                    )

# Set the canvas scrolling region
canvas.config(scrollregion=canvas.bbox("all"))

# Launch the GUI
ventana.mainloop()