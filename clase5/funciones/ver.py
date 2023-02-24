
def ver(dict:dict) -> dict:
    a = 0
    for i in dict:
        a += 1
        print(f'{a}. {i}')
    num = str(input('Por favor ingrese del usuario que desea ver: '))
    print(num)
    
    for i in dict['Salvatore']:
       print(i, ':', dict[i])