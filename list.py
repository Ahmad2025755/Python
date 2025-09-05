lst = ['Apple' , 'Banana' , 'Pineapple' , 'Strawberry', 'Watermelon']
#        0          1           2              3            4

print("Length:",len(lst))
print("First element:", lst[0])

lst.append('Bannana')
print("Update list:", lst)

lst.remove('Pineapple')
print("Updated list:", lst)

lst.pop(1)
print("Updated list", lst)

lst.reverse()
print("Reversed list:", lst)

lst = lst[0:4]
print("Sliced list:", lst)