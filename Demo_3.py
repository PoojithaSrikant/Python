a=2
print(a ** 3)

#precidance of operator
print(5-8+2)

#String Manupulation
str1 = "moolya"
print(len(str1))
print(str1[4])
b = 3456
print (str(b))
c= 1234
print(type(c))

#operations in strings
#find()
print(str1.find("l"))
print(str1.find("z"))
print(str1.upper()) #change to upper case
print(str1) #prints actual string coz immutable
print(str1.count("o")) #index count
print(str1.isupper()) #checking case

#Remove strip/space
str2= "  hello  "
print(str2)
print(str2.strip())
z= " visakhapatnam "
print(z)
print(z.replace("a","b").upper()) #replaces char and converts to uppercase
print(z.lstrip()) #trims space from the leftside of the string
print(z.rstrip()) #trims rightside space of string

#Replace()
str4= "I am Indian"
print(str4.replace("I am Indian","We are Indians"))

#Split operation()
str5="Selenium is a free open-source automated testing framework used to validate web applications across different browsers and platforms"
print(str5.split()) #it will divide according to the space(char) provided b/w them
print(str5.split("a")) # it will splits the word bfore "a" and after "a" aside (w.r.t reference word)
print(str5.split("testing"))

#Escape Character
str6="poojitha\" srikant" # "\" escape char
print(str6)

#For multiple line strings(b/w thrible quotes anything we write)
z="""
jiyanshi
She is my lifeline
I love her a lot
"""
print(z)
print('is' in z)

#Reverse Character
y="""
india
tiger
peacock
vande matharam
"""
print(y)
print(y[::-1]) #prints the string and order of string back to front (reverse)


