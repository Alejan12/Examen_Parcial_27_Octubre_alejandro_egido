class Alumno():
    def __init__(self,clase,notas):
        self.clase=clase
        self.notas=notas
    def __str__(self):
        return "El alumno {} ha sacado la nota {} ".format(self.clase,self.notas)
class Beca(Alumno):
    def __init__(self, clase, notas, beca):
        super().__init__(clase, notas)
        self.beca=beca
    def __str__(self):
        return Alumno.__str__(self)+"{} ha tenido derecho a beca".format(self.beca)
a=Beca("Alex",5,"No")
b=Beca("Ruben",10,"SI")
print(a)
print(b)