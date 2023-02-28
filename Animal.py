class Animal:
    def __init__(self, species):
        self.species = species
    def Details(self):
        print("species:", self.species)

class Cat(Animal):
    def __init__(self, species, voice):
        Animal.__init__(self, species)
        self.voice = voice
    def meow(self):
        self.Details()
        print("voice:", self.voice)

class Kitten(Cat):
    def __init__(self, species, voice, baby):
        Cat.__init__(self, species, voice)
        self.baby = baby
    def baby(self):
        self.meow()
        print("baby:", self.baby)

#c = Cat("Cat", "meow")
#c.meow()
#print()

k = Kitten("Cat", "meow", "kitten")
k.baby()
print()

