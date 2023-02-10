import time

def eliminar(
    dict:dict
):
    """
    Función que permite eliminar usuarios de la biblioteca
    
    ~Parámetros~
     dict = Diccionario
    """
    a = str(input('Por favor ingrese el nombre del usuario que desea eliminar: '))
    if a in dict:
        print(f'{a} : {dict[a]}')
        b = str(input('¿Seguro que quiere eliminar el usuario? (Si o No): '))
        if b.lower() == 'si':
            dict.pop(a)
        else:
            print('Puede salir')
            time.sleep(1.2)
    else:
        print('El usuario no está disponible')
        time.sleep(1.2)