''' 1. Using format() , create a sentence:
 "My name is John and I am 25 years old."
 "John" and 25 as variables
 2.DO the same using f-string'''
template="My name is {} and I am {} years old."
print(template.format("John",25))
name=input("enter the name ")
age=int(input("enter the age"))
print(f"My name is {name} and I am {age} years old.")
