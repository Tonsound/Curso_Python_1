#Diccionarios
persona1 = {"edad":10, "nombre": "Marcos"}
persona2 = {"edad":12 ,"nombre": "Jaime"}

persona3 = persona1.copy()
persona3.update({"nombre": "Andres"})
print(persona3["nombre"] + " y " + persona2["nombre"])

persona1['edad']
persona2['nombre']

personas = [persona1, persona2, persona3]

#If  == , !=, >, <, >=, <=
def quien_es_mayor(personas):
    for i in range(len(personas)):
        if personas[i]['edad'] == max(personas[0]['edad'], personas[1]['edad'], personas[2]['edad']):
            print(personas[i]['nombre']+ " es mayor")

quien_es_mayor(personas)


 def quien_es_mayor2(var1, var2):
    if var1["edad"] > var2["edad"]:
        print(var1["nombre"] + " es mayor")
    elif var1["edad"] < var2["edad"]:
        print(var2["nombre"] + " es mayor")
    elif var1["edad"] == var2["edad"]:
        print("Ambas personas tienen la misma edad")
    else:
        pass


persona1.update({"edad": persona2["edad"]})

persona1.update({"Poder": 5})
persona2.update({"Poder": 7})
persona3['Poder'] = 8


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












