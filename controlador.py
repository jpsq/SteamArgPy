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
        if(datos_juego==0):
            self.__ventana.mostrar_alerta_juego_no_encontrado()
        else:
            logo_juego = im.cargarImagen( im.descargarImagen(datos_juego[2], entrada.get().replace(" ", "_") ) )
            self.__lista_juegos.append(mod.Juego(datos_juego[0], logo_juego, datos_juego[1],  self.__ventana.getFrameGrid(),self)) 
            
            self.__ventana.actualizarFrames()
            self.__ventana.sumar_a_total(self.__lista_juegos[-1].getPrecioFinal())
            self.__ventana.sumarJuegoActivo()
            self.__ventana.sumarCantJuegos()


    def iniciar(self):
        self.__ventana.iniciar()

    def borrar_juego(self,juego_a_quitar):

        if not juego_a_quitar.is_free_to_play():
            if juego_a_quitar.getCheck_estado():
                self.__ventana.quitar_a_total(juego_a_quitar.getPrecioFinal())
                self.__ventana.restarJuegoActivo()
        else:
            self.__ventana.restarJuegoActivo()

        self.__lista_juegos.remove(juego_a_quitar)
        self.__ventana.restarCantJuegos()

    def desactivar_juego(self,juego_a_desactivar):
        self.__ventana.quitar_a_total(juego_a_desactivar.getPrecioFinal())
        self.__ventana.restarJuegoActivo()

    def activar_juego(self,juego_a_activar):
        self.__ventana.sumar_a_total(juego_a_activar.getPrecioFinal())
        self.__ventana.sumarJuegoActivo()