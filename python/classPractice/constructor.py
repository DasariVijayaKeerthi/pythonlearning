"""Constructor and Attributes
Create a class 
Person with a constructor (
__init__ ) that accepts 
as arguments and stores them as instance attributes.
Create an object and print the person’s name and age"""
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
obj=Person("John",22)
print(f"Name of the person {obj.name} and age of the person is {obj.age}")