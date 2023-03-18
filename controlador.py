import window as w
from im import imagenes as im
from modulo import juego as mod
from modulo import scrapper as sc

class Controlador:
    __lista_juegos = None
    __ventana = None

    def __init__(self):
        self.__lista_juegos = list()
        self.__ventana = w.Window(self)

    def agregar(self,entrada):
        datos_juego = sc.obtener(entrada.get())
        logo_juego = im.cargarImagen( im.descargarImagen(datos_juego[2], entrada.get().replace(" ", "_") ) )
        self.__lista_juegos.append(mod.Juego(datos_juego[0], logo_juego, datos_juego[1],  self.__ventana.getFrameGrid(),self)) 
        
        self.__ventana.actualizarFrames()
        self.__ventana.sumar_a_total(self.__lista_juegos[-1].getPrecioFinal())

    def iniciar(self):
        self.__ventana.iniciar()

    def borrar_juego(self,juego_a_quitar):
        if juego_a_quitar.getCheck_estado() == 1:
            self.__ventana.quitar_a_total(juego_a_quitar.getPrecioFinal())
        
        self.__lista_juegos.remove(juego_a_quitar)


    def desactivar_juego(self,juego_a_desactivar):
        self.__ventana.quitar_a_total(juego_a_desactivar.getPrecioFinal())

    def activar_juego(self,juego_a_activar):
        self.__ventana.sumar_a_total(juego_a_activar.getPrecioFinal())