import time

def ver(
    dict:dict
):
    """
    Función que permite ver los usuarios de la biblioteca
    
    ~Parámetros~
     dict = Diccionario
    """
    a = str(input('Por favor ingrese el usuario que desea ver: '))
    for a in dict:
        print(f'{a} : {dict[a]}')