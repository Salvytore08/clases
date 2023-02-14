lista1 = [1,2,3,4,5,6,7,8,9,10]
lista2 = [18,19,20,21,22,23,24]

def MayorEdad(lista1,lista2):
    lista = lista1+lista2
    a = 0
    for i in lista:
        if i >= 18:
            a += 1
    
    return f'Hay {a} mayores de edad'

print(MayorEdad(lista1,lista2))