import hashlib
class Hash():
    def generarHash(self):
        digest=self.hexdigest()# Esto sirve para que se encripte en lenguaje en hexadecimal
        return digest
print("Leia. ¿Cual es el mensaje para Luke?")
mensaje=input()
algoritmo="SHA256" #SHA256 es un algoritmo el cual te encripta en 256 bytes toda la informacion que le pidas
def encriptar(mensaje,algoritmo):
    datos=bytes(mensaje,"utf-8")
    h=hashlib.new(algoritmo,datos)
    h1=Hash.generarHash(h)
    return h1
def guion():
    print("Darth Siduos intenta captar el mensaje pero no entiende lo que le sale una cosa muy extraña, propia de los mandalorianos")
    print(encriptar(mensaje,algoritmo))
    print("Luke recibe el mensaje")
    print(mensaje)
    print("Y cumple con su mision que le ha mandado Leia, acabando con la Estrella de la muerte y pensando que han matado a Darth Sidios")
guion()