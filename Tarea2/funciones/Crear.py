import time 
try:
    def crear(
        dict:dict
    ):
        """
        Función que permite agregar usuarios a la biblioteca
        
        ~Parámetros~
        dict = Diccionario
        """
        nom = str(input('\nPor favor ingrese su nombre: '))
        lib = str(input('Por favor ingrese el libro que desea pedir: '))  
        fecha = (input('Por favor ingrese la fecha: '))  
        
        diccionario_interno = {
        "libro": lib,
        "fecha": fecha 
        }
        
        dict[nom].append(diccionario_interno)
        
        return dict
    
    
    
except ValueError:
    print('Por favor ingrese un nombre/libro válido')
    print('Los nombres sólo pueden contener palabras')
    print('Los libros sólo pueden contener palabras')
    time.sleep(1.2)