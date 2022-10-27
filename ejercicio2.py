lista=[18, 50, 210, 80, 145, 333, 70, 30]
def multiplo10_menor200(lista):
    for i in range(len(lista)):
        if lista[i]%10==0 and lista[i]<200:
            print("Estos son los valores menores de 200 y que son divisibles entre 10")
            print(lista[i])
multiplo10_menor200(lista)
def parar(lista):
    for i in range(len(lista)):
        if lista[i]>300:
            print("Estos son los valores que hay en la lista antes de 300")
            print(lista[:5])
            break
parar(lista)
def organizar(lista):
    a=lista.sort()
    print("Esta es la lista organizada")
    print(a)
organizar(lista)
def mirar145(lista):
    for i in range(len(lista)):
        if 145 in lista:
            print("Si que sale el valor")
            print(145)
            break
        else:
            print("No sale el examen")
            print(-1)
mirar145(lista)