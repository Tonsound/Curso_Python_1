#Cree una función que tome 3 datos y retorne una lista con esos datos
def listaDatos(x1, x2, x3):
    lista = [x1, x2, x3]
    return lista


miLista = listaDatos("matias", "jose", "nico")
# Cree una función que tome como argumentos una lista y otro valor, agregue el valor a la lista y retorne la nueva lista
def nuevaLista(x1, x2):
    x1.append(x2)
    return x1

listaAlargada = nuevaLista(miLista, "Fernando")
# Cree una funcion que tome dos listas y devuelva una sola lista con todos los elementos de ambas listas
def extensionListas(x1, x2):
    x1.extend(x2)
    return x1

listaLarga = extensionListas(listaAlargada, miLista)

