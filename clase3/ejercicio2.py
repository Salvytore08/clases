profesores = ['Felipe', 'Isaac']
estudiantes = ['Omar', 'Gabriela', 'Joshua', 'Brayan', 'Yo']

def añadir(lista1,lista2,lista3='si'):
    lista = lista1+lista2
    lista.append(lista3)
    print(lista)
    
añadir(profesores,estudiantes,'Hola')