# Cree un bucle For de Python.

libros = ['Amarilla', 'El plan C', 'No te escondo nada', 'Anna O', 'La vida imposible']

for libro in libros:
    print(libro)


# Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.

def suma(num1, num2, num3):
    return num1 + num2 + num3

print(suma(5,7,8))


# Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.

suma = lambda num1, num2, num3: num1 + num2 + num3

print(suma(5,7,8))


# Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista.

nombre = 'Enrique' lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

if nombre in lista_nombre:
    print('el nombre está incluido en la lista')
else:
    print('el nombre no está incluido en la lista')