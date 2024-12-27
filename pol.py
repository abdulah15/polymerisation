class dog:
    def __init__(self,sound):
        self. sound=sound
    def display(self):
        print("The dog", self. sound)
class cat:
    def __init__(self,sound):
        self.sound=sound
    def display(self):
        print("The cat", self. sound)
class lion:
    def __init__(self,sound):
        self.sound=sound
    def display(self):
        print("The lion", self. sound)

objdog=dog("barks")
objcat=cat ("meow")
objlion=lion("roar")
for i in (objdog, objcat, objlion):
    i. display()