
## ¿Qué es un condicional?

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





## ¿Cuáles son los diferentes tipos de bucles en Python? ¿Por qué son útiles?

En Python, los bucles son fundamentales para repetir código. Los dos tipos principales son los bucles  `for`  y los bucles  `while`. Los bucles  `for`  son ideales cuando se conoce de antemano cuántas veces se repetirá el código, mientras que los bucles  `while`  son útiles cuando la cantidad de repeticiones depende de una condición. 

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


## ¿Qué es una lista por comprensión en Python?





## ¿Qué es un argumento en Python?





## ¿Qué es una función Lambda en Python?





##  ¿Qué es un paquete pip?

> Written with [StackEdit](https://stackedit.io/)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTU4MjY0MjIxMSwxODE4MzIwNjU2LC0xMD
g0OTcxNTAyLC0xNDgyODgwNjE1LC0xMzc3NDk3MDQ2LDE5OTQ0
OTU2MTIsLTg3Mzk2MTE1MCwxMjI1MDQyNzkwLDE2OTY5MjQwOT
hdfQ==
-->