import PyPDF2



def process_file(filename):
    pags = []
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    num_pages = pdfReader.numPages
    count = 0
    text = ""
    while count < num_pages:
        pageObj = pdfReader.getPage(count)
        count +=1
        text += pageObj.extractText()
        pags.append(pageObj.extractText())
    return text, pags, num_pages

filename = "relatos de poder.pdf"

texto_libro, pags_libro, cantidad_de_pags = process_file(filename)

texto_libro.count("?")

def contar_preguntas(lista):
    contador_general = 0
    for i in range(len(lista)):
        contador_local = str(lista[i]).count("?")
        contador_general += contador_local
    return contador_general

cantidad_preguntas = contar_preguntas(pags_libro)





# Clase6
from bs4 import BeautifulSoup as soup
import pandas as pd
import requests


def simple_request(link):
    headers = {'Content-Type': 'application/json'}
    r = requests.get(link)
    return r.content, r

link = 'https://soundcloud.com/uiceheidd/bandit-ft-nba-youngboy'
# simple_request(link)
web_content, request_status =  simple_request(link)

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

<a href="un link">Ir acá pa ver más</a>

links = sopita.findAll("a")
links


links = [link.get("href") for link in links]


links2 = sopita.findAll("div", {"class":"downloadLinks"})
len(links2)



links2[0]
links2[0].text


s = requests.Session()

links = sopita.find("dd").text

#Busca un elemento dentro del código web de la página idetificando el tag del elemento, y se especifica una segunda indicacion tipo-elemento_a_buscar para seleccionar el elemento correcto. El campo texto corresponde a si lo buscado está como str
def sopear_elemento(url, tag, tipo, elemento_a_buscar, texto):
    r = s.get(url)
    data = soup(r.content, "html.parser")
    if texto == True:
        elemento = data.find(str(tag), {str(tipo) : str(elemento_a_buscar)}).text.strip()
    else:
        elemento = data.find(str(tag), {str(tipo) : str(elemento_a_buscar)})
    return elemento

data = sopear_elemento(link, "meta", "itemprop", "genre", 0)



def sopear_varios_elementos(url, tag, tipo, elemento_a_buscar):
    r = s.get(url)
    data = soup(r.content, "html.parser")
    elementos = data.findAll(str(tag), {str(tipo) : str(elemento_a_buscar)})
    return elementos
