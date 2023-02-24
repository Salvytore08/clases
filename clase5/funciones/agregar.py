import datetime

def agregar(dict:dict) -> dict:
    nombre = str(input('Por favor ingrese su nombre: '))
    libro = str(input('Por favor ingrese el libro que desea pedir: '))
    fecha = input('Por favor ingrese la fecha del préstamo: ')
    
    dict.update({nombre:{'libro':libro,'fecha':fecha}})
       
