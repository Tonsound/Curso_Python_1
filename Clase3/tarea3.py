#Ejercicio1
#Escriba funcion que meta los valores del 0 al 100 en una lista.
def lista():
    valores = []
    for i in range(100):
        valores.append(i)
    return valores

lista = lista()
#Ejercicio2
#Escriba una función que tome una lista de números y devuelva la suma acumulada, es decir, una nueva lista donde el primer elemento es el mismo, el segundo elemento es la suma del primero con el segundo, el tercer elemento es la suma del resultado anterior con el siguiente elemento y así sucesivamente. Por ejemplo, la suma acumulada de [1,2,3] es [1, 3, 6].
def suma_lista(lista):
    nueva_lista = []
    for i in range(len(lista)):
        if i == 0:
            nueva_lista.append(lista[i])
        else:
            nueva_lista.append(lista[i] + nueva_lista[i-1])
        print(nueva_lista)
        print(lista)
    return nueva_lista

lista2 = suma_lista(lista)

#Ejercicio3
#Escribe una función "ordenada" que tome una lista como parámetro y devuelva True si la lista está ordenada en orden ascendente y devuelva False en caso contrario.
#Por ejemplo, ordenada([1, 2, 3]) retorna True y ordenada([b, a]) retorna False.
def lista_ordenada(lista):
    count = 0
    for i in range(1, len(lista)):
        if lista[i] >= lista[i-1]:
            pass
        else:
            count += 1
    if count >= 1:
        print("Lista no ordenada")
    else:
        print("Lista Ordenada")


#Ejercicio4
#Escribe una función llamada "elimina_duplicados" que tome una lista y devuelva una nueva lista con los elementos únicos de la lista original. No tienen porque estar en el mismo orden.
def elimina_duplicados(lista):
    lista2 = []
    for i in lista:
        if lista[i] not in lista2:
            lista2.append(lista[i])
        else:
            pass


#Ejercicio5
# Cree un contador dentro de su función que estime la cantidad de número pares que hay dentro de su sucesion de fibonacci,
# para esto puede usar una comparación entre el número // 2 y el número / 2, solo en caso de los pares, esto debería ser verdad
# además se recomienda definir la variable count = 0 antes del loop

def fibonacci(rango):
    numeros = []
    count = 0
    for i in range(rango):
        if i == 0:
            a = 0
            numeros.append(a)
        elif i <= 1:
            a = numeros[i-1] + i
            numeros.append(a)
        else:
            a = numeros[i-1] + numeros[i-2]
            numeros.append(a)
        if a // 2 == a /2:
            count += 1
        print(a)
    print("hay " + str(count) + " numeros pares")

fibonacci(10)
    