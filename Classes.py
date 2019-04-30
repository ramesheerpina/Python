class MyClass:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x= MyClass(3.0, -4.5)
print(x.r)
print(x.i)

#simple class
class NewSnake:
    name = "newPython"
print(NewSnake.name)

#class with a method defined in it
class Snake1:
    def change_name(self, name1):
        self.name = name1
snake1 = Snake1()
snake1.change_name("Anaconda")
print(snake1.name)

#__init__can be used to pass attributes at tuntime
class Snake:
    def __init__(self, named):
        self.name = named
python = Snake("Python")
print(python.name)
anaconda = Snake("Anaconda")
print(anaconda.name)

