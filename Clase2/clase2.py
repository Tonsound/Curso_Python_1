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

# Atributos: los atributos son características de nuestros elementos que viene prediseñadas e incluídas dentro de funciones de python o librerías que importamos.
# Podemos utilizarlas a nuestro gusto, y se escriben con un punto y el atributo, como en los siguientes ejemplos:
# str("some_string").replace("some", "replaced"): en una string reemplaza un una parte específica de esta string por otra
# str("some_string").split("_"): divide una string en base al argumento entregado, en este caso nos entregará la lista ["some", "string"]

vladimir = "Vladimir Painequeo"

valentin = vladimir.replace("Vladimir", "Valentín")

cinco = 5
cinco.replace("Vladimir", "Valentín")

lista_valentin = valentin.split(" ")

apellido_valentin = valentin.split(" ")[1]

nombre_valentin = valentin.split(" ")[0]

lista_valentin[0]

# LISTAS

# Las listas son conjuntos de datos ordenados separados por una coma y encerrados en [].
# Son un objeto iterable por lo que podemos movernos elemento por elemento. Ojo que parte desde el elemento 0.
# se pueden tener tambien listas anidadas en listas:
# Ej.
# comida = [["apio", "lechuga", "palta"], ["arroz", "pan", "papas"]]
# Podemos acceder a un elemento de una lista señalando su posición entre brackets:
# Ej.
# comida[0] = ["apio", "lechuga", "palta"], comida[0][2] = "palta"

vegetales = ["apio", "lechuga", "palta"]

apio = vegetales[0]

vegetales.append("tomate")
vegetales.remove("apio")

print(vegetales)


carbohidratos = ["arroz", "pan", "papas"]

# LIBRERÍAS

# Es un conjunto de elementos (funciones, clases, tipos predefinidos, constantes, variables globales, macros, etc) que es posible utilizar en un programa para facilitar la implementación de ese programa.
# Las puedes implementar en tu programa con la string import, tambien podemos cambiar el nombre con el que la vamos ocupar con la string "as " + el nombre que queremos usar:
# Ej.
# import pandas as pd  --> ahora podemos usar pandas como pd, pd.DataFrame(), si importamos asi: import pandas  --> debemos usar el nombre completo para usar funciones de pandas: pandas.DataFrame()

import random

print(random.choice(vegetales))


help(random)

def Sugerencia_comida(carbohidratos, vegetales):
    print(random.choice(carbohidratos) + " con " + random.choice(vegetales))


#LOOP FOR:

# Nos permite iterar sobre una secuencia. Por cada iteración podemos ejecutar un código, podemos anidar cuantos loops queramos,
# pero en general existen otras fórmulas mejores para hacer iteraciones sobre iteraciones.

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



