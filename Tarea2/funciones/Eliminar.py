import time
try:
    def eliminar(
        dict:dict
    ):
        """
        Función que permite eliminar usuarios de la biblioteca
        
        ~Parámetros~
        dict = Diccionario
        """
        a = str(input('\nPor favor ingrese el nombre del usuario que desea eliminar: '))
        if a.lower() in dict:
            print(f'{a} : {dict[a]}')
            time.sleep(1.2)
            b = str(input('¿Seguro que quiere eliminar el usuario? (Si o No): '))
            if b.lower() == 'si':
                dict.pop(a)
            else:
                print('Puede salir')
                time.sleep(1.2)
   
except ValueError:
    print('Ingrese un nombre/opción válidos')
    print('Los nombres sólo pueden contener palabras')
    print('Las opciones sólo pueden ser si o no')
    time.sleep(1.5)
except KeyError:
    print('El usuario no está disponible')
    time.sleep(1.2)