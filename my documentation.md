
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
	    
Una sentencia condicional puede contener en su interior otro bloque con una sentencia *if* o *if-else*. 

> **MEJORES PRÁCTICAS:**
> 
> Si bien existe la posibilidad de utilizar un número ilimitado de anidaciones, con cada una de ellas el código será más difícil de leer e interpretar, con lo que resulta recomendable hacer un uso responsable de dichas anidaciones.
   
   

### Sentencia condicional no binaria


    amistades = ['persona_uno', 'persona_dos', 'persona_tres']
    
    personas_desconocidas = ['persona_cuatro', 'persona_cinco', 'persona_seis']
    
    personas_desgraciadamente_conocidas = ['persona_siete', 'persona_ocho']
    
    if amistades:
	    print('me haría muy feliz hacer un viaje contigo en mi cumpleaños')


En este caso necesitarás utilizar una sentencia *if-elif-else*.

 `if-elif-else`:
    
    Permite evaluar múltiples condiciones. Se evalúa la condición en el  `if`. Si es falsa, se evalúa la condición en el  `elif`, y así sucesivamente. Si ninguna condición es verdadera, se ejecuta el bloque de código en el  `else`.


En Python, la sentencia «Elif» se utiliza para comprobar múltiples condiciones si una condición es falsa. Es similar a la sentencia «If-Else», pero la diferencia es que «Elif» evalúa **múltiples condiciones** a diferencia de «Else».

Para probar **varias expresiones**, se puede utilizar una escalera de sentencias Elif. Esto se llama una «Elif ladder” (escalera Elif). El **controlador** comprueba las condiciones de la sentencia if, y si se cumplen, se ejecuta **el conjunto de sentencias de ese bloque**.

En caso contrario, el controlador pasa al **primer bloque Elif** para evaluar las condiciones. El proceso continúa para todas las sentencias Elif, y si determina en la evaluación que todas las condiciones If y Elif se son falsas, se ejecuta el bloque Else.

