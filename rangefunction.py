#list1=[1,2,3,4,5,6,7,8,9,10]
#for x in list1:
    #print(x)

for x in range(1,11):
    print(x)
for x in range(51):
    print(x)

#for odd and even numbers
#(1)
for x in range(1,101):
    if x%2==0:
        print(x)
for x in range(1,101):
    if x%2!=0:
        print(x)
#(2)
is_even = []
is_odd = []
for x in range(1,101):
    if x%2==0:
        is_even.append(x)
    if x%2!=0:
        is_odd.append(x)
print(is_even)
print(is_odd)

#(3)
for x in range(2,102,2):#range(start, stop, step)
    print(x,end=' ') #to avoid new line in console
for y in range(1,101,2):
    print(y,end=' ')


#23 table till range10

num=23
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)