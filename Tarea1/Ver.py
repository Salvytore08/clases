import time

def ver(
    dict:dict
):
    """
    Función que permite ver los usuarios de la biblioteca
    
    ~Parámetros~
     dict = Diccionario
    """
    a = str(input('\nPor favor ingrese el usuario que desea ver: '))
    print(f'{a} : {dict[a]}')
    time.sleep(1.2)