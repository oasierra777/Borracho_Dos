import random
from secrets import choice
from tkinter.tix import Y_REGION

class Borracho:
    
    def __init__(self, nombre, x=0, y=0):
        self.nombre = nombre
        self.x = x
        self.y = y
        
    def posicion(self):
        return (self.x, self.y)
    
    def distancia_origen(self):
        return (self.x**2 + self.y**2)**0.5
        
class BorrachoTradicional(Borracho):
    
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def camina(self):
        dx, dy = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        self.x += dx
        self.y += dy
        return [dx, dy]

class BorrachoMuyModerado(Borracho):
    
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def camina(self):
        dx, dy = random.choice([(0, 2), (0, -2), (2, 0), (-2, 0)])
        self.x += dx
        self.y += dy
        return [dx, dy]
class BorrachoDerecha(Borracho):
    
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def camina(self):
        dx, dy = random.choice([(0, 5), (0, -1), (1, 0), (-1, 0)])
        self.x += dx
        self.y += dy
        return [dx, dy]