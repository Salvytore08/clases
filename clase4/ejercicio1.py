lista = []

def añadir(lista:list) -> list:
    a = int(input('¿Cuántas palabras debe tener la lista?: '))
    for i in range(a):
        b = str(input('Por favor ingrese una palabra: '))
        lista.append(b)
    print(lista)

def eliminar(lista:list) -> list:
    a = int(input('¿Cuántas palabras desea eliminar?: '))
    for i in range(a):
        b = str(input('Por favor ingrese una palabra: '))
        lista.remove(b)
    print(lista)
    
añadir(lista)
eliminar(lista)



    




