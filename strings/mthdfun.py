# name=" vijaya keerthi "#Strings are immutable
# #name[2]="E"
# '''name[2]="E"
#     ~~~~^^^
# TypeError: 'str' object does not support item assignment'''
# '''print(len(name))
# print(name.upper())
# print(name.capitalize())#convert first character as capatial
# print(name.lower())
# print(name.title())'''

# #strip- removing whitespace(whitespace can be blank,new line,or tab)
# print(name.strip())
# print(name.lstrip())
# print(name.rstrip())

# s="\n hello world \n"
# print(s.strip())
# print(s.lstrip())
# print(s.rstrip())

# #Finding and replace
s="pythonisfun"

# print(s.find("fun"))#return index where it start
# print(s.replace("fun","awesome"))

# string properties-return boolean values
print(s.isalnum())#returns true if the string contains only alpha or only number or both 
print(s.isalpha())
print(s.isdigit())
print(s.isspace())

s1="a"
print(ord(s1))