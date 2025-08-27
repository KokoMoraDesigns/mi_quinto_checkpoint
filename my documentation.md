
# Breve glosario de Python

## Argumento

En Python, un argumento es la indicación que le das a una función determinada sobre cuál es la salida que deseas lograr; el parámetro, por otro lado, es el nombre que le asignas a dicho argumento al formular la función.

A continuación unos ejemplos según los distintos tipos de argumentos que existen.


#### Argumento posicional

El orden en que se incluyen los argumentos al declarar la función **debe ser el mismo** orden que utilizaste al formular los parámetros de la función. 


    
    **definir la función:**
    
    def sum(a,b,c): --> a, b y c siendo los *parámetros* de la función
	    return a+b+c


	**llamar la función:**

	sum(4,8,9) --> 4, 8 y 9 siendo los *argumentos* de la función




#### Argumento de palabra clave

El orden en que se incluyen los argumentos al declarar la función **no es relevante**, dado que vamos a puntualizar en la declaración a qué parámetro  estamos haciendo referencia.

    def sum(a,b,c):
    
	    return a+b+c
    
    sum(a=4,c=9,b=8)
    


Existe la posibilidad de combinar en una llamada a la función argumentos posicionales y de palabras clave, en cuyo caso, **los argumentos posicionales deben ir al principio** de la declaración --> sum(a=4,8,9) : *SyntaxError: invalid syntax* 

    def sum(a,b,c):
    
	    return a+b+c
	    
    sum (4,c=9,b=8)
    

#### Argumento predeterminado

