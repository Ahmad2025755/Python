my_dict = {}

my_dict = {1: "Apple", 2: "Ball"}


my_dict = {'name': 'John',1: [2,3,4]}

my_dict = {'name': 'John', 'age': 26}


print(my_dict['name'])
print(my_dict.get('age'))

my_dict['age'] = 27
print(my_dict)

my_dict["Address"] = "Downtown"
print(my_dict)

my_dict.pop('age')
print(my_dict)

print("Address", my_dict.get("Address"))

my_dict.clear()
print(my_dict)