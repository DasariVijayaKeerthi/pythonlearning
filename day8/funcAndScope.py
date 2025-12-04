i=10 #global variable -used across any function
def add(a,b):
    print(a+b+i)
def sub(c,d):
    print(i-c-d)
a=int(input("enter a number"))
b=int(input("enter a number"))
add(a,b)
sub(a,b)
# a,b,c,d are local variables which can be used only within that particular function