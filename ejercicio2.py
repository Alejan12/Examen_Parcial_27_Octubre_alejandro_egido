lista=[18, 50, 210, 80, 145, 333, 70, 30]

def multiplo10_menor200(lista):
    for i in range(len(lista)):
        if lista[i]%10==0 and lista[i]<200:
            
            return (lista[i])
multiplo10_menor200(lista)
def parar(lista):
    for i in range(len(lista)):
        if lista[i]>300:
            
            return (lista[:5])
            break
parar(lista)
def organizar(lista):
    a=lista.sort()
    return a
organizar(lista)
def mirar145(lista):
    for i in range(len(lista)):
        if 145 in lista:
            return 145
            break
        else:
            return -1
mirar145(lista)

