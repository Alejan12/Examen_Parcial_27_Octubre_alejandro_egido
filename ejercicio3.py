from collections import deque
class Alumno():
    def __init__(self,clase,notas):
        self.clase=clase
        self.notas=notas
    def __str__(self):
        return "El alumno {} se ha creado con exito  ".format(self.clase)
clase=deque()
notas=deque()
clase.append(input("Introduzca el nombre del alumo: "))
clase.append(input("Introduzca el nombre del alumo: "))
notas.append(input("Introduzca la nota del alumno: "))
notas.append(input("Introduzca la nota del alumno: "))
def calificar(clase,notas):
    for i in range(len(notas)):
        if int(notas[i])<5:
            print("El alumno "+clase[i]+" ha suspendido Algoritmos")
        else:
            print("El alumno "+clase[i]+" ha aprobado Algoritmos")
calificar(clase,notas)