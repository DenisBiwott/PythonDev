#Inheritance using super
class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        area =self.length * self.width
        print(area)
class square(rectangle):
    def __init__(self, length):
        super().__init__(length,length)
square1 = square(6)
square1.area() 
