'''Write a program using match case that simulates a simple calculator.
 1.Ask the user for two numbers and an operation (+, -, *, /).
 2. Perform the operation using match case '''
n,n1=map(int,input("Enter two number").split())
operator=input("Enter the operation symbol to be perform on the numbers")
match operator:
    case "+":
        print(n+n1)
    case "-":
        if(n>n1):
            print(n-n1)
        else:
            print(n1-n)
    case "*":
        print(n*n1)
    case "/":
        print(n/n1)