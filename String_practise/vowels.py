# Write a program that counts how many vowels are in a given string.
str=input("Enter a string ")
count=0

for i in str.lower():
    if i in ['a', 'e' , 'i' , 'o' , 'u']:
        count+=1
print(count)

