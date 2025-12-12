class Animal:
    def sound(self):
        print("Some sound")
class Dog(Animal):
    def sound(self):
        print("Bark")
obj=Dog()
obj.sound()
"""
self keyword is used in the method as the first parameter because it refer to the current object.
 and self will be first parameter when we write the method inside the class.
 
"""