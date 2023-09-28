### SteamArgPy

(OUTDATED) Debido a cambios en la pagina web de Steam, la aplicacion no funciona correctamente hasta un proximo fix.

Carrito de Steam, proyecto realizado para aprender Python y GUIs con Tkinter.

El proyecto utiliza web scraping con BeautifulSoup para tomar datos de la web de "https://store.steampowered.com/", para luego visualizar un carrito de compras (con impuestos Argentinos incluidos) en una interfaz de Tkinter con la libreria "https://github.com/TomSchimansky/CustomTkinter" (CustomTkinter).

- ### Instalación:
En /build se encuentra un .zip con un empaquetado para Windows.

- ### Uso:
Ingrese el nombre del juego que quiera agregar al carrito mediante el campo de entrada, al presionar Enter o usando el boton este se agregara segun los resultados de la pagina de Steam.
Los juegos pueden quitarse o en su lugar desactivarse para que ya no cuenten en el total pero se mantengan los datos en la interfaz.

- ### Imagen de muestra de la interfaz:

![](https://github.com/jpsq/SteamArgPy/blob/master/preview.png?raw=true)
###

NOTA: si tienes problemas con la importacion de pil.image y pil.imagetk usa:
pip install --upgrade --force-reinstall Pillow
