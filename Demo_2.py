import keyword  # package of keyword
print(keyword.kwlist)
print(keyword.iskeyword("a"))
print(keyword.iskeyword("break"))

a=5  # integer
b=4
print(type(a))
print(a)

print(id(a)) # prints location of 'a'
print(a!=b) == print(a is not b)
print(a==b) == print(a is b)

a=(2,7,8,9) #arrays
print(2 in a)
print(5 in a)

