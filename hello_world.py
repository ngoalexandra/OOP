def a():
    return 5
print(a())  
# prints 5

def a():
    return 5
print(a()+a())     
# prints 10

def a():
    return 5
    return 10
print(a())     
# prints 5, 10 . I compared it to when I ran it and turns out it only returns the first return. Not both

def a():
    return 5
    print(10)
print(a())    
# it will only return 5, and it will print the 10 if you use the console

def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a)  
# it will only return 10 . 
#  i compared the answers and I was wrong. It won't print anything because of syntax error. We are missing parenthesis when calling function

def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
# returns 14
print(a(5,3))
# returns 7
print(a(2,3) + a(5,3))  
# will return 21 

def a(b,c):
    return b+c
    return 10
print(a(3,5))     
# returns 8

b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)  

# prints 300, 300, 300
#  I compared it and it should print 500,500,300,500

b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b) 
# 500, 500, 300, 500

b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)
# 500, 500, 300, 300




