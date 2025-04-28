
# Breve glosario de Python

## Argumento

son los valores que se pasan a una función cuando se llama, mientras que los parámetros son los nombres que se utilizan para definir esos valores en la declaración de la función. Los argumentos pueden ser de diferentes tipos: posicionales, de palabra clave, predeterminados, y también existen mecanismos para pasar un número variable de argumentos.

### Tipos de argumentos

#### Argumento posicional

Se pasan a la función en un orden específico que coincide con el orden de los parámetros en la definición de la función.

La función anterior se puede llamar de dos maneras:

En primer lugar, durante la llamada a la función, todos los argumentos se proporcionan como argumentos posicionales. Los valores que se pasan a través de los argumentos se transfieren a los parámetros según su posición. `10`se asigna a `a`, `20`se asigna a `b`y `30`se asigna a `c`.

```
print (add(10,20,30))
#Output:60
```

La segunda forma es combinar argumentos posicionales y de palabras clave. Los argumentos de palabras clave siempre deben ir después de los argumentos posicionales.

```
print (add(10,c=30,b=20))
#Output:60
```

#### Argumento de palabra clave

Se pasan a la función especificando el nombre del parámetro y su valor

Durante una llamada a una función, los valores que se pasan a través de argumentos no necesitan estar en el mismo orden que los parámetros en la definición de la función. Esto se puede lograr mediante argumentos de palabra clave.

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


## Lista de comprensión


## Paquete pip

> Written by Maite Ekhiñe Mora
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTA3NzQ4MDg4NywtNTUwMzQ3NjA1LDc5NT
gxOTAxMCwtMjEwNzE5ODUxNCwtMjIwNjY1NDQ5LC03NDMxNDM1
NTgsLTE1MTAwODkyMzQsODA0NzM1OTMwLC0xMTM0NjUwMTYsMj
AwODUyODc3NCwxNTk4NTA2ODExLC01ODI2NDIyMTEsMTgxODMy
MDY1NiwtMTA4NDk3MTUwMiwtMTQ4Mjg4MDYxNSwtMTM3NzQ5Nz
A0NiwxOTk0NDk1NjEyLC04NzM5NjExNTAsMTIyNTA0Mjc5MCwx
Njk2OTI0MDk4XX0=
-->