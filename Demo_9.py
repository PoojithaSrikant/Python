#Rightangledtriangle
print("*")
print("*","*")
print("*","*","*")

#dictionary
a={"URL1":"google.com","URL2":"amazon.in"} #key and value of the key
b={1:"Poojitha",2:"Srikant"}
print(b[1])
print(a["URL1"])
b[3]="Jiyanshi"#dictionary can be increased by adding items more
print(b)
#print(b[4])
print(b.get(1)) #get method for accessing key
print(b.keys()) #no of keys in (b)
print(b.items())#keys and values come in the form of tuples
print(b.values())#only the values will come
print(b.pop(1))#for removing key
print(b.keys())
print(b.popitem())#for deleting last value
print(b.keys())
b.update({3:"demoqa.com",4:"orangehrm.com"})#updating keys and values
print(b)
b.setdefault(5,"youtube.com")#for update the keys and values (another method)
print(b)
b.clear()
print(b)


