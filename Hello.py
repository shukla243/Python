class Hw:
    def __init__(self,hello):
        self.hello = hello

    def say(self):
        print(self.hello + " World")

h = Hw("Hello")
h.say()
