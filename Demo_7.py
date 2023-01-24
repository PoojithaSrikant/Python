#list
l1=[13,'pooji',1994,True]
print(l1[0])
print(l1[3])

#   0    1     2     3     4  5
l2=[10,'pooji',10,'pooji',10,90]
print(l2[3])
print("Number of times pooji is repeated:")
print(l2.count('pooji'))

print(l2[0:5:4])
l2.remove('pooji')
l2.remove('pooji')
print(l2)


#-----------------------

l3=[1,2,3,4,5,6,7,8,9]
print(l3[0:10:3])
l2.append('srikant')
print(l3)
l3.insert(0,'pooji')
print(l3)

#------------------------

l4=['Pooji','juhi','srikant','moolya']
l4.sort()# sorting in alphabetical order
print(l4)

#-------------------

l5=[25,45,88,75,65,55,21]
l5.sort(reverse=True)#sorting in reverse (descending) order
print(l5)

l5.pop()# last value will be deleted
print(l5)

