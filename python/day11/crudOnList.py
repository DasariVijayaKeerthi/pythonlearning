"""This module perform CRUD operations on the list"""
# Create(Add elements)
my_list=[1,2,3]
# add at the end of the list
my_list.append(4)
print(my_list)

# Read(Access elements)
print(f"element at index 3 is {my_list[3]}")

# Update elements in list
my_list[2]=100
print(my_list)

# delete(remove elements)
my_list.remove(100)
print(my_list)
