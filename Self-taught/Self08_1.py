class Shape:
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2
class Square(Shape):
    square_list = []
    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self)

    def calculate_perimeter(self):
        return self.s1 * 4

are1 = Rectangle(20,50)
asq1 = Square(29)

are1.what_am_i()
asq1.what_am_i()

print(Square.square_list
asq2 = Square(93)
print(Square.square_list
