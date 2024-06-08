class Rectangle: 
    def __init__(self, length: float, width: float): 
        self.length = length 
        self.width = width 
 
    def area(self) -> float: 
        return self.length * self.width 
 
    def perimeter(self) -> float: 
        return 2 * (self.length + self.width) 
rectangle = Rectangle(8.0, 6.0) 
print(f"Area: {rectangle.area()}") 
print(f"Perimeter: {rectangle.perimeter()}") 