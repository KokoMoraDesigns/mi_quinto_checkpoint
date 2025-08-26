
# Breve glosario de Python

## Argumento

En Python, un argumento es la indicación que le das a una función determinada sobre cuál es la salida que estás tratando de lograr. El parámetro, por otro lado, es el nombre que le asignas a dicho argumento al formular la función.

A continuación unos ejemplos según los distintos tipos de argumentos que existen.


#### Argumento posicional

El orden en que se incluyen los argumentos al declarar la función **debe ser el mismo** orden que utilizaste al formular los parámetros de la función. 


    sum (a, b, c) --> a, b y c siendo los *parámetros* de la función

	sum (4, 8, 9) --> 4, 8 y 9 siendo los *argumentos* de la función

	salida = print(sum (4, 8, 9)) = a + b `c = 4 + 8 + 9 = 21



#### Argumento de palabra clave

El orden en que se incluyen los argumentos al declarar la función **no es relevante**, dado que vamos a puntualizar en la declaración a qué parámetro  estamos haciendo referencia.

    sum (a=4, c=9, b=8)
    
    salida = print(sum(a=4, c=9, b=8)) = 21


Existe la posibilidad de combinar en una llamada a la función argumentos posicionales y de palabras clave, en cuyo caso, **los argumentos posicionales deben ir al principio** de la declaración.

    sum (4, c=9, b=8)
    
    salida = print(sum(4, c=9, b=8)) = 21



#### Argumento predeterminado
    
    Son argumentos que tienen un valor predefinido y se pueden omitir en la llamada a la función.

-   Los argumentos predeterminados son valores que se proporcionan al definir funciones.
-   El operador de asignación `=`se utiliza para asignar un valor predeterminado al argumento.
-   Los argumentos predeterminados se vuelven opcionales durante las llamadas de función.
-   Si proporcionamos un valor a los argumentos predeterminados durante las llamadas de función, anula el valor predeterminado.
-   La función puede tener cualquier número de argumentos predeterminados.
-   Los argumentos predeterminados deben seguir a los argumentos no predeterminados.

En el siguiente ejemplo, el valor predeterminado se asigna al argumento `b` y `c`.

```
def add(a,b=5,c=10):
    return (a+b+c
```


#### Argumento arbitrario

Permiten a las funciones recibir un número variable de argumentos.`*args`  se utiliza para argumentos posicionales, mientras que  `**kwargs`  se utiliza para argumentos de palabra clave.


[Los argumentos de longitud variable](https://builtin-com.translate.goog/articles/python-variable-in-string?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=rq) también se conocen como argumentos arbitrarios. Si desconocemos de antemano el número de argumentos necesarios para la función, podemos usar argumentos arbitrarios. Estos argumentos son de dos tipos: argumentos posicionales arbitrarios y argumentos de palabras clave arbitrarios.

Para argumentos posicionales arbitrarios, se coloca un [asterisco (*)](https://builtin-com.translate.goog/data-science/merging-lists-in-python?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=rq) antes de un parámetro en la definición de función que puede contener argumentos de longitud variable que no sean palabras clave. Estos argumentos se agruparán en una [tupla](https://builtin-com.translate.goog/software-engineering-perspectives/python-tuples-vs-lists?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=rq) . Antes del número variable de argumentos, pueden aparecer cero o más argumentos normales.

```
def add(*b):
    result=0
    for i in b:
         result=result+i
    return result

```
def add(*b):
    result=0
    for i in b:
         result=result+i
    return result

print (add(1,2,3,4,5))
#Output:15
print (add(10,20))
#Output:30
```
print (add(1,2,3,4,5))
#Output:15
print (add(10,20))
#Output:30

Para un argumento de palabra clave arbitrario, se coloca un asterisco doble (**) antes de un parámetro en una función que puede contener argumentos de palabra clave de longitud variable.
```

```
def fn(**a):
    for i in a.items():
        print (i)
fn(numbers=5,colors="blue",fruits="apple")
'''
Output:
('numbers', 5)
('colors', 'blue')
('fruits', 'apple')
'''
```
*En Python, un argumento es un valor que se pasa a una función durante una llamada. Los argumentos son entradas que indican a las funciones qué salida deben dar
son los valores que se pasan a una función cuando se llama, mientras que los parámetros son los nombres que se utilizan para definir esos valores en la declaración de la función. Los argumentos pueden ser de diferentes tipos: posicionales, de palabra clave, predeterminados, y también existen mecanismos para pasar un número variable de argumentos.*


def  f(a=2,  /):  
	pass  

f()  # Allowed, argument is optional  

f(1)  # Allowed, it's a positional argument  

f(a=1)  # Error, positional only argument


def  f(a):  pass  f()  # Error, argument required  f(1)  # Allowed, it's a positional argument  f(a=1)  # Allowed, it's a keyword argument  # De hecho esta funcion equivale a:  def  f(*,  a,  /):  pass




#### Los argumentos predeterminados deben seguir a los argumentos no predeterminados

```
def add(a=5,b,c):
    return (a+b+c)

#Output:SyntaxError: non-default argument follows default argument
```

#### Los argumentos de palabras clave deben seguir a los argumentos posicionales

```
def add(a,b,c):
    return (a+b+c)

print (add(a=10,3,4))
#Output:SyntaxError: positional argument follows keyword argument
```

>!atención:#### Los argumentos predeterminados deben seguir a los argumentos no predeterminados

```
def add(a=5,b,c):
    return (a+b+c)

#Output:SyntaxError: non-default argument follows default argument
```

#### Los argumentos de palabras clave deben seguir a los argumentos posicionales

```
def add(a,b,c):
    return (a+b+c)

print (add(a=10,3,4))
#Output:SyntaxError: positional argument follows keyword argument
```


Para mejorar la legibilidad y el rendimiento, conviene restringir la forma en que se pueden pasar los argumentos, de modo que un desarrollador solo tenga que consultar la definición de la función para determinar si los elementos se pasan por posición, por posición o palabra clave, o por palabra clave.

argumentos solo posicionales:

Los parámetros posicionales se colocan antes de una `/`barra diagonal en la definición de la función. Esto `/`se utiliza para separar lógicamente los parámetros posicionales del resto. Los parámetros que siguen a `/`pueden ser posicionales, de palabra clave o de palabra clave.

```
def add(a,b,/,c,d):
    return a+b+c+d

print (add(3,4,5,6))
#Output:12

print (add(3,4,c=1,d=2))
#Output:6
```

Si especificamos argumentos de palabras clave solo para argumentos posicionales, se generará [TypeError](https://builtin-com.translate.goog/articles/typeerror-int-object-is-not-callable?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=rq) .

```
def add(a,b,/,c,d):
    return a+b+c+d

print (add(3,b=4,c=1,d=2))
#Output:TypeError: add() got some positional-only arguments passed as keyword
```

argumentos solo de palabras clave:

Para marcar parámetros como solo de palabras clave, coloque un `*`en la lista de argumentos justo antes del primer parámetro solo de palabras clave.

```
def add(a,b,*,c,d):
    return a+b+c+d

print (add(3,4,c=1,d=2))
#Output:10
```

Si especificamos argumentos posicionales para argumentos de solo palabras clave, se generará TypeError **.**

```
def add(a,b,*,c,d):
    return a+b+c+d

print (add(3,4,1,d=2))
#Output:TypeError: add() takes 2 positional arguments but 3 positional argumen
```

Las tres convenciones de llamada se utilizan en la misma función. En el siguiente ejemplo, la función `add`contiene los tres argumentos:

-   `a`, `b`: Argumentos únicamente posicionales.
-   `c`:Argumentos posicionales o de palabras clave.
-   `d`:Argumentos de sólo palabras clave.

```
def add(a,b,/,c,*,d):
    return a+b+c+d

print (add(3,4,1,d=2))
#Output:10
```

1.  Utilice **solo posicional** si desea que el nombre de los parámetros no esté disponible para el usuario. Esto es útil cuando los nombres de los parámetros no tienen un significado real.
2.  Utilice **solo posición** si desea imponer el orden de los argumentos cuando se llama a la función.
3.  Utilice **solo palabras clave** cuando los nombres tengan significado y la definición de la función sea más comprensible al ser explícita con los nombres.


def  funcion(a,  b,  *args,  **kwargs):  print("a =",  a)  print("b =",  b)  for  arg  in  args:  print("args =",  arg)  for  key,  value  in  kwargs.items():  print(key,  "=",  value)  funcion(10,  20,  1,  2,  3,  4,  x="Hola",  y="Que",  z="Tal")  #Salida #a = 10 #b = 20 #args = 1 #args = 2 #args = 3 #args = 4 #x = Hola #y = Que #z = Tal

Y por último un truco que no podemos dejar sin mencionar es lo que se conoce como _tuple unpacking_. Haciendo uso de `*`, podemos extraer los valores de una lista o tupla, y que sean pasados como argumentos a la función.

def  funcion(a,  b,  *args,  **kwargs):  print("a =",  a)  print("b =",  b)  for  arg  in  args:  print("args =",  arg)  for  key,  value  in  kwargs.items():  print(key,  "=",  value)  args  =  [1,  2,  3,  4]  kwargs  =  {'x':"Hola",  'y':"Que",  'z':"Tal"}  funcion(10,  20,  *args,  **kwargs)  #Salida #a = 10 #b = 20 #args = 1 #args = 2 #args = 3 #args = 4 #x = Hola #y = Que #z = Tal


## Bucle

En Python, los bucles son fundamentales para repetir código. Los dos tipos principales son los bucles  `for`  y los bucles  `while`. Los bucles  `for`  son ideales cuando se conoce de antemano cuántas veces se repetirá el código, mientras que los bucles  `while`  son útiles cuando la cantidad de repeticiones depende de una condición. 
Cabe destacar que existe dos tipos de bucles, los que tienen un número de iteraciones **no definidas**, y los que tienen un número de iteraciones **definidas**.
Bucles  `for`:

-   **Funcionamiento:** Iteran sobre una secuencia (como una lista, tupla, cadena, etc.) o sobre un rango de números.
-   **Ejemplo:**
    

Python

```
    mi_lista = [1, 2, 3]    for elemento in mi_lista:        print(elemento)
```

-   **Utilidad:** Ideales para procesar cada elemento de una colección, como imprimir nombres de una lista o realizar cálculos con números dentro de un rango.

Bucles  `while`:

-   **Funcionamiento:** Ejecutan un bloque de código mientras una condición sea verdadera.
-   **Ejemplo:**
    

Python

```
    contador = 0    while contador < 5:        print(contador)        contador += 1
```

-   **Utilidad:** Útiles cuando no se conoce de antemano cuántas veces se ejecutará el código, como solicitar entrada de usuario hasta que se ingrese un valor válido o realizar operaciones hasta que se cumpla una condición.
En resumen:

-   `for`: Iteración sobre secuencias conocidas.
-   `while`: Iteración condicionada a una condición.


Mientras que en el while la condición era evaluada en cada iteración para decidir si volver a ejecutar o no el código, en el  `for`  no existe tal condición, sino un  `iterable`  que define las veces que se ejecutará el código. En el siguiente ejemplo vemos un bucle  `for`  que se ejecuta 5 veces, y donde la  `i`  incrementa su valor “automáticamente” en 1 en cada iteración.

```
for i in range(0, 5):
    print(i)

# Salida:
# 0
# 1
# 2
# 3
# 4
```

for  i  in  "Python":  print(i)  # Salida: # P # y # t # h # o # n


-   Los  **iterables**  son aquellos objetos que como su nombre indica pueden ser iterados, lo que dicho de otra forma es, que puedan ser indexados. Si piensas en un array (o una  `list`  en Python), podemos indexarlo con  `lista[1]`  por ejemplo, por lo que sería un iterable.
-   Los  **iteradores**  son objetos que hacen referencia a un elemento, y que tienen un método  `next`  que permite hacer referencia al siguiente.

Como hemos comentado, los  **iterables**  son objetos que pueden ser iterados o accedidos con un índice. Algunos ejemplos de iterables en Python son las listas, tuplas, cadenas o diccionarios. Sabiendo esto, lo primero que tenemos que tener claro es que en un  `for`, lo que va después del  `in`**deberá ser siempre un iterable**.

```
#for <variable> in <iterable>:
#    <Código>
```


Es posible  **anidar**  los  `for`, es decir,  **meter uno dentro de otro**. Esto puede ser muy útil si queremos iterar algún objeto que en cada elemento, tiene a su vez otra clase iterable. Podemos tener por ejemplo, una lista de listas, una especie de matriz.

```
lista = [[56, 34, 1],
         [12, 4, 5],
         [9, 4, 3]]

```

Si iteramos usando sólo un  `for`, estaremos realmente accediendo a la segunda lista, pero no a los elementos individuales.

```
for i in lista:
    print(i)
#[56, 34, 1]
#[12, 4, 5]
#[9, 4, 3]

```

Si queremos acceder a cada elemento individualmente, podemos anidar dos  `for`. Uno de ellos se encargará de iterar las columnas y el otro las filas.

```
for i in lista:
    for j in i:
        print(j)
# Salida: 56,34,1,12,4,5,9,4,3
```


Iterando cadena al revés. Haciendo uso de  `[::-1]`  se puede iterar la lista desde el último al primer elemento.

```
texto = "Python"
for i in texto[::-1]:
    print(i) #n,o,h,t,y,P

```

Itera la cadena saltándose elementos. Con  `[::2]`  vamos tomando un elemento si y otro no.

```
texto = "Python"
for i in texto[::2]:
    print(i) #P,t,o
```


cuadrados  =  []  for  i  in  range(5):  cuadrados.append(i**2)  #[0, 1, 4, 9, 16]


x  =  5  while  x  >  0:  x  -=1  print(x)  # Salida: 4,3,2,1,0

En el ejemplo anterior tenemos un caso sencillo de  `while`. Tenemos una condición  `x>0`  y un bloque de código a ejecutar mientras dure esa condición  `x-=1`  y  `print(x)`. Por lo tanto mientras que  `x`  sea mayor que 0, se ejecutará el código. Una vez se llega al final, se vuelve a empezar y si la condición se cumple, se ejecuta otra vez. En este caso se entra al bloque de código 5 veces, hasta que en la sexta,  `x`  vale cero y por lo tanto la condición ya no se cumple. Por lo tanto el  `while`  tiene dos partes:

-   La  **condición**  que se tiene que cumplir para que se ejecute el código.
-   El  **bloque de código**  que se ejecutará mientras la condición se cumpla.


Algo no muy corriente en otros lenguajes de programación pero si en Python, es el uso de la cláusula  `else`  al final del  `while`. Podemos ver el ejemplo anterior mezclado con el  `else`. La sección de código que se encuentra dentro del  `else`, se ejecutará cuando el bucle termine, pero solo si lo hace “por razones naturales”. Es decir, si el bucle termina porque la condición se deja de cumplir, y no porque se ha hecho uso del  `break`.

```
x = 5
while x > 0:
    x -=1
    print(x) #4,3,2,1,0
else:
    print("El bucle ha finalizado")
```

La palabra reservada `while` ejecuta una porción de código una y otra vez hasta que la condición especificada sea falsa; o, dicho de otro modo, ejecuta una porción de código mientras que la condición sea verdadera.

¡Genial! Lo que ha ocurrido aquí es lo siguiente: el bucle _for_ ejecuta el bloque de código indentado (en este caso la llamada a `print()`) tantas veces como elementos haya en la colección indicada a la derecha del operador `in`. Pero, cada vez que ese código es ejecutado, la variable `lenguaje` tendrá un valor diferente: en la primera ejecución será igual a `"Python"`; en la segunda, a `"C"`; y así hasta alcanzar el final de la lista.

-   La palabra clave  `while`;
-   Una afección que se transmite a  `True`  o  `False`; Y
-   Un bloque de código que quieres ejecutar repetidamente


## Condicional

> Las sentencias condicionales también se denominan sentencias de decisión. **Se utilizan para ejecutar un bloque específico de código si las condiciones dadas son verdaderas o falsas**. es una forma de controlar el flujo de ejecución del código, permitiendo que se ejecuten diferentes bloques de código en función de si una condición es verdadera o falsa. Las condicionales son fundamentales para crear programas que puedan tomar decisiones y responder de manera diferente a diferentes situaciones. Utiliza la palabra clave «If» seguida de la condición que debe cumplirse. El programador también elige la acción que se ejecutará si se cumple la condición. Los elementos que analizaremos a continuación son: elementos de la condicional, sintaxis, tipos de condicionales, operadores de las condicionales, y, por supuesto, ejemplos.

Se comprueba la condición y el conjunto de código del bloque «If» se ejecuta si es verdadera. De lo contrario, el código del bloque «If» no se ejecuta y se ejecuta la sentencia que sigue a la sentencia If.

La sentencia «If» es útil si se puede especificar qué sentencias ejecutar si se cumple una condición. En cambio, para evaluar sentencias que determinan si una condición es verdadera y si otro conjunto de sentencias es falso, se utiliza la **sentencia condicional «if-else»**.

La sentencia «If-else» se utiliza para ejecutar tanto la parte verdadera como la falsa de una condición. Si la condición es verdadera, se ejecuta el **bloque de código If**. Si la condición es falsa, se ejecuta el bloque de código Else.

Se comprueba la expresión de prueba y se ejecutan las sentencias del **cuerpo del bloque de código If**. A continuación, se ejecutan las sentencias situadas debajo del **bloque If**.

Si los resultados de la expresión de prueba son falsos, se ejecutan las sentencias del código Else. A continuación, se ejecutan las sentencias del bloque If-else.

El bloque «Else» solo se ejecutará si las condiciones son falsas. Las acciones de este bloque se ejecutan cuando las condiciones no son verdaderas.

Cuando una sentencia If o If-else está presente dentro de otro bloque de sentencia If o If-Else, se trata de una **sentencia IF anidada**. Esta situación se produce cuando es necesario filtrar una variable varias veces y comprobar varias condiciones.

En una sentencia IF anidada, la indentación que permite **definir el alcance de cada sentencia** es esencial. El número de anidaciones posibles es ilimitado, pero cada una de ellas reduce la optimización del programa y lo hace más complejo de leer y entender. Por lo tanto, es mejor **reducir al mínimo el número de anidaciones**.

Las sentencias IF e If-else solo son útiles para **situaciones binarias**. En el caso de un problema condicional múltiple, se utiliza la sentencia «if-elif-else».

En primer lugar, se comprueba la condición de la sentencia If. Si es falsa, se evalúa la **sentencia Elif**. Si la condición también es falsa, se evalúa la sentencia Else.

En Python, la sentencia «Elif» se utiliza para comprobar múltiples condiciones si una condición es falsa. Es similar a la sentencia «If-Else», pero la diferencia es que «Elif» evalúa **múltiples condiciones** a diferencia de «Else».

Para probar **varias expresiones**, se puede utilizar una escalera de sentencias Elif. Esto se llama una «Elif ladder” (escalera Elif). El **controlador** comprueba las condiciones de la sentencia if, y si se cumplen, se ejecuta **el conjunto de sentencias de ese bloque**.

En caso contrario, el controlador pasa al **primer bloque Elif** para evaluar las condiciones. El proceso continúa para todas las sentencias Elif, y si determina en la evaluación que todas las condiciones If y Elif se son falsas, se ejecuta el bloque Else.

![](https://db0dce98.rocketcdn.me/es/files/2023/02/if-elfi-else.jpg)

Es muy importante tener en cuenta que la sentencia `if` debe ir terminada por `:` y el bloque de código a ejecutar debe estar indentado. Si usas algún editor de código, seguramente la indentación se producirá automáticamente al presionar enter. Nótese que el bloque de código puede también contener más de una línea, es decir puede contener más de una instrucción.

if  b  !=  0:  c  =  a/b  d  =  c  +  1  print(d)

Todo lo que vaya después del `if` y esté indentado, será parte del bloque de código que se ejecutará si la condición se cumple. Por lo tanto el segundo `print()` “Fuera if” será ejecutado siempre, ya que está fuera del bloque `if`.

Se puede también combinar varias condiciones entre el `if` y los `:`. Por ejemplo, se puede requerir que un número sea mayor que 5 y además menor que 15. Tenemos en realidad tres operadores usados conjuntamente, que serán evaluados por separado hasta devolver el resultado final, que será `True` si la condición se cumple o `False` de lo contrario.

Se puede usar también de manera conjunta todo, el `if` con el `elif` y un `else` al final. Es muy importante notar que `if` y `else` solamente puede haber uno, mientras que `elif` puede haber varios.

x  =  5  if  x  ==  5:  print("Es 5")  elif  x  ==  6:  print("Es 6")  elif  x  ==  7:  print("Es 7")

x  =  5  if  x  ==  5:  print("Es 5")  elif  x  ==  6:  print("Es 6")  elif  x  ==  7:  print("Es 7")  else:  print("Es otro")

El operador ternario o `ternary operator` es una herramienta muy potente que muchos lenguajes de programación tienen. En Python es un poco distinto a lo que sería en C, pero el concepto es el mismo. Se trata de una cláusula `if`, `else` que se define en una sola línea y puede ser usado por ejemplo, dentro de un `print()`.

> Ver https://peps.python.org/pep-0308/ 

x  =  5  print("Es 5"  if  x  ==  5  else  "No es 5")  #Es 5

Existen tres partes en un operador ternario, que son exactamente iguales a los que había en un `if``else`. Tenemos la condición a evaluar, el código que se ejecuta si se cumple, y el código que se ejecuta si no se cumple. En este caso, tenemos los tres en la misma línea.

```
# [código si se cumple] if [condición] else [código si no se cumple]

```

(if <condition>: <expression1> else: <expression2>)
The resulting expression is evaluated like this:

-   First, <condition> is evaluated.
-   If <condition> is true, <expression1> is evaluated and is the result of the whole thing.
-   If <condition> is false, <expression2> is evaluated and is the result of the whole thing.
- <condition> and <expression1> or <expression2>

En ciertas ocasiones necesitamos añadir código auxiliar a nuestros programas. Por ejemplo, añadimos una sentencia `if` que completamos posteriormente con su código a ejecutar. Como en Python se usa la indentación para delimitar las sentencias condicionales, si el intérprete no encuentra código indentado después de una sentencia `if`, lanza un error de tipo `IndentationError`. Este tipo de errores los puede detectar automáticamente un IDE para Python o una aplicación como [Atom con el paquete linter-flake8](https://www.programaenpython.com/miscelanea/configurar-atom-para-programar-en-python/). En cualquier caso, como se ilustra en el siguiente bloque de código, siempre podemos hacer uso de una sentencia `pass` la cual actúa como un marcador que hace que el interprete no nos lance un error.

if Ture:
	pass
print('Seguir...')

Tipos de condicionales en Python:

-   `if`:
    
    Ejecuta un bloque de código si la condición es verdadera. Si la condición es falsa, el bloque de código no se ejecuta.
    
-   `if-else`:
    
    Ejecuta un bloque de código si la condición es verdadera, y otro bloque de código si la condición es falsa.
    
-   `if-elif-else`:
    
    Permite evaluar múltiples condiciones. Se evalúa la condición en el  `if`. Si es falsa, se evalúa la condición en el  `elif`, y así sucesivamente. Si ninguna condición es verdadera, se ejecuta el bloque de código en el  `else`.


edad = 20
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

En este ejemplo, el código dentro del bloque  `if`  se ejecutará si la variable  `edad`  es mayor o igual a 18. De lo contrario, se ejecutará el código dentro del bloque  `else`.


Operadores de comparación:

Los condicionales utilizan operadores de comparación para evaluar las condiciones:

-   `==`  (igual a)
-   `!=`  (diferente a)
-   `>`  (mayor que)
-   `<`  (menor que)
-   `>=`  (mayor o igual que)
-   `<=`  (menor o igual que)

En resumen: Los condicionales en Python, como  `if`,  `else`  y  `elif`, son herramientas esenciales para crear programas que puedan adaptarse a diferentes situaciones y tomar decisiones basadas en condiciones específicas.


bucles anidados:
#Take user input
number = 2 

#condition of the while loop
while number < 5 :  
    # condition of the nested while loop    
    while number % 2 == 0: 
        print("The number "+ str(number)+" is even")

Verás que el control entra en el primer bucle for y el valor de la variable  `number`  se inicializa como 0. Se imprime la primera sentencia print, y luego el control entra en el segundo bucle for, donde el valor de la variable  `another_number`  se inicializa a  `0`. La primera sentencia print del segundo bucle for se imprime una vez.

Ahora, el control vuelve al bucle for interno una vez más y el valor de  `another_number`  se inicializa de nuevo al siguiente número entero, seguido de la impresión de la declaración dentro de la función  `print()`.

El proceso anterior continúa hasta que el control ha atravesado el final de la función  `range()`, que en este caso es 5, y entonces el control vuelve al bucle exterior, inicializa la variable  `number`  con el siguiente número entero, imprime la sentencia dentro de la función  `print()`, visita el bucle interior y repite todos los pasos anteriores hasta atravesar la función  `range()`.

Este viaje del control desde el bucle exterior, pasando por el bucle interior y volviendo al bucle for exterior continúa hasta que el control ha recorrido todo el rango, que en tu caso es 3 veces.

#Print the below statement 3 times
for number in range(3) :  
    print("-------------------------------------------")
    print("I am outer loop iteration "+str(number))
    # Inner loop
    for another_number in range(5):  
        print("****************************")
        print("I am inner loop iteration "+str(another_number))

-------------------------------------------
I am outer loop iteration 0
****************************
I am inner loop iteration 0
****************************
I am inner loop iteration 1
****************************
I am inner loop iteration 2
****************************
I am inner loop iteration 3
****************************
I am inner loop iteration 4
-------------------------------------------
I am outer loop iteration 1
****************************
I am inner loop iteration 0
****************************
I am inner loop iteration 1
****************************
I am inner loop iteration 2
****************************
I am inner loop iteration 3
****************************
I am inner loop iteration 4
-------------------------------------------
I am outer loop iteration 2
****************************
I am inner loop iteration 0
****************************
I am inner loop iteration 1
****************************
I am inner loop iteration 2
****************************
I am inner loop iteration 3
****************************
I am inner loop iteration 4


Bucle infinito: 
#Take user input
number = 2 

#condition of the while loop
while number < 5 :  
    # condition of the nested while loop    
    while number % 2 == 0: 
        print("The number "+ str(number)+" is even")


```python
numero = 0
while numero < 10:
    print(f"Numero es {numero}!")
    numero = numero + 1
```
Aquí, la variable  `numero`  es fijada en  `0`  al inicio.

Antes de que cualquier código sea ejecutado, Python verifica la condición (`numero < 10`). Verifica si la condición es True, imprime el siguiente estado `Number is 0!`  y así mientras que la condición continúa siendo verdadero.

`numero`  es entonces incrementado en `1`. La condición es reevaluada, y si nuevamente es ver verdadero, todo el proceso se repite has que  `numero`  es igual a  `9`.

Ahora cuando llegamos al punto  `Numero es 9!`  y  `numero`  es incrementado en uno,  `numero`  es igual a  `10`  la condición deja de ser verdadero, y se convierte en falso`False`

Cómo viste anteriormente, los bucles  `while`  están acompañados típicamente por una variable cuyo valor cambia a través de la duración del bucle, hasta que finalmente se determina un punto en el cual el bucle llega a su cesación.

Si no agregas esta línea, crearás un  **bucle infinito**.

`numero`  no se incrementaría o actualizaría. Siempre sería fijado en `0`  por tanto la condición  `numero < 10`  será verdadero siempre. Esto significa que el bucle continuará siempre.

En Python, la instrucción  `break`  permite salir de un bucle  `for`  o  `while`  de forma inmediata. Cuando el código encuentra una instrucción  `break`  dentro de un bucle, el bucle se interrumpe y la ejecución del programa continúa con la siguiente línea de código después del bucle.

    for i in range(10):
        print(i)
        if i == 5:
            break
    print("Fin del bucle")
-   **Bucle anidados:**
    
    En bucles anidados,  `break`  interrumpe solo el bucle más interno en el que está.

Un ejemplo un poco más útil, sería el de buscar una letra en una palabra. Se itera toda la palabra y en el momento en el que se encuentra la letra que buscábamos, se rompe el bucle y se sale.

Esto es algo muy útil porque si ya encontramos lo que estábamos buscando, no tendría mucho sentido seguir iterando la lista, ya que desperdiciaríamos recursos.


break con bucles for:
```
cadena = 'Python'
for letra in cadena:
    if letra == 'h':
        print("Se encontró la h")
        break
    print(letra)

# Salida:
# P
# y
# t
# Se encontró la h
```

break con bucles while:

x  =  5  while  True:  x  -=  1  print(x)  if  x  ==  0:  break  print("Fin del bucle")  #4, 3, 2, 1, 0

break con bucles anidados:

Como hemos dicho, el uso de  `break`  rompe el bucle, pero sólo aquel en el que está dentro.

Es decir, si tenemos dos bucles anidados, el  `break`  romperá el bucle anidado, pero no el exterior.

Concretamente,  `continue`  se salta todo el código restante en la iteración actual y vuelve al principio en el caso de que aún queden iteraciones por completar.

La diferencia entre el  `break`  y  `continue`  es que el  `continue`  no rompe el bucle, si no que pasa a la siguiente iteración saltando el código pendiente.

En el siguiente ejemplo vemos como al encontrar la letra  `P`  se llama al continue, lo que hace que se salte el  `print()`. Es por ello por lo que no vemos la letra  `P`  impresa en pantalla.

cadena  =  'Python'  for  letra  in  cadena:  if  letra  ==  'P':  continue  print(letra)  # Salida: # y # t # h # o # n

A diferencia del  `break`, el  `continue`  no rompe el bucle sino que finaliza la iteración actual, haciendo que todo el código que va después se salte, y se vuelva al principio a evaluar la condición.

En el siguiente ejemplo podemos ver como cuando la  `x`  vale 3, se llama al  `continue`, lo que hace que se salte el resto de código de la iteración (el  `print()`). Por ello, vemos como el número 3 no se imprime en pantalla.

```
x = 5
while x > 0:
    x -= 1
    if x == 3:
        continue
    print(x)

#Salida: 4, 2, 1, 0
```

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
eyJoaXN0b3J5IjpbMjA1NjkyNTAxOSwxMzc5MTM4MzcsLTExMz
IyNzI2MDUsLTExMTM3Njk0OTYsLTE2ODUxMTE4MjEsMTA5ODAy
NTkxOCwtMTIwNzk2NjUwOSwtMjAxOTg2NTgyLDU3NTE1NjQxNi
w2MjUxMTkyNjgsLTg2MDczMzc1MiwtNDU1NDAyODgzLC0xMjQ2
MzQwMDAxLDc4MTQ1NDIzLDQxODI2NjA4LC0xMjY0MjE0NTU2LD
E2OTIwNjAzNzYsLTU1MDM0NzYwNSw3OTU4MTkwMTAsLTIxMDcx
OTg1MTRdfQ==
-->