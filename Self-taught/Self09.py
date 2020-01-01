class Square:

    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

    def what_am_i(self):
        super().what_am_i()
        print("I am a Square.")
    def __repr__(self):
        return "{}by{}by{}by{}".format(self.s1, self.s1, self.s1, self.s1)
squ1 = Square(50)
print(squ1.calculate_perimeter())
print(squ1)

def fn(x, y):
    return x is y
print(fn(20, 20))
print(fn(20, 21))