El argumento **se declara al definir la función**, por eso más adelante no es necesario incluir dicho argumento en la llamada de la función (si en la llamada incluyeras otro valor para ese argumento, estarías sobreescribiendo el que declaraste al principio.

    def sum(a,b=8,c=9):
    
	    return a+b+c
    
    sum(4,b,c) --> salida = 4 + 8 + 9 = 21

   Los argumentos predeterminados **deben ir a continuación de los no predeterminados** --> def sum(a=5,b,c) : *SyntaxError: parameter without a default follows parameter with a default*




#### Argumento arbitrario o de longitud variable

Los utilizas en funciones con argumentos variables, cuando no conoces de antemano el número exacto de argumentos que vas a incluir en la función. 



***args** hace referencia a argumentos posicionales (incluyes un asterisco antes del parámetro variables), y ****kwargs** a argumentos de palabra clave (incluyes dos asteriscos antes del parámetro variable).

    def sum(a,*b):
    
	    return a+b
	    
	sum(4,8,9) --> salida = 4 + 8 + 9 = 21
	
	(en dicha salida 'a' equivale a 4, 'b' equivale a 8 y a 9)


Un argumento variable **puede ir precedido por otros argumentos no variables.**

 

> **MEJORES PRÁCTICAS:**
> Restringir desde la definición de la función con qué tipos de argumentos se está trabajando, de modo que solo sea necesario mirar la función para comprender el funcionamiento de sus argumentos.
> 
>  Es aconsejable hacer uso de argumentos **obligatoriamente posicionales** cuando deseas imponer un orden al llamar a los argumentos de la función, y de argumentos **obligatoriamente de palabras clave** cuando los nombres de los parámetros sean significativos y apoyen a la correcta comprensión de la función (por ejemplo: *def name(first,last):* .

**Trabajando con argumentos obligatoriamente posicionales**

Separas mediante '/' los parámetros obligatoriamente posicionales (que *quedan a la izquierda del signo*) del resto, que podrán ser tanto posicionales como de palabra clave.


    def sum(a,b,/,c,d):
    
	    return a+b+c+d
	    
	    
	sum(4,8,9,5) --> salida: 26 --> correcto
	
	sum(4,8,d=5,c=9) --> salida: 26 --> correcto
	
	sum(b=8,a=4,c=8,d=9) --> salida: TypeError: sum() got some positional-only arguments passed as keyword arguments: 'a, b'


**Trabajando con argumentos obligatoriamente de palabras clave**

Separas mediante un asterisco los parámetros obligatoriamente de palabras clave (que *quedan a la derecha del signo*) del resto, que podrán ser tanto posicionales como de palabra clave.

    def sum(a,b,*,c,d):
    
	    return a+b+c+d
	    
	    
	sum(4,8,c=9,d=5) --> salida: 26 --> correcto
	
	sum(b=8,a=4,d=5,c=9) --> salida: 26 --> correcto
	
	sum(4,8,8,d=5) --> salida: TypeError: sum() takes 2 positional arguments but 3 positional arguments (and 1 keyword-only argument) were given


**Trabajando con argumentos obligatoriamente posicionales y obligatoriamente de palabras clave**

    def sum(a,b,/,c,*,d):
    
	    return a+b+c+d
	    
	sum(4,8,9,d=5) --> salida: 26 --> 'a' y 'b' son argumentos obligatoriamente posicionales, 'c' posicional o de palabra clave, y 'd' obligatoriamente de palabra clave.






## Bucle

Los bucles se utilizan para el código reiterativo, existiendo dos tipos principales de bucles: *for* y *while*. 

### Bucle *for*



**Itera sobre una secuencia**  (lista, tupla, cadena....) **de la que tienes conocimiento previo**, con lo que ya sabes el número de veces en que se va a repetir el código; por ejemplo, si deseas imprimir el contenido de una colección o efectuar cálculos con los números contenidos en un rango ya determinado, se repetirá el código tantas veces como elementos tengas en la colección que hayas colocado a la derecha de la cláusula *(el operador)* 'in'.

    mis_libros = ['amarilla', 'biciosas', 'la isla de las medusas', 'pirómanas', 'brillando']
    
    for libro in mis_libros:
    
	    print(libro) 
	    
	    
	salida: amarilla
			biciosas
			la isla de las medusas
			pirómanas
			brillando



Cada vez que se ha ejecutado el código, la variable 'libro' ha contenido en su interior un elemento diferente.


Estructura del bucle *for*:
   
    for 'variable' in 'iterable':

	    'bloque de código a ejecutar'



### Bucle *while*
**Ejecuta un bloque de código** siempre y **cuando su factor condicionante se mantenga verdadero**; por ejemplo, deseas que el código se repita hasta que la persona usuaria inserte el valor correcto o que determinada operación se repita hasta que se cumpla, o deje de cumplirse, determinada condición.

    horchata = 7 
    
    while horchata > 1:
    
	    horchata -=1
	    print(horchata)
	    
	    
	salida: 6
			5
			4
			3
			2
			1
			

Estructura del bucle *while*:
   
    while 'condición':

	    'bloque de código a ejecutar'


También puedes incluir la cláusula *else*, que entrará en acción una vez el bucle haya terminado, es decir, una vez la condición haya cesado de ser cierta:

    horchata = 7 
    
    while horchata > 1:
    
	    horchata -=1
	    print(f'nos quedan {horchata} horchatas')
	    
	else:
	    print('deberíamos comprar más horchata')
	    
	salida: nos quedan 6 horchatas
			nos quedan 5 horchatas
			nos quedan 4 horchatas
			nos quedan 3 horchatas
			nos quedan 2 horchatas
			nos quedan 1 horchatas
			deberíamos comprar más horchata

> Si no defines la cláusula *while*, crearás **un bucle infinito**, dado que no existirá un momento en que la declaración sea falsa.

Estructura del bucle *while/else*:
   
    while 'condición':

	    'bloque de código a ejecutar'
	    
	else:
	
		'nuevo código a ejecutar'

En la operación del bucle *while* y *while/else*, tras cada iteración volvía a analizarse si 'horchata' seguía siendo mayor que 1, para decidir si volver a ejecutar el código o no; en la operación del bucle *for*, el iterable era el que decidía el número de veces en que se ejecutaría el código.

    for i in 'perros':
    
	    print(i)


	salida: p
			e
			r
			r
			o
			s

En la operación anterior, 'perros' equivale al **iterable**, es decir, al objeto que va a ser iterado *(e indexado, es decir, que podrás acceder al mismo mediante un índice)* en la operación.  En un bucle *for*, lo que coloques después de 'in' equivaldrá al iterable.

#### Bucles anidados

Si estás trabajando con un objeto iteradle que, en su interior, contiene otro objeto iterable, puedes crear un bucle *for* anidado. Por ejemplo:

    mi_cine = [['us', 'oddity', 'seven veils', 'heretic', 'the shining'], ['bottoms', 'bullet train', 'the blackening', 'heathers']]
    
    
    for genero in mi_cine:
    
    	print(genero)
    	

    salida: ['us', 'oddity', 'seven veils', 'heretic', 'the shining']
		    ['bottoms', 'bullet train', 'the blackening', 'heathers']


Con el bucle *for* simple del ejemplo *mi_cine* estamos accediendo únicamente al objeto iterable exterior; no obstante, si ahora anidamos un segundo bucle *for* podremos acceder también a los elementos internos, ya que el primer *for* iterará sobre la primera lista, y el segundo *for* sobre la lista anidada a la primera:

    for genero in mi_cine:
    
	    for filme in genero:
	    
		    print(filme)
		    

	salida: us
			oddity
			seven veils
			heretic
			the shining
			bottoms
			bullet train
			the blackening
			heathers




#### Bucles según su índice

También puedes iterar una cadena **en sentido inverso**:

    color_ojos ='marrón'
    
    for i in color_ojos[::-1]:
	    print(i)
    
    
    salida: n
		    ó
		    r
		    r
		    a
		    m


También puedes iterar una cadena **saltando elementos**:

    color_ojos ='marrón'
    
    for i in color_ojos[::2]:
    
	    print(i)
	    
	    
	salida: m
			r
			ó

#### Bucles con operaciones

    multiplos = []
    
    for num in [3, 6, 9]:
    
	    multiplos.append(num*3)
	    
	    
	multiplos = [9, 18, 27]

---------
    cuadrados = []
    
    for num in range(8):
    
	    cuadrados.append(num**2)
	    

	cuadrados = [0, 1, 4, 9, 16, 25, 36, 49]

#### Bucle con orden *break*

La orden *break* interrumpirá el bucle de inmediato y, en caso de existir, pasará a ejecutar la siguiente línea del código:

  
    
	for num in range(8):
    
		cuadrados = num**2
		
		if cuadrados == 16:
			print(f'el número que buscamos es {num}')
			break
			
	


#### Bucle con orden *continue*		  
 
 En lugar de interrumpir la ejecución del código, la orden *continue* lo que hará será saltarse el código que vaya después de la orden y volver al comienzo, analizando la condición para el resto de valores que le queden.
 

    peliculas_por_ver = ['us', 'oddity', 'seven veils', 'heretic', 'the shining']
    
    for opcion in peliculas_por_ver:
	    if opcion == 'oddity':
		    continue
	    print(opcion)

	

    
## Condicional

Una condicional permite que se ejecuten bloques de código diferentes en dependencia de si una condición determinada resulta ser verdadera o resulta ser falsa, esto le da independencia al programa para tomar decisiones *(de hecho, a la sentencia condiciónal también se puede llamar sentencia de decisión)* según el contexto en que se encuentre. 

La indentación es extremadamente importante para definir el alcance de cada sentencia condicional.

### Sentencia condicional *if*

Si la condición es verdadera, ejecutará el siguiente bloque de código, si la condición es falsa, no la ejecutará. Puede haber una condición, o múltiples condiciones.

    personas_invitadas = ['persona_uno', 'persona_dos', 'persona_tres', 'persona_cuatro', 'persona_cinco', 'persona_seis', 'persona_siete']
 
    personas_aceptaron = ['persona_uno', 'persona_cuatro', 'persona_cinco', 'persona_seis']

	personas_vacunadas = ['persona_uno', 'persona_dos', 'persona_cuatro', 'persona_cinco', 'persona_siete']
    
    enviar_billetes = []    


    for persona in personas_invitadas:
    
	    if persona in personas_aceptaron and persona in personas_vacunadas:
	    
		    print(f'{persona} viene al viaje sin duda alguna')
		    enviar_billetes.append(persona)
		    
	print(enviar_billetes)
		    
	

El código indentado después de *if* forma parte del condicional, mientras que el resto ( *print(enviar_billetes* ) se reproducirá tanto si se cumple la condición como si no se cumple. Además, en este ejemplo no solamente tenemos un condicional, sino que tenemos dos, y ambos deberán ser verdaderos para que el código condicional en su conjunto resulte verdadero y se ejecute.


### Sentencia condicional if-else

Si la condición es verdadera, ejecutará el primer bloque de código y no leerá más, si la condición es falsa, seguirá leyendo y ejecutará el otro bloque de código (el que sigue a *else*). 


    if edad >= 18:
    
    	print('puedes beber alcohol delante de la policía')
    	
    else:
    
	    print('es aconsejable que la policía no te vea bebiendo alcohol')
	    
	    
	 edad = 25 (es decir, la condicion 'if' es verdadera) --> salida: puedes beber alcohol delante de la policía 
	 
	 edad = 17 (es decir, la condicion 'if' es falsa) --> salida: es aconsejable que la policía no te vea bebiendo alcohol



### Sentencia condicional anidada
	    
Una sentencia condicional puede contener en su interior otro bloque con otra sentencia condicional. 

    frances = 9.5
    ingles = 9.7
    japones = 9.8
    guarani= 9.9
    
    idiomas = (frances + ingles + japones + guarani) / 4
    
    
    if idiomas >=8:
	    print(f'tienes una media de {idiomas} en idiomas, ¡se te da increíble! ¿Has considerado las profesiones que demandan un alto conocimiento de idiomas?')
	    
	else:
	
		if idiomas >=5:
		
			print(f'tienes una media de {idiomas} en idiomas, estás almacenando mucho conocimiento para viajar por el mundo')
			
		else:
			print(f'tienes una media de {idiomas} en idiomas, ¿crees que necesitas refuerzo o prefieres investigar qué otras áreas puedes estudiar?')


> **MEJORES PRÁCTICAS:**
> 
> Si bien existe la posibilidad de utilizar un número ilimitado de anidaciones, con cada una de ellas el código será más difícil de leer e interpretar, con lo que resulta recomendable usarlas únicamente cuando vayan a optimizar el funcionamiento y la lectura del código.
   
   

### Sentencia condicional no binaria

Similar a *if*-*else*, solo que en lugar de una sola, examina múltiples condiciones: si la sentencia *if* es falsa, sigue leyendo de una en una el resto de sentencias *elif* (*else if*) que hayas introducido hasta encontrar la verdadera y ejecutar su código, y si todas las condiciones resultan ser falsas, ejecuta el código que se encuentre después de la sentencia *else*. 


    seres_queridos = ['persona_uno', 'persona_dos', 'persona_tres']

    personas_desgraciadamente_conocidas = ['persona_siete', 'persona_ocho']

	mandar_mensaje = 'persona_cuatro'
    
    
    if mandar_mensaje in seres_queridos:
	    print('te quiero, me haría muy feliz hacer un viaje contigo')
	    
	elif mandar_mensaje in personas_desgraciadamente_conocidas:
		print('me haría muy feliz no tener que volver a intercambiar una palabra contigo :)')
		
	else:
		print('todavía no nos conocemos, pero me haría muy feliz charlar contigo para descubrir si conectamos')

    
### Operador ternario

Resume el código en una sola línea, que se divide en tres partes diferentes: 

 1. El código que queremos ejecutar si la condición es verdadera.
 2. La condición que estamos evaluando.
 4. El código que queremos ejecutar si la condición es falsa.
        
        zona_horaria = 'dia'
        
        print('buenos días' if zona_horaria == 'dia' else 'buenas noches')



## Función Lambda ( o función anónima)

Sirven para declarar de una manera rápida y sencilla funciones cortas que no necesitan poseer un nombre ( de ahí su consideración de 'anónimas'). Se caracterizan por tener una sola expresión, aunque sí pueden componerse por más de un argumento.

Estructura de una función Lambda:

    *lambda argumentos: expresión* --> palabra clave 'lambda', 
								       espacio, 
								       argumentos separados por comas, 
								       el signo ':',
								       la expresión
								    
Por ejemplo:

    FUNCIÓN TRADICIONAL:			FUNCIÓN LAMBDA:
    
    def sum(num1,num2):				sum = lambda num1,num2: num1+num2
    
	    return num1+num2
	    
	    
						sum(4,7) --> 11


En el ejemplo previo, la función Lambda está asignada a la variable 'sum', porque, al ser una función que carece de nombre, no resulta útil si no le asignas una variable o la integras en otro cometido mayor.

Por ejemplo:

    mezcla = ['4', '8', 'ma', '10', 'love','12','life', '14']
    
    nums = filter(lambda num: num.isdigit(), mezcla)
    
    nums_solo = list(nums)
    
 
Los tipos de argumentos de las funciones tradicionales también se aplican con las funciones anónimas:

    sum = lambda num1,num2=4: num1+num2
    
    sum(2) --> salida: 6
    
También las puedes utilizar dentro de una función tradicional:

    def porcentaje (p):
    
	    return lambda num: num * p / 100
	    
	    
	veinte_porcentaje = porcentaje(20)
	cuarenta_porcentaje = porcentaje(40)
	
	cuarenta_porcentaje(400) --> salida --> 160




> **MEJORES PRÁCTICAS**
> Son ideales para las ocasiones en que necesitas una función simple que solo vas a utilizar una vez, de esta manera, el código queda más ordenado.




## Comprensión de lista

Sirve para, con una sola línea de código, iterar un elemento y crear una nueva lista que, o bien almacene el nuevo contenido que has generado, o bien almacene el contenido de la lista principal que 'haya pasado la prueba' de la(s) condicion(es) que le hayas impuesto. Es decir:


Estructura de la comprensión de lista:

    nueva_lista = código a ejecutar for variable in iterable

Por ejemplo:

    multiplos_cinco = [num*5 for num in range(1,7)]
    
    multiplos_cinco = [5, 10, 15, 20, 25, 30]

Dentro de la comprensión de lista, también podemos llamar a una función: 


    def porcentaje (p):
        
    	    return lambda num: num * p / 100
    	    
    	    
    	cuarenta_porcentaje = porcentaje(40)
    	
    	

    precio_iphones = [1219, 959, 709, 859]
    
    mi_precio_iphones = [cuarenta_porcentaje(precio) for precio in precio_iphones]
    
    mi_precio_iphones = [487.6, 383.6, 283.6, 343.6]



Estructura de la comprensión de lista con condiciones:

    nueva_lista = código a ejecutar for variable in iterable if condicion(es)

En la nueva lista solo se almacenará el contenido que cumpla la(s) condicion(es). Por ejemplo:

    invitadas = [('persona uno', 'aficionada libros'), ('persona dos', 'aficionada musica'), ('persona tres', 'aficionada musica'), ('persona cuatro', 'aficionada libros')]
    
    itinerario_libros = [invitada for invitada in invitadas if invitada[1] == 'aficionada libros']


    itinerario_libros = [('persona uno', 'aficionada libros'), ('persona cuatro', 'aficionada libros')]




> **MEJORES PRÁCTICAS**
> La comprensión de lista es muy útil para colecciones iterables a las que deseamos aplicar modificaciones, pero, dado que en la programación siempre debe primar tanto la optimización como la buena legibilidad del código, en operaciones largas o complejas sería más recomendable prescindir de esta herramienta.

## Paquete pip

Un **gestor de paquetes** es una herramienta que te permite gestionar (instalar, actualizar, desinstalar, consultar, etc.) las bibliotecas o paquetes externos que utilices en tu proyecto de Python, con sus dependencias (las librerías y módulos que el paquete necesita para poder funcionar bien); a su vez, un *paquete* te ofrece funcionalidades extra que no están incluidas en la oferta básica (la Biblioteca Estándar) de Python. 

PIP (Package Installer for Python) o PIP3 es el gestor de paquetes más usado entre las personas usuarios de Python, de hecho, se instala de manera automática al instalar las últimas versiones de Python.

Algunos comandos que pip tproporciona para poder gestionar de manera eficiente nuestras bibliotecas son:

 `pip install <nombre_del_paquete>` --> para instalar un paquete determinado.
 
 `pip install <nombre_del_paquete> >= o == <version_del_paquete>` --> para instalar paquetes a partir de determinada versión, o de determinada versión.
 
`pip freeze > requirements.txt` --> para crear un archivo que le indique a pip los paquetes (y sus versiones) que necesitas para el proyecto en que vas a trabajar (muy útil en el caso de proyectos colaborativos, por ejemplo).

  `pip install -r requirements.txt` -->para instalar los paquetes incluidos en el archivo de requisitos.

`pip install --upgrade <nombre_del_paquete>` --> para actualizar determinado paquete a su última versión.

`pip install -r requirements.txt --upgrade` --> para actualizar a su última versión todos los paquetes incluidos en el archivo de requisitos.

`pip uninstall <nombre_paquete>` --> para eliminar un paquete determinado de tu entorno de Python.

pip list --> para listar los paquetes que tene


    
Para listar todos los paquetes instalados en tu entorno:

`>>pip list`

Para ver un resumen de un paquete de tu interés:

`>>pip show [NameOfPackage]`
> Written by [ Maite Ekhiñe Mora ]
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTk1ODgwMzA3MywtMTk0MjY4MzMzNiwtMj
A1NDAzOTkxLDQzNzgwODI1NSw4MTM3MjgyMiwxNTQ1NDg5MjQy
LDgyMzMwOTc5MCwxNzgwMTMxMzYyLC0xMzczMjg5OTMxLDEyNT
kyMDU1MjQsMjE0NzI2ODc2OSwxNTExNjM1MDU2LC0yMzY2NzIw
OCwtMTkwMzA1OTkzNSwtMTE2MTczMjUyMCwxOTQ3NjEyMTMxLC
00MDgyNDA3MjQsMjUwNTQzNDk4LC0xNDE4MDM3NTYsMjQ4MjA3
MzM4XX0=
-->