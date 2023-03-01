class carro():
    def __init__(self,matrícula,marca,kilómetros,gasolina):
        self.matrícula = matrícula
        self.marca = marca
        self.kilómetros = kilómetros
        self.gasolina = gasolina
        
    def avanzar(self,km):
        self.gasolina = self.gasolina - km
        self.kilómetros = self.kilómetros + km
        
        if self.gasolina <= 0:
            print('Te has quedado sin gasolina')
        else:
            print(f'Tienes {self.gasolina} galones de gasolina')
        
Salvatore = carro("SDS548", "Ferrari", 10, 40)
Salvatore.avanzar(50)

print(Salvatore.kilómetros)
        
