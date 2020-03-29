
# La función cuál es mi nombre toma el argumento *nombre* y luego lo pasa a la función *print*
# que está anidada dentro de cual_es_mi_nombre y le dice a la consola que imprima el argumento nombre
# al pegar la función en la consola python almacenará este dato y luego podremos llamarla cuantas veces lo necitemos.
def cual_es_mi_nombre(nombre):
    print(nombre)

# Aquí estamos llamando a la función y pasandole el argumento "José Miguel", por lo que de salir todo bien, 
# la consola debería imprimir "José Miguel"
cual_es_mi_nombre("José Miguel")


# Aqui vemos una función más compleja, en ella se usa el condicional if que verifica el cumplimiento de una condición
# además incluímos dentro de nuestra función suma_de_numeros (que toma 2 argumentos), la función  isinstance que permite
# verificar si una variable es cierto tipo de dato. En particular esta función suma los números e imprime el resultado en
# en la consola, pero solo si estos son enteros, si no son enteros la función imprimirá el mensaje:
#  "Los datos no son números enteros"
def suma_de_numeros(numero1, numero2):
    if isinstance(numero1, int) and isinstance(numero2, int):
        print(int(numero1) + int(numero2))
    else:
        print("Los datos no son números enteros")

# aqui definimos la variables dos como el string "dos"
dos = "dos"

# Probaremos nuestra funcion con una variable de tipo str y un número entero
suma_de_numeros(dos, int(5))

# Aquí probaremos como funciona la función isinstance que verifica si la variable pertenece a cierta categoria de datos, arrojando
# Lo que se conoce como un dato booleano True o False.
isinstance(5.03, int)