n=int(input("Enter the number to get its multiplies"))
n1=int(input("Enter the how number of the multiplies you need"))
for i in range(1,n1+1):
    print(str(n) +" * "+str(i)+"=",n*i)
    #print(n,"*",i,"=",n*i) The above statement can be write as this also and ,(comma) by default prints the space
    #To do word wrap go to view-->word wrap
    #for loop is used when we knew the extact number the loop should iterate
    #While loop is used when the number of iterations are not known and checks if specific conditions meet or not
    