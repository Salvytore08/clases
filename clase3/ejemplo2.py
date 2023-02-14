estudiantes = []
profesores = []

while True:
    def menú():
        print('MENÚ'.title())
        print('1. Añadir')
        print('2. Eliminar')
        print('3. Ver')
        print('4. Salir')

    def añadir(lista):
        a = str(input('Por favor ingrese la persona que desea añadir: '))
        lista.append(a)     
        
    def eliminar(lista):
        a = str(input('Por favor ingrese la persona que desea eliminar: '))
        lista.remove(a)
        
    def ver(lista):
        print(lista)
        
    print('Por favor ingrese una de las siguientes opciones numéricas:')
    menú()
    a = int(input('> '))
    
    match a:
        case 1:
            a = str(input('¿Desea añadir un profesor o un estudiante?: '))
            if a == 'profesor':
                añadir(profesores)
            elif a == 'estudiante':
                añadir(estudiantes)
            else:
                print('Ingrese una opción correcta')
            
        case 2:
            a = str(input('¿Desea eliminar un profesor o un estudiante?: '))
            if a == 'profesor':
                eliminar(profesores)
            elif a == 'estudiante':
                eliminar(estudiantes)
            else:
                print('Ingrese una opción correcta')
        case 3:
            a = str(input('¿Desea ver los profesores o los estudiantes?: '))
            if a == 'profesor':
                ver(profesores)
            elif a == 'estudiante':
                ver(estudiantes)
            else:
                print('Ingrese una opción correcta')