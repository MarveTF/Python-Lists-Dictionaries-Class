
## Ejercicio 01.

Escriba un programa Python para convertir una lista de diccionarios en una lista de valores correspondientes a la clave especificada.

Use una comprension de listas (list comprehension) y dict.get() para obtener el valor de la clave para cada diccionario en lst.

Ejemplo:
students = [
{'name': 'Theodore', 'age': 18},
{'name': 'Mathew', 'age': 22},
{'name': 'Roxanne', 'age': 20},
{'name': 'David', 'age': 18}
]

se espera el retorno de:
[['Theodore', 18], ['Mathew', 22], ['Roxanne', 20], ['David', 18]]

## Ejercicio 02.

Escriba un programa en Python para encontrar la clave del valor máximo y minimo en un diccionario.
Ejemplo:

students = {
'Alex': 20,
'Paola': 22,
'Piero': 21,
'Christian': 36
'Yahyr': 35
}

se espera el retorno de:
(Christian, Alex)

## Ejercicio 03.

"""
Escriba una clase de Python llamada Estudiante con varias instancias estudiante1, estudiante2, etc...
y asigne valores dados a los atributos (nombre, calificacion y edad) de dichas instancias.

Imprimir:

1. Mensaje de felicitaciones a los estudiantes con grados mayores o iguales a 15.
2. Mensaje de aliento a los estudiantes con grados menores de 15 pero no inferiores a 10.
3. Mensaje de alerta a estudiantes con grados menores a 10.

Adicionalmente se deben retornar los estudiantes ordenados (decrecientemente) por edad en una lista.
"""
