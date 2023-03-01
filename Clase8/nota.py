class alumno():
    def __init__(self,nombre, nota):
        self.nota = nota
        self.nom = nombre
        
    def pasar(self):
        if self.nota > 60:
            print(f'{self.nom} pasó con {self.nota}')
        else:
            print(f'{self.nom} no pasó con {self.nota}')
        
x = int(input('Por favor ingrese su nota: '))
yo = alumno('Salvatore', x)

yo.pasar()