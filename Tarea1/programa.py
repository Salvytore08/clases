def programa():
    """
        Esta función es la que contiene toda la lógica del programa
    
    """
    import Menú
    import Crear
    import Eliminar
    import Actualizar
    import Ver

    dict = {}

    while True:
        Menú.menu()
        a = int(input('Por favor ingrese la opción que desea: '))
        
        match a:
            case 1: 
                Crear.crear(dict)
            case 2:
                Eliminar.eliminar(dict)
            case 3:
                Actualizar.actualizar(dict)
            case 4:
                Ver.ver(dict)
            case 5:
                print('Puede salir')
                break
