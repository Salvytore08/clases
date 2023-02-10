def programa():
    """
        Esta función es la que contiene toda la lógica del programa
    
    """
    import time
    import Menú
    import Crear
    import Eliminar
    import Actualizar
    import Ver

    dict = {}

    while True:
        Menú.menu()
        a = int(input('Por favor ingrese la opción que desea: '))
        time.sleep(1.2)
        
        match a:
            case 1: 
                Crear.crear(dict)
                time.sleep(1.2)
            case 2:
                Eliminar.eliminar(dict)
                time.sleep(1.2)
            case 3:
                Actualizar.actualizar(dict)
                time.sleep(1.2)
            case 4:
                Ver.ver(dict)
                time.sleep(1.2)
            case 5:
                print('Puede salir')
                break
