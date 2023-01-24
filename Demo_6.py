#set - It is unordered,does not accept repetitive values

s={10,20,30,40,50,60,'k'}
print(s)
print(len(s))
s.add('pooji')
print(s)
s.pop()
print(s)


#-------------------

a={1,2,3,4,5}
b={6,7,8,9,6}
z=a.union(b) #prints elements of a and b
print(z)

z1=a.symmetric_difference(b) # prints a-b
print(z1)

c={6,7}
print(c.issubset((b))) #checks whether the elements of 'c' is matches elements of 'b'


