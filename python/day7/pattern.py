#soild square
print("Soild square")
n=int(input("Enter the number of  vertical lines"))
for i in range(0,n):
    for j in range(0,n):
        print("*",end="")
    print()
#triangle
print("Triangle")
for i in range(0,n+1):
    for j in range(0,i):
        print("*",end="")
    print()
print("inverterd right angle triangle")
for i in range(n,0,-1):
    for  j in range(0,i):
        print("*",end="")
    print()
