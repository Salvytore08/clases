lista1 = []

def añadir(lista1:list) -> list:
    a = int(input('¿Cuántas palabras debe tener la lista?: '))
    for i in range(a):
        b = str(input('Por favor ingrese una palabra: '))
        lista1.append(b)
    return lista1
    
def eliminar(lista:list) -> list:
    lista2 = []
    a = int(input('¿Cuántas palabras desea eliminar?: '))
    for i in range(a):
        b = str(input('Por favor ingrese una palabra: '))
        lista2.append(b)
    for i in lista2:
        if i in lista:
            lista.remove(i)
    print(lista)
    
print(añadir(lista1))
eliminar(lista1)



    




