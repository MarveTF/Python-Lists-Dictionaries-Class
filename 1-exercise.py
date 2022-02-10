""" 
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
"""

students = {
    'Alex': 20,
    'Paola': 22,
    'Piero': 21,
    'Christian': 36,
    'Yahyr': 35
}
studentslist=[]
find_max = max(students, key=students.get)
# print(find_max)
studentslist.append(find_max)
# print(studentslist)

find_min = min(students, key=students.get)
# print(find_min)
studentslist.append(find_min)
print(studentslist)

# studentsList =
# print(studentsList)