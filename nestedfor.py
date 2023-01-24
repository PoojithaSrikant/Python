list1=["Moolya","Pooji","python","project","learn"]
for x in list1:
    for y in x:
        print(y) #prints the list of strings in line

str1="Poojitha"
for z in str1:
    print(z) #prints the string in line

list2= [["a","b","c"],["d","e"]]
for t in list2:
    for q in t:
        print(q)

list3=[['india','delhi'],['usa','new jersy'],['canada','vancouver']]
#my country name is +country+ and i live in +city
#for a in list3:
   # print(a)
for b,c in list3:
        print("My country is" +b+ "and I live in" +c)

dic1= dict(list3)
print(dic1)
for a,b in dic1.items():
    print(a,b)
list4=["United States","Mumbai","Losangles","Boston"]
set1=set(list4)
print(set1)
tuple1=tuple(list4)
print(tuple1)
tuple2=tuple(list3)
print(tuple2)
