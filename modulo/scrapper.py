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
    pagina = requests.get(url_a_scrappear)
    soup = BeautifulSoup(pagina.text, 'lxml')

    #cargo el primero elemento de la lista resultado de steam
    div_principal = soup.find(class_="search_result_row")

    div = div_principal.find(class_="col search_capsule")
    lista = div.contents
    datos_juego.insert(2, lista[0]["src"])  # url de la imagen

    div = div_principal.find(class_="col search_name ellipsis")
    lista = div.contents
    datos_juego.insert(0, lista[1].get_text()) # valor de la etiqueta, en este caso el nombre del juego

    indice_lista = 0 #para caso inicial sin descuento
    div = div_principal.find(class_="col search_price responsive_secondrow")
    if div == None: #si no encontro el precio con esa clase, uso la clase para cuando esta en oferta
        div = div_principal.find(class_="col search_price discounted responsive_secondrow")
        indice_lista = 1 #para caso con descuento
    lista = div.contents
    
    datos_juego.insert(1, lista[indice_lista].get_text().replace('.', '').replace(',', '.'))
    indice_inicia_numero = datos_juego[1].find('$')
    datos_juego[1] = float(
                        datos_juego[1][indice_inicia_numero+2: len(datos_juego[1])]
    )

    return datos_juego
