from ex3 import Shape
    
class Rectangle(Shape):
    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__(x, y)
        self.wi = width
        self.he = height
        
        return
        
    def to_string(self) -> str:
        stx = str(self.x)
        sty = str(self.y)
        
        stwi = str(self.wi)
        sthe = str(self.he)
        
        return print(f'Rectangle: x={stx} , y={sty} , width={stwi}, height={sthe} ')
    
    def area(self) -> float:
            flx = float(self.x)
            fly = float(self.y)
            
            flwi = float(self.wi)
            flhe = float(self.he)
            
            area = flwi * flhe
            
            return area
    
c1 = Rectangle(3.2, -2.2, 3,4)
c1.to_string()
c1.area()
