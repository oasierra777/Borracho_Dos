import random
from secrets import choice

class Borracho:
    
    def __init__(self, nombre):
        self.nombre = nombre
        
class BorrachoTradicional(Borracho):
    
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def camina(self):
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
    
class BorrachoMuyModerado(Borracho):
    
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def camina(self):
        return.choice([(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)])
    
class BorrachoDerecha(Borracho):
    
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def camina(self):
        return random.choice([(0, 4), (0, -1), (4, 0), (1, 0)])