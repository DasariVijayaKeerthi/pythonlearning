# Take a user input string and check if it is a palindrome (same forwards and backwards).
str=input("enter the string to cjeck whether it is palindrome or not " )
if(str==str[::-1]):
    print("It is palindrome")
else:
    print("  It is not a palindrom")