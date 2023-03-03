class Seres():
    sentidos = ['Olfato','Vista','Tacto','Gusto','Oido']
    
    def __init__(self,nom):
        self.nom = nom
    
    def siento(self):
        print(f'Los sentidos de {self.nom} son {self.sentidos}')
        
    def mover(self):
        print(f'{self.nom} se está moviendo')
        
    def sonidos(self):
        print(f'{self.nom} está haciendo un sonido')
        
        
class persona(Seres):
    def sonidos(self):
        print(f'{self.nom} está hablando')
        
    def mover(self):
        print(f'{self.nom} está caminando')


class gato(Seres):
    def sonidos(self):
        print(f'{self.nom} está maullando')
        
    def mover(self):
        print(f'{self.nom} está escalando una pared')


class perro(Seres):
    def sonidos(self):
        print(f'{self.nom} está ladrando')
        
    def mover(self):
        print(f'{self.nom} está persiguiendo una pelota')
        
        
yo = persona('Salvatore')
yo.mover()
yo.sonidos()
yo.siento()

cat = gato('Hidráulico')
cat.mover()
cat.sonidos()
cat.siento()

dog = perro('Max')
dog.mover()
dog.sonidos()
dog.siento()