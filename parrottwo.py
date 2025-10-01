class Parrot: 

    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)
    
#Instiantiate the Parrot class
blu = Parrot("Blu", 10)

#call the instance methods
print(blu.sing("'Happy'"))
print(blu.dance())
