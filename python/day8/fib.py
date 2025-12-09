'''def fib(n):
    if n<0:
        return "Enter a positive number "
    else:
        a=1
        b=1
        for i in range(2,n):
            c=a+b
            a=b
            b=c
        return c
n=int(input("Enter a number"))
print(fib(n))
'''
def fib(n):
    if n<=0:
        return "Enter a positive number"
    elif(n==1 or n==2):
        return 1
    
    else:
        return fib(n-1)+fib(n-2)
n=int(input("Enter a number"))
print(fib(n))

