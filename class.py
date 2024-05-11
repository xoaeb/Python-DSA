class Cookie:
    def __init__(
        self,
        color,
    ):
        self.color = color

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color


cookie1 = Cookie("green")
cookie2 = Cookie("red")
print(cookie1.getColor())
print(cookie2.getColor())

cookie1.setColor("black")

print("new cookie 1 is", cookie1.getColor())


class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f"{self.name} says Woof!")


# Creating an instance of the Dog class
my_dog = Dog("Buddy")

# Calling the bark method on the instance
my_dog.bark()

class Laptop:
    def __init__(self, name):
        self.name = name
        
    def specs(self, processorName, refreshRate):
        print(f"Processor in {self.name} is {processorName} and screen refresh is at {refreshRate}")
        
    def games(self, g1, g2, g3):
        print(f"{self.name} can play games like {g1}, {g2}, {g3} etc.")


myLaptop = Laptop('Dell')
myLaptop.specs('Intel', '120Hz')
myLaptop.games('RDR2', 'Forza', 'WItcher')
