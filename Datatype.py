name = "Robert"  #String
age  = "15"  #Integers
is_student = True #Booleans
weight = 38.5  #Float


print("Name: ", name)
print("DataType of name is", type(name))
print("Age:", age )
print("DataType of age is", type(age))


print("Before type casting.....")
print(age)
print(type(age))
print()


print("After type casting.....")
age = str(age)  #Type Casting
print(age)
print("DataType of age is",  type(age))