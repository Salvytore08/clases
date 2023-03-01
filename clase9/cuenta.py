diccionario = {}
class cuenta(): 
    
    def nuevo(self,dict):
        a = input('Ingrese el nombre del usuario que desea agregar: ')
        b = input('Ingrese el dinero que tiene en su cuenta: ')
        dict[a] = b
        
    def eliminar(self,dict):
        x = input('Por favor ingrese el usuario que desea eliminar: ')
        dict.pop(x)
        
    def ver(self,dict):
       for i,j in dict.items():
           print(f'{i} : {j}')
           
Yo = cuenta()
Yo.nuevo(diccionario)
Yo.ver(diccionario)
Yo.eliminar(diccionario)
Yo.ver(diccionario)