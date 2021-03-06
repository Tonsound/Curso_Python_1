
import pandas as pd

lista = ['pablo', 'andres', 'leti', 'jose']

df = pd.DataFrame(lista)

df2 = df.transpose() #transpone la base de datos

frame_data = {'name': ['James', 'Jason', 'Rogers'], 'age': [18, 20, 22], 'job': ['Assistant', 'Manager', 'Clerk']}
df = pd.DataFrame(frame_data, index = frame_data['name'])

df2 = df.drop(['Rogers']) #elimina la fila en que se encuentre 'Rogers' dentro de la columna indice, en esta base de datos se establecio que el index es la cokumna con los nombres, si no agregamos un index, pandas elaborará uno numerico y lo agregará como columna index
df2 = df.drop(df.index[[1, 1]]) #elimina un rango de filas

df2 = df.drop_duplicates(['name']) #bota los duplicados de la columna name
df2 = df.drop(['job'], axis=1) #elimina la columna 'job' Si el valor del eje es 1 significa que queremos eliminar columnas, si el valor del eje es 0 o se deja en blanco significa que la fila se eliminará


suma = df['age'].sum() # esto nos permite sumar los datos de la columna 'A'
valores_unicos =  df['age'].nunique() #cuenta los valores unicos
cantidad_de_datos = df['age'].count() # cuenta todos los valores de la columna 'A'
df[0:1] #selecciona las 3 primeras filas

df2 = df[df['Estado interno'] == 'problemas']




#from PyPDF2 import PdfFileReader, PdfFileWriter
import PyPDF2
#pip install PyPDF2
import os

pags = []


def process_file(filename):
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
    print('Leido')

filename = "Sopa de Wuhan ASPO.pdf"

process_file(filename)

indice = pags[9].split('\n')

cap1 = pags[16]

citas = []

def get_citas(lista):
    for i in range(len(pags)):
        if '[*]' in pags[i]:
            citas.append(pags[i])
            print(citas)

get_citas(pags)

citas = []


def get_citas(lista):
    for i in range(len(pags)):
        if '[*]' in pags[i]:
            citas.append(pags[i].split('[*]')[1])
    print('Listas tomadas')

get_citas(pags)

autores = []

def get_autores(lista):
    for i in range(len(pags)):
        if '[*]' in pags[i]:
            cita = pags[i].split('[*]')[1]
            autor = cita.split('\n')[0]
            autores.append(autor)
    print('Listas tomadas')


get_autores(pags)

from pandas import ExcelWriter as ew
import pandas as pd

df = pd.DataFrame(autores)

def generar_DF_Excel(df, nombre_archivo):
    nombre_final = nombre_archivo + '.xlsx' 
    writer = ew(nombre_final)
    df.to_excel(writer,'Orders2')
    writer.save()
    print('Ok')


generar_DF_Excel(df, 'autores sopa de wuhan')