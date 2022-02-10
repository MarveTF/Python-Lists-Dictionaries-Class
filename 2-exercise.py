""" 
Escriba una clase de Python llamada Estudiante con varias instancias estudiante1, estudiante2, etc...
y asigne valores dados a los atributos (nombre, calificacion y edad) de dichas instancias. 

Imprimir:
1. Mensaje de felicitaciones a los estudiantes con grados mayores o iguales a 15.
2. Mensaje de aliento a los estudiantes con grados menores de 15 pero no inferiores a 10.
3. Mensaje de alerta a estudiantes con grados menores a 10.

Adicionalmente se deben retornar los estudiantes ordenados (decrecientemente) por edad en una lista.
"""
class Estudiante:
    def __init__(self, nombre, calificacion, edad):
        self.nombre = nombre
        self.calificacion = calificacion
        self.edad = edad

    def mensaje(self):
        if self.calificacion >= 15:
            print('felicitaciones')

        elif 10 <= self.calificacion and self.calificacion < 15:
            print('aliento')

        elif self.calificacion < 10:
            print('alerta')

    def getedad(self):
        listedad =[]
        listedad.append(self.edad)
        print(listedad)

estudiante1 = Estudiante('Marvelys', 18, 20)
estudiante2 = Estudiante('Javier', 12, 18)
estudiante3 = Estudiante('Sandro', 5, 30)
estudiante1.mensaje()
estudiante2.mensaje()
estudiante3.mensaje()

newlist= []
estudiante1.getedad()
estudiante2.getedad()
estudiante3.getedad()

