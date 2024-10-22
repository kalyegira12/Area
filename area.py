class shape:
    def __init__(self, type, side):
        self.type = type
        self.side = side
        print(f"{type}'s Area is, {side}'s side")

class Square(shape):
    def __init__(self, type, side, length):
        super().__init__(type,side)
        self.length = length

    def area(self):    
        print(f"Area = {self.length ** 2}")

square = Square("square", 4, 5)
square.area()    

class rectangle(Square):
    def __init__(self, type, side, length, width):
        super().__init__(type, side, length)
        self.width = width
    def area(self):
        print(f"area = {self.width * self.length}cm")

rectangle = rectangle("recatangle", 4, 5, 6)
rectangle.area()        







        
                