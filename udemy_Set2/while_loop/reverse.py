# Use a while loop to reverse a given number (e.g., 123 → 321)
n=int(input("Enter a number "))
res_num=0
while n>0:
    last_dig=n%10
    res_num=res_num*10+last_dig
    n//=10
print(res_num) 