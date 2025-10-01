class  CSStudent:

    #Class variables
    stream  = "cse"

    #The init method or constructor
    def __init__(self, roll):

    #Instance variables
     self.roll = roll
    def setAdress(self, address):
        self.address = address


    #Retrieves instance variable

    def getAdress(self):
      return self.address
    

add = CSStudent(101)
add.setAdress("Pune , Maharashtra")
print(add.getAdress())


a = CSStudent(101)


print(a.stream)
print(a.roll)



print(CSStudent.stream)