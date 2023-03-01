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
        
robo = robot('robo', 0,0)

robo.subir(2)
robo.ver()
robo.bajar(5)
robo.ver()
robo.izquier(2)
robo.ver()
robo.dere(5)
robo.ver()