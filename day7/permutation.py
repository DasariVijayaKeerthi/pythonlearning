def permutation(s,path=""):
    if not s:
        print(path)
        return path
    for i in range(len(s)):
        permutation(s[:i]+s[i+1:],path+s[i])
s=input("Enter a string ")
print(permutation(s))