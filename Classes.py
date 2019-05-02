class Rocket:
    def __init__(self, name, distance):
        self.named = name
        self.distanced = distance
    def launch(self):
        return("%s has reached %s" % (self.named, self.distanced))



class MarsRover(Rocket): #inherited from the base class
    def __init__(self, name, distance, maker):
        Rocket.__init__(self, name, distance)
        self.maker = maker

    def get_maker(self):
        return "%s Launched by %s has reached %s" %(self.named, self.maker, self.distanced)

if __name__ == "__main__":
    rockey = Rocket("Apollo", "moon")
    print(rockey.launch())
    x = MarsRover("marsrover", "low earth orbit", "ISRO")
    print(x.get_maker())


# class - composition, uild reltionships between classes through the use of instance variables that are references to other objects

class MarsroverComp():
    def __init__(self, name, distance, maker):
        self.rockey = Rocket(name, distance) # instantiating the base class
        self.maker = maker
    def get_maker(self):
        return "%s Launched 2 by %s has reached %s" % (self.named, self.maker, self.distanced)

if __name__ == "__main__":
    z = MarsroverComp("Mars Rover2", "Beyong Mars", "ISRO2")
    print(rockey.launch())
    print(z.get_maker())