![](https://db0dce98.rocketcdn.me/es/files/2023/02/if-elfi-else.jpg)


Se puede usar también de manera conjunta todo, el `if` con el `elif` y un `else` al final. Es muy importante notar que `if` y `else` solamente puede haber uno, mientras que `elif` puede haber varios.

x  =  5  if  x  ==  5:  print("Es 5")  elif  x  ==  6:  print("Es 6")  elif  x  ==  7:  print("Es 7")

x  =  5  if  x  ==  5:  print("Es 5")  elif  x  ==  6:  print("Es 6")  elif  x  ==  7:  print("Es 7")  else:  print("Es otro")

### Operador ternario

El operador ternario o `ternary operator` es una herramienta muy potente que muchos lenguajes de programación tienen. En Python es un poco distinto a lo que sería en C, pero el concepto es el mismo. Se trata de una cláusula `if`, `else` que se define en una sola línea y puede ser usado por ejemplo, dentro de un `print()`.

> Ver https://peps.python.org/pep-0308/ 

x  =  5  print("Es 5"  if  x  ==  5  else  "No es 5")  #Es 5

Existen tres partes en un operador ternario, que son exactamente iguales a los que había en un `if``else`. Tenemos la condición a evaluar, el código que se ejecuta si se cumple, y el código que se ejecuta si no se cumple. En este caso, tenemos los tres en la misma línea.


#[código si se cumple] if [condición] else [código si no se cumple]


Operadores de comparación:

Los condicionales utilizan operadores de comparación para evaluar las condiciones:

-   `==`  (igual a)
-   `!=`  (diferente a)
-   `>`  (mayor que)
-   `<`  (menor que)
-   `>=`  (mayor o igual que)
-   `<=`  (menor o igual que)



## Función Lambda

Las expresiones lambda se usan idealmente cuando necesitamos hacer algo simple y estamos más interesados en hacer el trabajo rápidamente en lugar de nombrar formalmente la función. Las expresiones lambda también se conocen como funciones anónimas.

Las expresiones lambda en Python son una forma corta de declarar funciones pequeñas y anónimas (no es necesario proporcionar un nombre para las funciones lambda).

Las funciones Lambda se comportan como funciones normales declaradas con la palabra clave `def`. Resultan útiles cuando se desea definir una función pequeña de forma concisa. Pueden contener solo una expresión, por lo que no son las más adecuadas para funciones con instrucciones de flujo de control.


Las llamamos “funciones anónimas” porque técnicamente carecen de nombre.

Al contrario que una función normal, no la definimos con la palabra clave estándar  _def_  que utilizamos en  _Python_. En su lugar, las funciones Lambda se definen como una  **línea que ejecuta una sola expresión**. Este tipo de funciones pueden tomar cualquier número de argumentos, pero solo pueden tener una expresión.


Si una función es utilizada una sola vez, lo mejor es usar una función lambda para evitar código innecesario y desorganizado.

**Sintaxis de una función Lambda**

La sintaxis de una función lambda es  `lambda args: expresión`. Primero escribes la palabra clave  `lambda`, dejas un espacio, después los argumentos que necesites separados por coma, dos puntos  `:`, y por último la expresión que será el cuerpo de la función.

Recuerda que no puedes darle un nombre a una función lambda, ya que estas son anónimas (sin nombre) por definición.

`lambda argumentos: expresión`

Las funciones Lambda pueden tener cualquier número de argumentos, pero solo una expresión.

```py
# Función Lambda para calcular el cuadrado de un número
square = lambda x: x ** 2
print(square(3)) # Resultado: 9

# Funcion tradicional para calcular el cuadrado de un numero
def square1(num):
  return num ** 2
print(square(5)) # Resultado: 25
```

```py
lambda_func = lambda x: True if x**2 >= 10 else False
lambda_func(3) # Retorna False
lambda_func(4) # Retorna True
```


```python
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtrado = filter(lambda x: x % 2 != 0, mi_lista)

list(filtrado)
# [1, 3, 5, 7, 9]
```

¿Entonces qué ha ocurrido? Le dijiste a `filter` que tomara cada elemento en `mi_lista` y aplicara la expresión lambda. Los valores que devuelven `False` se filtran.

una función `lambda` no tiene un nombre, y por lo tanto salvo que sea asignada a una variable, es totalmente inútil. Para ello debemos.

suma  =  lambda  a,  b:  a  +  b

Es posible tener argumentos con valor asignado por defecto.

```
(lambda a, b, c=3: a + b + c)(1, 2) # 6

```

También se pueden pasar los parámetros indicando su nombre.

```
(lambda a, b, c: a + b + c)(a=1, b=2, c=3) # 6

```

Al igual que en las funciones se puede tener un número variable de argumentos haciendo uso de  `*`, lo conocido como  **tuple unpacking**.

```
(lambda *args: sum(args))(1, 2, 3) # 6
```

Y si tenemos los parámetros de entrada almacenados en forma de  `key`  y  `value`como si fuera un diccionario, también es posible llamar a la función.

```
(lambda **kwargs: sum(kwargs.values()))(a=1, b=2, c=3) # 6

```

Por último, es posible devolver más de un valor.

```
x = lambda a, b: (b, a)
print(x(3, 9))
# Salida (9,3)
```


También es posible que una función devuelva una función lambda.

Si necesitas funciones que multipliquen diferentes números, por ejemplo, duplicar, triplicar, etc... una función lambda puede ser útil

En lugar de crear múltiples funciones, puedes crear una sola función  `multiplicar_por()`  y llamarla con diferentes argumentos para crear una función que duplique o triplique.

```python
def multiplicar_por (n):
  return lambda x: x * n
  
duplicar = multiplicar_por(2)
triplicar = multiplicar_por(3)
diez_veces = multiplicar_por(10)
```

## Comprensión de lista

La comprensión de listas es una forma de recorrer una lista para producir una nueva lista basada en algunas condiciones.
Vayamos al grano, las  _list comprehension_  nos permiten crear listas de elementos en una sola línea de código. Por ejemplo, podemos crear una lista con los cuadrados de los primeros 5 números de la siguiente forma

```
cuadrados = [i**2 for i in range(5)]
#[0, 1, 4, 9, 16]

```

De no existir, podríamos hacer lo mismo de la siguiente forma, pero necesitamos alguna que otra línea más de código.

```
cuadrados = []
for i in range(5):
    cuadrados.append(i**2)
#[0, 1, 4, 9, 16]
```

veamos la sintaxis general de las comprensiones de listas.

```
# lista = [expresión for elemento in iterable]
```

list_variable =  [x for x in iterable]

Es decir, por un lado tenemos el  `for elemento in iterable`, que itera un determinado iterable y “almacena” cada uno de los elementos en  `elemento`  [como vimos en este otro post sobre el for](https://ellibrodepython.com/for-python/). Por otro lado, tenemos la  `expresión`, que es lo que será añadido a la lista en cada iteración.

La expresión puede ser una operación como hemos visto anteriormente  `i**2`, pero también puede ser un valor constante. El siguiente ejemplo genera una lista de cinco unos.

```
unos = [1 for i in range(5)]
#[1, 1, 1, 1, 1]
```

La expresión también puede ser una llamada a una función. Se podría escribir el ejemplo anterior del cálculo de cuadrados de la siguiente manera.

```
def eleva_al_2(i):
    return i**2

cuadrados = [eleva_al_2(i) for i in range(5)]
#[0, 1, 4, 9, 16]
```

Como puedes observar, las posibilidades son bastante amplias. Cualquier elemento que sea iterable puede ser usado con las  _list comprehensions_. Anteriormente hemos iterado  `range()`  pero podemos hacer lo mismo para una lista. En el siguiente ejemplo vemos como dividir todos los números de una lista entre 10.

```
lista = [10, 20, 30, 40 , 50]
nueva_lista = [i/10 for i in lista]
#[1.0, 2.0, 3.0, 4.0, 5.0]
```

Pero, ¿y si quisiéramos realizar la operación sobre el elemento sólo si una determinada condición se cumple? Pues tenemos buenas noticias, porque es posible añadir un condicional  `if`. La expresión genérica sería la siguiente.

```
# lista = [expresión for elemento in iterable if condición]

```

Por lo tanto la  `expresión`  sólo se aplicará al  `elemento`  si se cumple la  `condición`. Veamos un ejemplo con una frase, de la que queremos saber el número de erres que tiene.

```
frase = "El perro de san roque no tiene rabo"
erres = [i for i in frase if i == 'r']
#['r', 'r', 'r', 'r']

```

Lo que hace el código anterior es iterar cada letra de la frase, y si es una  `r`, se añade a la lista.


Siempre que tengamos una colección iterable que queramos modificar, son una buena opción para evitar tener que escribir bucles for.

La comprensión de listas también puede contener condiciones if anidadas. Considera el siguiente bucle:

```py
divisible = list()
for i in range(50):
  if i%2 == 0:
    if i%3 == 0:
      divisible.append(i)
```

Usando la comprensión de listas, esto se puede escribir como:

```py
divisible = [i for i in range(50) if i%2==0 if i%3==0]
```

La sentencia If-Else también se puede utilizar junto con la comprensión de listas.

```py
lista_1 = [i if i%2==0 else i*-1 for i in range(10)]
```
!hay que tener cuidado con su uso y no abusar de ellas. Resulta fácil caer en la tentación de acabar escribiendo comprensiones que son tan largas que prácticamente son imposibles de leer, algo que puede no ser muy buena idea.

## Paquete pip

Paquete:

Gestor de paquetes:

Dependencias:


`pip`  es el gestor de paquetes principal para Python. Sirve para instalar, actualizar y eliminar paquetes de software en Python. Es una herramienta esencial para el desarrollo en Python, ya que facilita la gestión de dependencias y la reutilización de código.

pip (también conocido por el alias pip3 de Python 3) es **un sistema de gestión de paquetes escrito en Python y se utiliza para instalar y administrar paquetes de software**

Aunque Python por sí solo ya es capaz de hacer muchas cosas geniales, los profesionales de los datos -y, más ampliamente, los desarrolladores de software- suelen hacer uso de paquetes adicionales -también conocidos como bibliotecas- para facilitarles la vida. Un paquete es una colección de archivos, módulos y dependencias relacionados que pueden utilizarse repetidamente en diferentes aplicaciones y problemas.

Uno de los principales puntos fuertes de Python es su amplio catálogo de bibliotecas bien documentadas y completas. ¿Dónde están alojadas estas bibliotecas? ¿Cómo puedes instalar y gestionar los paquetes que te interesan?

Utilicemos una metáfora para entender qué es pip. Imagina que Python es una caja de herramientas bonita y equilibrada con los elementos esenciales que necesitarás para codificar. Cuando compras (instalas) Python en tu ordenador, viene con una amplia colección de herramientas adicionales (paquetes) que puedes utilizar en cualquier momento.

La llamada  [Biblioteca Estándar de Python](https://docs.python.org/3/library/)  es un amplio conjunto de paquetes incorporados que proporciona soluciones estandarizadas para muchos problemas que surgen en la programación cotidiana. Como estos paquetes vienen incluidos en las distribuciones modernas de Python, puedes utilizarlos sin necesidad de ninguna instalación adicional. Sólo tienes que "importarlos" a tu espacio de trabajo (más adelante hablaremos de ello).

Sin embargo, a veces no encontrarás la herramienta que buscas en Python o en su Biblioteca Estándar. En estos casos, tendrás que conseguir nuevas herramientas en otro lugar. Afortunadamente, Internet es un inmenso almacén donde puedes encontrar cientos de miles de paquetes desarrollados por desarrolladores de Python para todo tipo de propósitos.

Un gestor de paquetes (también llamado sistema de gestión de paquetes) es una herramienta que automatiza el proceso de instalación, actualización, configuración y eliminación de paquetes de un ordenador de forma coherente.

Los gestores de paquetes están diseñados para eliminar la necesidad de instalaciones y actualizaciones manuales, garantizando así que un paquete se instala junto con todas las dependencias que necesita para funcionar. Asimismo, como los gestores de paquetes aprovechan la información almacenada en repositorios de paquetes certificados, como PyPi y  [Anaconda](https://anaconda.org/anaconda/repo), garantizan la integridad y autenticidad de los paquetes.

El gestor de paquetes más popular para Python es pip. Desarrollado en 2008, pip (acrónimo de "pip Install Packages") es hoy la  [herramienta estándar](https://packaging.python.org/en/latest/guides/tool-recommendations/)  para instalar paquetes de Python y sus dependencias de forma segura. Las distribuciones más recientes de Python vienen con pip preinstalado. Python 2.7.9 y Python 3.4 y versiones posteriores incluyen pip por defecto.

Pip es una herramienta potente y fácil de usar que te permite gestionar paquetes de Python utilizando un puñado de comandos. 

En caso de que quieras instalar un paquete que cumpla determinadas condiciones en cuanto a versiones, pip te permite utilizar ciertas condiciones booleanas. Por ejemplo, si quieres instalar una versión de pandas mayor o igual que v.1.0.0 y menor que 1.5:

`>>pip install pandas>=1.0.0,<1.5.0`

Cuando trabajas en proyectos colaborativos, es muy habitual que todos los miembros del equipo utilicen los mismos paquetes con las mismas versiones. Para asegurarte de ello, la mejor forma es instalar paquetes utilizando un archivo de requisitos. Suele ser un archivo de texto que contiene todos los paquetes, junto con sus respectivas versiones, que se utilizan en el proyecto.

Pip te permite instalar una lista de paquetes a la vez utilizando un archivo de requisitos. Por ejemplo, si necesitamos para nuestro proyecto los paquetes  [numpy](https://www.datacamp.com/es/courses/introduction-to-numpy?),  [pandas](https://www.datacamp.com/es/courses/data-manipulation-with-pandas)  y  [TensorFlow](https://www.datacamp.com/es/courses/introduction-to-tensorflow-in-python), podríamos incluirlos, junto con las versiones deseadas, en un archivo requirements.txt, como se muestra a continuación:

![requisitos de pip install](https://images.datacamp.com/image/upload/v1676550998/pip_install_requirements_dd5b541997.png)

Si quieres crear un archivo de requisitos para compartirlo con el resto del equipo, puedes utilizar la siguiente instrucción:

`>>pip freeze > requirements.txt`

Para instalar los paquetes enumerados en un archivo requirements.txt, sólo tenemos que ejecutar

`>>pip install -r requirements.txt`

A veces necesitarás actualizar a una versión más reciente un paquete que ya tengas instalado en tu ordenador. Pip hace que este proceso sea extremadamente fácil. Por ejemplo, si quieres actualizar pandas a la última versión:

`>>pip install --upgrade pandas`

[POWERED BY](https://www.datacamp.com/datalab) 

En caso de que quieras actualizar todos los paquetes enumerados en un requirements.txt, podrías utilizar:

`>>pip install -r requirements.txt --upgrade`




-   **Instalación de paquetes:**
    
    `pip install <nombre_paquete>`  permite instalar paquetes desde el repositorio oficial de Python Package Index (PyPI) o desde otras fuentes.
    
-   **Actualización de paquetes:**
    
    `pip install --upgrade <nombre_paquete>`  actualiza un paquete a la última versión disponible.
    
-   **Eliminación de paquetes:**
    
    `pip uninstall <nombre_paquete>`  elimina un paquete del entorno de Python.
    
-   **Gestión de dependencias:**
    
    `pip freeze`  permite crear un archivo  `requirements.txt`  con la lista de paquetes y versiones instaladas en un entorno, facilitando la replicación de entornos en otros sistemas.
    
-   **Entornos virtuales:**
    
    `pip`  es compatible con entornos virtuales, lo que permite aislar las dependencias de diferentes proyectos.
    
-   **Versiones específicas:**
    
    Permite instalar versiones específicas de un paquete (e.g.,  `pip install pandas==1.3.4`).

Si necesitas información adicional sobre los distintos comandos pip disponibles y cómo utilizarlos, ejecútalos:

`>>pip help`

Para listar todos los paquetes instalados en tu entorno:

`>>pip list`

Para ver un resumen de un paquete de tu interés:

`>>pip show [NameOfPackage]`
> Written by Maite Ekhiñe Mora
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTY4NzcxNDExOSwtMTE2MTczMjUyMCwxOT
Q3NjEyMTMxLC00MDgyNDA3MjQsMjUwNTQzNDk4LC0xNDE4MDM3
NTYsMjQ4MjA3MzM4LDY2MDgzNjExMSwtMTExMDY5NDIxMiw2Mj
YwMDgyMTUsLTUzMDg0OTgzLDE2NDYyMjMyMywyMDg1MDg0MzY3
LC0xMzMwMzAxMDc3LDgxNjQwOTM3NSwxOTgxMTUxMjg5LDIzNz
IxNDc0OSwtMTM0MjQ1MjAwMywyNTQ3OTc0LDE2NTQ0MzgwNDVd
fQ==
-->