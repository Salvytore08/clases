class triángulo():
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.lados = [self.a,self.b,self.c]
        
    def mayor(self):
        mayor = max(self.lados)
        print(f'El lado mayor mide {mayor}')
        
    def tipo(self):
        lados = set(self.lados)
        if len(lados) == 3:
            print(f'El triángulo es escaleno')
        
        elif len(lados) == 2:
            print(f'El triángulo es isósceles')
            
        else:
            print(f'El triángulo es equilátero')
            
            
triangle = triángulo(20,20,20)
triangle.mayor()
triangle.tipo()