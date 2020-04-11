#Diccionarios
persona1 = {"edad":10, "nombre": "Marcos"}
persona2 = {"edad":12 ,"nombre": "Jaime"}


#If  == , !=, >, <
def quien_es_mayor(var1, var2):
    if var1["edad"] > var2["edad"]:
        print(var1["nombre"] + " es mayor")
    else:
        print(var2["nombre"] + " es mayor")


 def quien_es_mayor2(var1, var2):
    if var1["edad"] > var2["edad"]:
        print(var1["nombre"] + " es mayor")
    elif var1["edad"] < var2["edad"]:
        print(var2["nombre"] + " es mayor")
    elif var1["edad"] == var2["edad"]:
        print("Ambas personas tienen la misma edad")
    else:
        pass

persona1.update({"Poder": 5})
persona2.update({"Poder": 7})


#Loop while
import time
import random

def Torneo_de_pelea(var1, var2):
    peleas = 0
    while peleas <= 10:
        if var1["Poder"] > var2["Poder"]:
            print(var1["nombre"] + " le sacó la ctm a " + var2["nombre"])
            var2["Poder"] += random.randint(0,2)
            peleas += 1
        elif var2["Poder"] > var1["Poder"]:
            print(var2["nombre"] + " le sacó la ctm a " + var1["nombre"])
            var1["Poder"] += random.randint(0,3)
            peleas += 1
        else:
            print("Empataron y se fueron a entrenar")
            var1["Poder"] += random.randint(0,3)
            var2["Poder"] += random.randint(0,2)
            peleas += 1

Torneo_de_pelea(persona1, persona2)
#time.sleep() datetime()
import time

def Torneo_de_pelea(var1, var2):
    peleas = 0
    while peleas <= 10:
        if var1["Poder"] > var2["Poder"]:
            print(var1["nombre"] + " le sacó la ctm a " + var2["nombre"])
            var2["Poder"] += random.randint(0,2)
            peleas += 1
            time.sleep(3)
        elif var2["Poder"] > var1["Poder"]:
            print(var2["nombre"] + " le sacó la ctm a " + var1["nombre"])
            var1["Poder"] += random.randint(0,3)
            peleas += 1
            time.sleep(3)
        else:
            print("Empataron y se fueron a entrenar")
            var1["Poder"] += random.randint(0,3)
            var2["Poder"] += random.randint(0,2)
            peleas += 1
            time.sleep(3)

# list comprehension

digitos = [i for i in range(10)]
exponencial2 = [2**i for i in range(10)]
exponencial2_2 = [2**i for i in range(1, 10)]


# pandas
# cd ..
# cd <folder>
# ls
# columna Index

import pandas as pd
from pandas import ExcelWriter

xl = pd.ExcelFile("Notorious_ordenes.xls")
xl.sheet_names
df = xl.parse("Orders")

print(df)
print(df.head())
print(df.columns)

df.iloc[2, 5]

df.loc[2, 'Producto']

df['Estado interno']

def tipos_de_estado(df):
    estados_internos = []
    for i in range(len(df)):
        if df.loc[i, 'Estado interno'] not in estados_internos:
            estados_internos.append(df.loc[i, 'Estado interno'])
        else:
            pass
    return estados_internos

tipos_de_estado = tipos_de_estado(df)

df['Estado interno'].values

df2 = df[df['Estado interno'] == 'problemas']



def generar_DF_Excel(df, nombre_archivo):
    nombre_final = nombre_archivo + '.xlsx' 
    writer = ExcelWriter(nombre_final)
    df.to_excel(writer,'Orders')
    writer.save()
    print('Ok')


generar_DF_Excel(df2, 'ordenes_problemas')












