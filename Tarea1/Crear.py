def crear(
    dict:dict
):
    """
    Función que permite agregar usuarios a la biblioteca
    
    ~Parámetros~
     dict = Diccionario
    """
    nom = str(input('Por favor ingrese su nombre: '))
    lib = str(input('Por favor ingrese el libro que desea pedir: '))
    dict.update({nom:lib})