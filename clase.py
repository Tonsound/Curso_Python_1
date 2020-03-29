
def cual_es_mi_nombre(nombre):
    print(nombre)


cual_es_mi_nombre("José Miguel")

def suma_de_numeros(numero1, numero2):
    if isinstance(numero1, int) and isinstance(numero2, int):
        print(int(numero1) + int(numero2))
    else:
        print("No son los datos datos numéricos compadre")

dos = "dos"

suma_de_numeros(dos, int(5))

isinstance(5.03, int)