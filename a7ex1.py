import math

class Complex():
    def __init__(self, real: float, imaginary: float):
        self.re = real
        self.im = imaginary
                
    def print(self):
        
        if self.im >= 0:
            st = print(f'{self.re} + {abs(self.im)}i')
            return st
        else:
            st = print(f'{self.re} - {abs(self.im)}i')
            return st
        
    def abs(self) -> float:
        
        return math.sqrt(pow(self.re,2)+pow(self.im,2)) 
    
c1 = Complex(1.2, -5.4)
c1.print()
c2 = Complex(3.0, 4.0)
c2.print()
print(c2.abs())
