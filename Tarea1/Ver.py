import time
try:
    def ver(
        dict:dict
    ):
        """
        Función que permite ver los usuarios de la biblioteca
        
        ~Parámetros~
        dict = Diccionario
        """
        a = str(input('\nPor favor ingrese el usuario que desea ver: '))
        b = a.lower()
        print(f'{b} : {dict[b]}')
        time.sleep(1.2)
        
except ValueError:
    print('Ingrese un nombre válidos')
    print('Los nombres sólo pueden contener palabras')
    time.sleep(1.2)