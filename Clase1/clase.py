
int(3.1)
float(2)
string = "dsdasd"
a = False
b = True
clase = {"alumno1": "Nicolas", "alumno2": "Matias"}
clase["alumno1"]
clase2 = ["alumno1", "alumno2"]
clase2[0]
clase2[-1]



dos = "dos"
# Aquí definimos la variables dos como el string "dos"
type(dos)
# la función type nos indica que tipo de dato estamos ocupando




def cual_es_mi_nombre(nombre):
    print(nombre)
# La función cuál es mi nombre toma el argumento *nombre* y luego lo pasa a la función *print*
# que está anidada dentro de cual_es_mi_nombre y le dice a la consola que imprima el argumento nombre
# al pegar la función en la consola python almacenará este dato y luego podremos llamarla cuantas veces lo necitemos.

cual_es_mi_nombre("José Miguel")
# Aquí estamos llamando a la función y pasandole el argumento "José Miguel", por lo que de salir todo bien, 
# la consola debería imprimir "José Miguel"


def suma_de_numeros(numero1, numero2):
    if isinstance(numero1, int) and isinstance(numero2, int):
        print(int(numero1) + int(numero2))
    else:
        print("Los datos no son números enteros")
# Aqui vemos una función más compleja, en ella se usa el condicional if que verifica el cumplimiento de una condición
# además incluímos dentro de nuestra función suma_de_numeros (que toma 2 argumentos), la función  isinstance que permite
# verificar si una variable es cierto tipo de dato. En particular esta función suma los números e imprime el resultado en
# en la consola, pero solo si estos son enteros, si no son enteros la función imprimirá el mensaje:
#  "Los datos no son números enteros"


suma_de_numeros(dos, int(5))
# Probaremos nuestra funcion con una variable de tipo str y un número entero

isinstance(5.03, int)
# Aquí probaremos como funciona la función isinstance que verifica si la variable pertenece a cierta categoria de datos, arrojando
# Lo que se conoce como un dato booleano True o False.

