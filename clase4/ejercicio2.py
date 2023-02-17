dict = {}

def dividir(dict:dict):
    frase = str(input('Por favor ingrese una frase: '))
    a = frase.split(' ')
    dict.update({a[1]:a[1].len()})
    print(dict)
    
dividir(dict)