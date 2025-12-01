s1=int(input("Enter the score in subject1: "))
s2=int(input("Enter the score in subject2: "))
s3=int(input("Enter the score in subject3: "))
s4=int(input("Enter the score in subject4: "))
s5=int(input("Enter the score in subject5: "))
s6=int(input("Enter the score in subject6: "))
percentage=(sum([s1,s2,s3,s4,s5,s6])/600)*100
print(percentage)
if(percentage>=33):
    print("the student is passed and grade is ")
    if(percentage>=90):
        print("A+")
    elif(80<=percentage<90):
        print("A")
    elif(70<=percentage<80):
        print("B")
    elif(60<=percentage<70):
        print("C")
    elif(50<=percentage<60):
        print("D")
    else:
        print("E")
else:
    print("The student is failed")