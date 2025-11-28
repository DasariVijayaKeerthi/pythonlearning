Str1=input("Enter a string1: ")
Str2=input("Enter string2: ")

if(sorted(Str1.lower())==sorted(Str2.lower())):
    print("String1 and string2 are anagrams")
else:
    print("String1 and String2 are not anagrams")