"""
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
"""
students = [
    {'name': 'Theodore', 'age': 18},
    {'name': 'Mathew', 'age': 22},
    {'name': 'Roxanne', 'age': 20},
    {'name': 'David', 'age': 18}
]

studentName = [x.get('name') for x in students]
studentAge = [x.get('age') for x in students]

# print(studentName)
# print(studentAge)

studentsList = dict(zip(studentName, studentAge))
print(studentsList)



