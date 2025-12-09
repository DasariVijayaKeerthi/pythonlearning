"""In the module we perform merging two dictionaries and sum the common keys"""
d1={'a':10,'b':20,'c':5}
d2={'b':3,'c':7,'d':9}
res={}
# Iterate over the union of keys from both dictionaries
for i in d1.keys() | d2.keys():
    # use get() method
    res[i]=d1.get(i,0)+d2.get(i,0)
print(res)