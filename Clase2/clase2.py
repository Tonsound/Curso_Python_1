#funciones predefinidas: int, str, float, lst, dict
dos = "dos"
tres = 3

type(tres)

tres = str(tres)
type(tres)

def division(valor1, valor2):
    return valor1 // valor2

division(6, 4)

division(6.25, 7)
valor1 = "valor1"
valor2 = "valor2"

division(valor1, valor2)

def division2(valor1, valor2):
    try:
        resultado = valor1 / valor2
    except:
        resultado = "No se pueden dividir"
    return resultado


division2(6, dos)

division2(6, tres)

division2(6, int(tres))

#atributos: .split() .remove() los atributos son características de nuestros elementos que viene prediseñadas
#  y que podemos utilizar a nuestro gusto, .replace() en una string reemplaza un una parte específica de esta string por otra
# .split() divide una string en base al argumento entregado

vladimir = "Vladimir Painequeo"

valentin = vladimir.replace("Vladimir", "Valentín")

cinco = 5
cinco.replace("Vladimir", "Valentín")

lista_valentin = valentin.split(" ")

apellido_valentin = valentin.split(" ")[1]

nombre_valentin = valentin.split(" ")[0]

lista_valentin[0]

#listas
# Las listas son conjuntos de datos ordenados separados por una coma y encerrados en [], 
# son un objeto iterable por lo que podemos movernos elemento por elemento. Ojo que parte desde el item 0
# se pueden tener tambien listas de listas
# Ej.
# comida = [["apio", "lechuga", "palta"], ["arroz", "pan", "papas"]]
# podemos acceder a un elemento de una lista señalando su posición entre brackets,
# Ej.
# comida[0] = ["apio", "lechuga", "palta"], comida[0][2] = "palta"

vegetales = ["apio", "lechuga", "palta"]

apio = vegetales[0]

vegetales.append("tomate")
vegetales.remove("apio")

print(vegetales)


carbohidratos = ["arroz", "pan", "papas"]

#librerías
#es un conjunto de elementos (funciones, clases, tipos predefinidos, constantes, variables globales, macros, etc) que es posible utilizar en un programa para facilitar la implementación de ese programa.
# las llamamos con la string import y podemos cambiarle el nombre con el que la vamos ocupar con la string "as " + el nombre que queremos usar:
# Ej.
# import pandas as pd  --> ahora podemos usar pandas como pd, pd.DataFrame(), si importamos asi: importa pandas  --> debemos usar el nombre completo pandas.DataFrame()
import random

print(random.choice(vegetales))


help(random)

def Sugerencia_comida(carbohidratos, vegetales):
    print(random.choice(carbohidratos) + " con " + random.choice(vegetales))


#loop for
# nos permite iterar sobre una secuencia. Por cada iteración podemos ejecutar un código, podemos anidar cuantos loops queramos,
# pero en general existen otras fórmulas mejores para hacer iteraciones sobre iteraciones

def todos_los_carbohidratos(carbohidratos):
    elementos = []
    for element in carbohidratos:
        elementos.append(element)
    return elementos

carb = todos_los_carbohidratos(carbohidratos)

def menus_posibles(carbohidratos, vegetales):
    for a in carbohidratos:
        for b in vegetales:
            print(a + " con " + b)   

for i in range(len(carbohidratos)):
    print(carbohidratos[i])



