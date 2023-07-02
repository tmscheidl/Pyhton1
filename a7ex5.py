from ex3 import Shape

import math

class Circle(Shape):
    def __init__(self, x: int, y: int, radius: int):
        super().__init__(x, y)
        self.ra = radius
        
        return
        
    def to_string(self) -> str:
        stx = str(self.x)
        sty = str(self.y)
        
        stra = str(self.ra)
        
        return print(f'Circle: x={stx} , y={sty} , radius={stra} ')
    
    def area(self) -> float:
            flx = float(self.x)
            fly = float(self.y)
            
            flra = float(self.ra)
            
            area = pow(flra,2) * math.pi
            
            return area
    
c1 = Circle(3.2, -2.2,4)
c1.to_string()
c1.area()
