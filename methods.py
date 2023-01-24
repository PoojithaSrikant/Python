"""x,y= 5,10
print(x+y)
a,b = 15,10
print(a+b)"""

def add(x,y):
    print(x+y)
add(12,25)

#pass a string and inside method print the characters of a string

def str1(a):
    print(a)
str1("Jiyanshi")

def char(a):
    for i in a:
        print(i,end='')
def char(a):
    print("method overload")
char("moolya")


#fibanocci series

def fib(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)
fib(15)
