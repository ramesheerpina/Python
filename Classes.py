class MyClass:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x= MyClass(3.0, -4.5)
print(x.r)
print(x.i)

class Snake:
    def __init__(self, name):
        self.name = name
python = Snake("Python")
print(python.name)

class NewSnake:
    name = "newPython"
print(NewSnake.name)