# Curso Python Básico

A continuación se deja un glosario de los términos que estaremos viendo durante las clases, un instructivo de instalación de los software que vamos a ocupar y dentro de los directorios pueden encontrar el código de las clases con información relevante.

## Glorario

- **Directorio:** también se los denomina **carpetas de archivos**,  es un contenedor virtual en el que se almacenan una agrupación de archivos informáticos y otros subdirectorios, atendiendo a su contenido, a su propósito o a cualquier criterio que decida el usuario. Técnicamente, el directorio almacena información acerca de los archivos que contiene: como los atributos de los archivos o dónde se encuentran físicamente en el dispositivo de almacenamiento.

- **Software:**  soporte lógico de un sistema informático, que comprende el conjunto de los componentes lógicos necesarios que hacen posible la realización de tareas específicas, en contraposición a los componentes físicos que son llamados hardware. La interacción entre el software y el hardware hace operativo un ordenador (u otro dispositivo), es decir, el Software envía instrucciones que el Hardware ejecuta, haciendo posible su funcionamiento.

- **Python:** es un **lenguaje de programación interpretado** cuya filosofía hace hincapié en la legibilidad de su código.​ Se trata de un lenguaje de programación **multiparadigma**, ya que soporta orientación a objetos, programación imperativa y, en menor medida, programación funcional. Es un lenguaje interpretado, dinámico y multiplataforma.

- **Terminal:**  o **consola** es una interfaz que nos permite hacer solicitudes a nuestro **PC** a través de código.

- **Editor de código o IDE:** Un **entorno de desarrollo integrado**​ o entorno de desarrollo interactivo, en inglés **Integrated Development Environment (IDE)**, es una aplicación informática que proporciona servicios integrales para facilitarle al desarrollador o programador el desarrollo de software.
Normalmente, un IDE consiste de un **editor de código fuente**, herramientas de construcción automáticas y un depurador.
Un **editor de código fuente** es un editor de texto diseñado específicamente para editar el código fuente de programas informáticos. Puede ser una aplicación individual o estar incluido en un entorno de desarrollo integrado.

- **Función:** Una función es un bloque de código con un nombre asociado, que recibe cero o más argumentos como entrada, sigue una secuencia de sentencias, la cuales ejecuta una operación deseada y devuelve un valor y/o realiza una tarea, este bloque puede ser llamados cuando se necesite.

- **Librería:** es un conjunto de elementos (funciones, clases, tipos predefinidos, constantes, variables globales, macros, etc) que es posible utilizar en un programa para facilitar la implementación de ese programa.

- **Framework:** es un conjunto integrado de herramientas que facilitan un desarrollo software. Puede incluir APIs y bibliotecas. Pero también puede incluir otros elementos como herramientas de depuración, diseño gráfico, prototipado, edición, etc.

- **Tipos de Datos en python:** 
- *Strings:* es una secuencia de caracteres utilizado para guardar y representar textos. 
- *Números enteros:* se referencia a estos como int(). Ejs: 1, 2, 5, 17
- *Números de punto flotante:* se referencia a estos como float() . Ejs: 1.0, 2.5, 3.14156
- *Números complejos:* se especifica la parte imaginaria con la letra j o J. Ejs: 0j, 0.j, 0.0j, .0j
- *Tuplas:* Una tupla es una secuencia de items ordenada e inmutable, Los items de una tupla pueden ser objetos de cualquier tipo. Ejs: (100, "doscientos", 300)    # Tupla con tres elementos
- *Listas:* Una lista es una secuencia ordenada de elementos mutable. Los items de una lista pueden ser objetos de distintos tipos. Ej: a = [42, 3.14, 'hola', 'casa'], a = list("hola") # En ambos casos la *variable a* es una lista.
- *Diccionarios:* En Python, un diccionario es una colección no-ordenada de valores que son accedidos a traves de una clave. Es decir, en lugar de acceder a la información mediante el índice numérico, como es el caso de las listas y tuplas, es posible acceder a los valores a través de sus claves, que pueden ser de diversos tipo. Ej: alumnos = {1: "Pablo", 2: "Leti", 3: "Andres"}
- *Iterables:* El concepto de Python que generaliza la idea de "secuencia" es el concepto de "iterable".Todas las secuencias son iterables. Ejs: str(), list(), dict(), tuple()



## Instrucciones de Instalación

Para este curso usaremos un paquete llamado **Anaconda** , la *versión de Python* **3.7** que pueden descargar del siguiente link:

> https://www.anaconda.com/distribution/#download-section

Usaremos este paquete que instala junto con **Python 3.7** una seríe de **librerías** que nos harán más fácil el trabajo de programar más adelante.

Una vez descargado el programa instalar y asegurénse de que la opción de que establezca un path en su sistema operativo esté marcada, esto nos permite iniciar **Python** desde cualquier ubicación de nuestro PC. Cuanto termina la instalación el programa nos lleva a una página web, no la tomemos en cuénta (cierrenla), **Python** ya debería estar instalado en nuestro systema.

Listo lo anterior, en este curso trabajaremos con un **IDE** llamado **Visual Studio Code**, pueden ver más información sobre los editores de código en el glosario, lo cierto es que **VSC** es uno de los editores más usados dentro de la comunidad de programadores y esto es debido principalmente a su versatilidad y funcionalidad, siempre es bueno probar distintas tecnologías, por lo que puede que hoy programen con **VSC** y en un futuro usen algún otro **IDE**.
Pueden encontrar los links de descarga aquí:

> https://code.visualstudio.com/Download

Luego de terminada la descarga, deberán instalar el programa y cuando finalice seleccionar todas las opciones que les ofrece **VSC** respecto a su accesibilidad como se señala en la siguiente [imágen](Clase1/vsc.PNG).

Con todo listo procederemos a crear un **directorio** con el nombre que elijamos donde almacenaremos las clases, para cada clase crearemos una carpeta nueva como Clase1, Clase2, etc.. dentro de este directorio.

Con todo organizado, procederemos a abrir **VSC** y en donde dice **Archivo** o **File** (esquina superior izquierda) seleccionaremos **open folder** o **abrir carpeta** y buscaremos el directorio que creamos y seleccionaremos la carpeta de la Clase1.

Por último y para finalizar este tutorial, deben ir al menú superior y seleccionar **Terminal** y luego **New Terminal** *(en Windows podemos conseguir el mismo resultado con ctrl + shift + ñ)*, posteriormente escribir python en la consola y presionar enter, esto debería abrir **Python** en la consola de la parte inferior


