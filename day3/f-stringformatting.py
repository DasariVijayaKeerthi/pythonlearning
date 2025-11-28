user_input=input("enter a string: ")
print(f"f-string formatting {user_input}.")
name="keerthi"
emp_id=2430304
print(f"Hi I am {name} and my emp_id is {emp_id}.")
a=int(input("enter value of a= "))
b=int(input("enter value of b= "))

#temp="Sum of two number a={a} and b={b} is:{}"
# s1=temp.format(a,b,a+b)
# print(s1)

#using f-format
print(f"sum of a={a} and b={b} is:",a+b)