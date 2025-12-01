print("Hello world")
a=input("Enter a value")
print(a)

#datatype and typecasting
a=int(input("enter a integer value: "))
b=float(a)
print("variable is type casted from the integer to float",b)

#day3
s1,s2=input().split()
if(sorted(s1)==sorted(s2)):
    print("anagrams")
else:
    print("not anagrams")

#day4
#Arithmetic Expression
res=5+9+8
print(10/3)

#Comparsion Expression
age=int(input("Enter a age: "))
income=int(input("Enter a income: "))
if(age>18):
    print("Eligible for vote")
else:
    print("not eligible")

#Logical expression
if(age>=21 and income>=50000):
    print("admin")
else:
    print("user")

