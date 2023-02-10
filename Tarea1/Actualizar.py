import time

def actualizar(
    dict:dict
):
    """
    Función que permite actualizar usuarios de la biblioteca
    
    ~Parámetros~
     dict = Diccionario
    """
    a = str(input('Por favor ingrese el nombre del usuario que desea acualizar: '))
    if a in dict:
        b = str(input('¿Seguro que quiere actualizar el usuario? (Si o No): '))
        if b.lower() == 'si':
            nom = str(input('Por favor ingrese el nuevo nombre: '))
            lib = str(input('Por favor ingrese el nueo libro que desea pedir: '))
            dict.update({nom:lib})
        else:
            print('Puede salir')
            time.sleep(1.2)