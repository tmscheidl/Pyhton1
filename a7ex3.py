class Shape:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
        return
        
    def to_string(self) -> str:
        stx = str(self.x)
        sty = str(self.y)
        return print(f'Shape: x={stx} , y={sty}')
    
    def area(self) -> float:
        if self.x != float and self.y != float:
            flx = float(self.x)
            fly = float(self.y)
            
            return flx,fly
        elif self.x == float or self.y == float:
            print(type(self.x))
            print(type(self.y))
            raise NotImplementedError
    
c1 = Shape(3.2, -2.2)
c1.area()
