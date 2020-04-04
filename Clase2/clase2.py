#funciones predefinidas: int, str, float, lst, dict
dos = "dos"
tres = 3
type(tres)
tres = str(tres)
type(tres)

def division(valor1, valor2):
    return valor1 / valor2

division(6, 4)

division(6.25, 7)

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

#atributos: .split()

vladimir = "Vladimir Painequeo"

valentin = vladimir.replace("Vladimir", "Valentín")

lista_valentin = valentin.split(" ")

apellido_valentin = valentin.split(" ")[1]

nombre_valentin = valentin.split(" ")[0]


#listas

vegetales = ["apio", "lechuga", "palta"]

apio = vegetales[0]

vegetales.append("tomate")
vegetales.remove("apio")

print(vegetales)

print(vegetales.random())

perecibles = []

#loop for

#Loop while



#Diccionarios

#librerías
#time.sleep() datetime()



