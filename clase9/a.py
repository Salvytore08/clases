class Seres():
    sentidos = ['Olfato','Vista','Tacto','Gusto','Oido']
    
    def __init__(self,nom):
        self.nom = nom
    
    def siento(self):
        print(f'Los sentidos de {self.nom} son {self.sentidos}')
        
    def mover(self):
        print(f'{self.nom} se está moviendo')
        
    def hablar(self):
        print(f'{self.nom} está haciendo un sonido')
        
yo = Seres('Yo')
yo.mover()
yo.hablar()
yo.siento()
