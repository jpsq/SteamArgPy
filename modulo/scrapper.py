import requests
from bs4 import BeautifulSoup


def obtener(nombre_juego):

    """Obtener:

    The function scrap from the url of steam search the name, price and url of image logo and 
    storage in a list(str,float,str) in this order:
    list(name, price, url_image)
    
    Paramaters:
        nombre_juego: string , string with the name of the game to search and scrap dates

    Returns:
        datos_jueg: list(str,float,str) 
    """

    # cosas a devolver:  [titulo, precio, url_imagen]
    datos_juego = list()

    url_a_scrappear = f"https://store.steampowered.com/search/?term=" + \
    nombre_juego.replace(" ", "+")
    r = requests.get(url_a_scrappear)
    soup = BeautifulSoup(r.text, 'lxml')

    div = soup.find(class_="col search_capsule")
    lista = div.contents
    datos_juego.insert(2, lista[0]["src"])  # url de la imagen

    div = soup.find(class_="col search_name ellipsis")
    lista = div.contents
    datos_juego.insert(0, lista[1].get_text()) # valor de la etiqueta, en este caso el nombre dle juego

    div = soup.find(class_="col search_price responsive_secondrow")
    lista = div.contents
    datos_juego.insert(1, lista[0].get_text().replace('.', '').replace(',', '.'))
    indice_inicia_numero = datos_juego[1].find('$')
    datos_juego[1] = float(
                        datos_juego[1][indice_inicia_numero+2: len(datos_juego[1])]
    )

    return datos_juego
