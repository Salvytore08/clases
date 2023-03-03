class robot():
    def __init__(self,nombre, x = 0,y = 0):
        self.x = x
        self.y = y
        self.nom = nombre
        
    def subir(self,subir):
        self.y = self.y + subir
        
    def bajar(self,bajar):
        self.y = self.y - bajar
        
    def izquier(self,izquier):
        self.x = self.x - izquier
        
    def dere(self,dere):
        self.x = self.x + dere
        
    def ver(self):
        print(f'{self.nom} se encuentra en el punto {self.x},{self.y}')
        
        
class robo1(robot):
    def subir(self,subir):
        self.y = self.y + subir 
        
    def bajar(self,bajar):
        self.y = self.y - bajar 
        
    def izquier(self,izquier):
        self.x = self.x - izquier 
        
    def dere(self,dere):
        self.x = self.x + dere 
        


class robo2(robot):
    def subir(self,subir):
        self.y = self.y + subir + 1
        
    def bajar(self,bajar):
        self.y = self.y - bajar - 1
        
    def izquier(self,izquier):
        self.x = self.x - izquier - 1
        
    def dere(self,dere):
        self.x = self.x + dere + 1


class robo3(robot):
    def subir(self,subir):
        self.y = self.y + subir + 2
        
    def bajar(self,bajar):
        self.y = self.y - bajar - 2
        
    def izquier(self,izquier):
        self.x = self.x - izquier - 2
        
    def dere(self,dere):
        self.x = self.x + dere + 2
        
        
yo = robo1('Salvatore')
yo.subir(5)
yo.ver()
yo.bajar(3)
yo.ver()
yo.izquier(2)
yo.ver()
yo.dere(5)
yo.ver()

print('\n')

yo2 = robo2('Salvatore')
yo2.subir(5)
yo2.ver()
yo2.bajar(3)
yo2.ver()
yo2.izquier(2)
yo2.ver()
yo2.dere(5)
yo2.ver()

print('\n')

yo3 = robo3('Salvatore')
yo3.subir(5)
yo3.ver()
yo3.bajar(3)
yo3.ver()
yo3.izquier(2)
yo3.ver()
yo3.dere(5)
yo3.ver()

print('\n')