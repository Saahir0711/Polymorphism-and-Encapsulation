class Square:

    def __init__(self, len_side1, len_side2):
        self.len_side1 = len_side1
        self.len_side2 = len_side2

    def find_area(self):
        return self.len_side1 * self.len_side2
    
class Rectangle(Square):

    def __init__(self, len_side1, len_side2):
        Square.__init__(self, len_side1, len_side2)

class Parallelogram(Rectangle):

    def __init__(self, len_side1, len_side2):
        Rectangle.__init__(self, len_side1, len_side2)

class Triangle(Parallelogram):

    def __init__(self, len_side1, len_side2):
        Parallelogram.__init__(self, len_side1, len_side2)

    def find_area(self):
        return (Parallelogram.find_area())/2
    
class Circle:

    def __init__(self, radius):
        self.radius = radius
        self.__pi = 3.14

    def find_area(self):
        (self.radius * self.radius) * self.__pi

a = Square(5,5)
a.find_area()

b = Rectangle(7,5)
b.find_area()

c = Parallelogram(8,5)
c.find_area() 

d = Triangle(10,5)
d.find_area()

e = Circle(5)
e.find_area()
