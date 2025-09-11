from abc import ABC ,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 22/7*self.radius*self.radius
rec=Rectangle(4,3)
cir=Circle(6)
print(rec.area())
print(cir.area())
