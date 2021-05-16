#1
def a():
    return 5
print(a()) #will print 5

#2
def a():
    return 5
print(a()+a()) #will print 10

#3
def a():
    return 5
    return 10
print(a()) #will print 5

#4
def a():
    return 5
    print(10)
print(a()) #it will print 5 in the return and ignore the print(10)

#5
def a():
    print(5)
x = a()
print(x)# it will print 5 

#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3)) # it will print 3 then it will print 5 then it will print 8 

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5)) #it will print 25 , the str convert the number to strings

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a()) # syntax error

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))#it will print 7
print(a(5,3))# it will print 14
print(a(2,3) + a(5,3)) # it will print 7

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5)) # it will print 8 and ignor the second return

#11
b = 500
print(b)# this will print 500
def a():
    b = 300
    print(b) # this will print 300 and change the b value , its global
print(b)#this will print 300
a()#this will print 300 when the function called
print(b)#this will print 300


#12
b = 500
print(b) # this will print 500
def a():
    b = 300
    print(b)#this will print 300
    return b # this will return 300
print(b) #this will print 300
a() # this will print 300 and return 300
print(b)# this will print 300

#13
b = 500
print(b) #this will print 500
def a():
    b = 300
    print(b)#this will print 300
    return b #this will return 300
print(b)#this will print 300
b=a()
print(b)#this will print 300 and return 300

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a() # will print 1 then 3 then 2

#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)# this will print 1 then 3 and return 5 and print 5 then stop










