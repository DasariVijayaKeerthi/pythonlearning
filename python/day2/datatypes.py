#numeric
#integer
a=10
print(type(a),"\n value:",a)
#float
f=10.9
print(type(f),"\n value:",f)
#complex
c=3+2j
print(type(c),"\n value:",c)

print(a+f+c)

#String
str="keerthi"
print(type(str),"\n value:",str)

#Boolean
b=True
print(type(b),"\n value:",b)

#sequence
#list
l=[1,3]
l.append(2)
print(type(l),"\n value:",l)

#tuple
t=(1,2,3)
print(type(t),"\n value:",t)

#set
s={1,2,3}
s.add(23)
print(type(s),"\n value:",s)

#mapping
#dictionary
d={"name":"keerthi","emp_no":2430304}
print(type(d),"\n value:",d)
d["gender"]="f"
print(type(d),"\n value:",d)
print(d.get("name"))