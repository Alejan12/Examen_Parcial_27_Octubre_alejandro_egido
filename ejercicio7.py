from sympy import *
from collections import deque
x=symbols("x")
y=symbols("y")
p1=3*x**2+x*y+4
p2=x**2+3*x*y+9
def restar(p1,p2):
    r=(p1-p2)
    return r
def dividir(p1,p2):
    dividi=div(p1,p2)
    return dividi
print("Estos son tus polinomios:")
print(p1)
print(p2)
print("Resta=")
print(restar(p1,p2))
print("Este es el resultado de la division:")
print(dividir(p1,p2))
p3=[]
p3.append("3*x**2")
p3.append("+")
p3.append("x*y")
p3.append("+")
p3.append("4")
def eliminar_termino(p3):
    p3.pop()
    p3.pop()
    return p3
print("Eliminamos el ultimo termino del primer polinomio")
print(eliminar_termino(p3))


