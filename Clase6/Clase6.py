import requests
from bs4 import BeautifulSoup as soup
import pandas as pd


def simple_request(link):
    headers = {'Content-Type': 'application/xml'}
    r = requests.get(link, headers=headers)
    print(r)
    return r.content


web_content =  simple_request('https://animeflv.net/')

type(web_content)

def simple_parser(contenido_web):
    page_soup = soup(str(contenido_web), "html.parser")
    print(type(page_soup))
    # print(page_soup)

simple_parser(web_content)




def simple_parser(contenido_web):
    page_soup = soup(str(contenido_web), "html.parser")
    return page_soup

sopita = simple_parser(web_content)

links = sopita.findAll("a")
links

links = sopita.findAll("a").get("href")
links

links = [link.get("href") for link in links]

links2 = sopita.findAll("a", {"class":"fa-play-circle"})
len(links2)

links2 = sopita.find("ul", {"class":"ListSdbr"})
links2
links2[0]


s = requests.Session()


#Busca un elemento dentro del código web de la página idetificando el tag del elemento, y se especifica una segunda indicacion tipo-elemento_a_buscar para seleccionar el elemento correcto. El campo texto corresponde a si lo buscado está como str
def sopear_elemento(url, tag, tipo, elemento_a_buscar, texto):
    r = s.get(url)
    data = soup(r.content, "html.parser")
    if texto == True:
        elemento = data.find(str(tag), {str(tipo) : str(elemento_a_buscar)}).text.strip()
    else:
        elemento = data.find(str(tag), {str(tipo) : str(elemento_a_buscar)})
    return elemento

def sopear_varios_elementos(url, tag, tipo, elemento_a_buscar):
    r = s.get(url)
    data = soup(r.content, "html.parser")
    elementos = data.findAll(str(tag), {str(tipo) : str(elemento_a_buscar)})
    return elementos