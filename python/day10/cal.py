def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        return "Error:division by zero"
    return x/y

def main():
    while True:
        num1,num2=map(float,input("Enter the numbers: ").split())
        operator=input("Enter operatoe (+,-,*,/) or 'q' to quit: ")
        if operator.lower()=='q':
            break
        if operator=='+':
            res=add(num1,num2)
        elif operator=='-':
            res=subtract(num1,num2)

        elif operator=='*':
            res=multiply(num1,num2)
        elif operator=='/':
            res=divide(num1,num2)
        else:
            res="Invalid operator"
        print("Result: ",res)
    
main()

