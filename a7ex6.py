from ex4 import Rectangle

class Square(Rectangle):
    def __init__(self, x: int, y: int, length: int):
        super().__init__(x,y, width, height)
        self.le = length
        
        return
        
    def to_string(self) -> str:
        stx = str(self.x)
        sty = str(self.y)
        
        stle = str(self.le)
        
        return print(f'Square: x={stx} , y={sty} , width={stle}, height={stle} ')
    
    def area(self) -> float:
            flx = float(self.x)
            fly = float(self.y)
            
            flle = float(self.le)
            
            area = flle * flle
            
            return area
    
c1 = Square(3.2, -2.2, 3.4)
c1.to_string()
c1.area()
