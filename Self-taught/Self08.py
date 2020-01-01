class Rectangle:
    def __init__(self, w, l):
        self.w = w
        self.l = l


    def calculate_perimeter(self):
        return self.w * 2 + self.l * 2

class Square:
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

    def change_size(self, new_size):
        self.s1 += new_size

a_re = Rectangle(25, 50)
a_sq = Square(20)

print(a_re.calculate_perimeter())
print(a_sq.calculate_perimeter())
a_sq.change_size(-10)
print(a_sq.calculate_perimeter())

class Horse:
    def __init__(self, name, r):
        self.name = name
        self.r = r

class Rider:
    def __init__(self, name):
        self.name = name

rider = Rider("俺")
horse = Horse("小城", rider)
print(horse.r.name)
print(horse.name)
