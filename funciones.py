def rec(a,b):
    área = a*b
    return área  

a = float(input('Por favor ingrese la altura del rectángulo: '))
b = float(input('Por favor ingrese la base del rectángulo: '))

print(f'El área del rectángulo es de {rec(a,b)}')