class Animal:
    def __init__(self, species):
        self.species = species
    def Details(self):
        print("Species:", self.species)

class Cat(Animal):
    def __init__(self, species, voice):
        Animal.__init__(self, species)
        self.voice = voice
    def Meow(self):
        self.Details()
        print("Voice:", self.voice)

class Kitten(Cat):
    def __init__(self, species, voice, baby):
        Cat.__init__(self, species, voice)
        self.baby = baby
    def Baby(self):
        self.Meow()
        print("Baby:", self.baby)

#c = Cat("cat", "meow")
#c.Meow()
#print()

k = Kitten("cat", "meow", "kitten")
k.Baby()
print()

