# Ask the user to enter a day number (1–7) and print the corresponding day of the week using match case 
n=int(input("Enter the value between 1 to 7"))
match n:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid number")
