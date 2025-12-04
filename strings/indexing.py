lang="python"
print(lang[1])
print(lang[0:2]) 
'''p y t h o n
   0  1 2 3 4 5
   [0:2]-->0:2-1-->0:1'''
print(lang[3:-1])#same as [3:5]
# print(lang[0:6:n])-->skips n-1 characters
# [start:stop:step]
print(lang[0:7:2])#skip 1 character 
print(lang[0:7:1])#skips 0 character

print(lang[:4])#replace start value with 0
print(lang[1:])#replace stop value with len(string).