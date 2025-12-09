def fact(n):
    if(n<0):
        return "enter the number greater than zero"
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter a number"))
print(fact(n))
