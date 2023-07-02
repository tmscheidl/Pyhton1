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
    
    def add(self, other: "Complex"):
        
            self.re = self.re + other.re
            self.im = self.im + other.im
             
    def add_all(comp: "Complex", *comps: "Complex") -> "Complex":
        
        result = Complex(comp.re,comp.im)
        
        if all(isinstance(j, complex) for j in comps):
            raise TypeError("This is not  complex number")
        else:
            for i in comps:
                result.re += i.re 
                result.im += i.im
            return result
        
    
c1 = Complex(1.0, -2.0)
c1.print()
c2 = Complex(9., 100.)
c1.add(c2)
c1.print()
c_sum = Complex.add_all(c1, c1, c2, Complex(33.75, -14.25))
c_sum.print()
c1.print()
will_fail = Complex.add_all(100)
