import time
try:
    def actualizar(
        dict:dict
    ):
        """
        Función que permite actualizar usuarios de la biblioteca
        
        ~Parámetros~
        dict = Diccionario
        """
        a = str(input('\nPor favor ingrese el nombre del usuario que desea acualizar: '))
        if a.lower() in dict:
            print(f'{a} : {dict[a]}')
            b = str(input('¿Seguro que quiere actualizar el usuario? (Si o No): '))
            if b.lower() == 'si':
                nom = str(input('Por favor ingrese el nuevo nombre: '))
                lib = str(input('Por favor ingrese el nuevo libro que desea pedir: '))
                dict.update({nom:lib})
            else:
                print('Puede salir')
                time.sleep(1.2)
   
except ValueError:
    print('Ingrese un nombre/opción/libro válidos')
    print('Los nombres sólo pueden contener palabras')
    print('Los libros sólo pueden contener palabras')
    print('Las opciones sólo pueden ser si o no')
    time.sleep(1.5)
except KeyError:
    print('El usuario no está disponible')
    time.sleep(1.2)