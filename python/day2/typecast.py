
a=34
print(type(a))

b="34"
print(type(b))

# converting b into an Integer
c=int(b)
print(type(c))
print(id(a)==id(c))

d=str(a)
print(type(d))
print(id(d),id(b))

f=float(a)
bo1=bool(a)
k=0
bo=bool(k)
print(f"{f},{bo1},{bo},type of f {type(f)},type of bo1 {type(bo1)},type of bo1 {type(bo1)}")
