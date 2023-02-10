import time

def actualizar(
    dict:dict
):
    """
    Función que permite actualizar usuarios de la biblioteca
    
    ~Parámetros~
     dict = Diccionario
    """
    nom = str(input('\nPor favor ingrese el nombre del usuario que desea acualizar: '))
    if nom.lower() in dict:
        b = str(input('¿Seguro que quiere actualizar el usuario? (Si o No): '))
        if b.lower() == 'si':
            nom = str(input('Por favor ingrese el nuevo nombre: '))
            lib = str(input('Por favor ingrese el nuevo libro que desea pedir: '))
            nom = nom.lower()
            lib = lib.lower()
            dict.update({nom:lib})
        else:
            print('Puede salir')
            time.sleep(1.2)
    else:
        print('El usuario no está disponible')
        time.sleep(1.2)