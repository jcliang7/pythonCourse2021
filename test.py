import math as math
class Circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r * self.r
    def circumference(self):
        return 2 * math.pi * self.r


newCircle = Circle(8)
print(newCircle.area())
print(newCircle.circumference())