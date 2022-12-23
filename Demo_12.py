#Mapping the lists using zip function
a=[1,2,3,4,5,6,7,]
b=[100,200,300,400,500,600,700]
c=zip(a,b)#mapping the set of list together
#print(list(c))
#print(c)#it will return zip object

#tuples using zip
t1=(10,20,30,40,)
t2=("puji","sri","juhi")
z=zip(t1,t2)
#print(tuple(z))

for x,y in c:
    print(x,y)

#finding profit using zip
cp=(25,65,66,77,88)
sp=(56,18,70,100,99)
z=zip(cp,sp)

for x,y in z:
    if(y>x):
        z=x-y
        print("profit",y-x)
    elif(x>y):
        z=y-x
        print("loss",x-y)


