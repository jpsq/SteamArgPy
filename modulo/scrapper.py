import requests
from bs4 import BeautifulSoup

class scrapper:

    def obtener(nombre_juego):

        #cosas a devolver:  [titulo, precio, url_imagen]
        datos_juego = []

        url_a_scrappear = f"https://store.steampowered.com/search/?term=" + nombre_juego.replace(" ","+")


