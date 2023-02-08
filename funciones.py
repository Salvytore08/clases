def rec(
    a:float,
    b:float
) -> float:
    """"
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