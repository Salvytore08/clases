import math

def dis(
    x1:float,
    x2:float,
    y1:float,
    y2:float
) -> float:
    """
    Función para hallar la distancia entre 2 puntos
    
    ~Parámetros~
    - x1 = x uno
    - x2 = x dos
    - y1 = y uno
    - y2 = y dos
    
    ~math~
    - pow = potencia
    - sqrt = raíz
    - x = (x2-x1) ^ 2
    - y = (y2-y1) ^ 2
    - d = (x+y) ""distancia"
    """
    
    x = math.pow(x2-x1,2)
    y = math.pow(y2-y1,2)
    d = math.sqrt(x+y)
    return d

def rec(
    a:float,
    b:float
) -> float:
    """
    Función que calcula el área de un rectángulo
    
    ~Parámetros~
    - a (float): Altura
    - b (float): Base
    
    ~Return~
    - área (float): Área
    """
    área = a*b
    return área



a = float(input('Por favor ingrese la altura del rectángulo: '))
b = float(input('Por favor ingrese la base del rectángulo: '))

print(f'El área del rectángulo es de {rec(a,b)}')

x1 = float(input('Por favor ingrese x1: '))
x2 = float(input('Por favor ingrese x2: '))  

y1 = float(input('Por favor ingrese y1: '))
y2 = float(input('Por favor ingrese y2: '))

print(f'La distancia es de {dis(x1,x2,y1,y2)}')