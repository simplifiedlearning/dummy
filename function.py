######################FUNCTIONS####################
#SYNTAX
#using def keyword
#without parameters
def greet():
    print("hello")
greet()
###add two number
#with parameters
def add1(x,y):
    z=x+y
    print(z)
add1(2,3)
####default arguments
def add2(b,c,a=12):
    print(a+b+c)
add2(5,5)
####abritriy arguments it is represented by * it is used when the programmer doesnt know how many arguments
def read(*n):
    for x in n:
        print(x)
read(1,2,3)
#####RECURSION
#Recursion doesnt have loops and do not use loops
#takes a lot of space
"""def fact(n):
    if(n==1):
        return 1
    else:
        return n*fact(n-1)
r=fact(5)
print(r)"""
###
#fact(5)  n!=1 so else statement is excuted
#which gives 5*fact(4) and is not equal to 1
#again 4*fact(3) n!=1
#3*fact(2)  n!=1
#2*fact(1) n==1
#soo returns 5*4*3*2*1=120
##############X RAISED TO Y
"""x=int(input("enter the value of x"))
y=int(input("enter the value of y"))
def xtoy():"""

########WAP TO CHECK NUMBER IS PALINDROME OR NOT#################
"""n=int(input("enter the number"))
r=0
m=n
while(n>0):
       d=n%10
       r=r*10+d
       n=n//10
if(m==r):
      print("its a palindrome")
else:
      print("its not a palindrome")"""
########WAP TO CHECK IF NUMBER IS PRIME OR NOT###################
"""n=int(int("enter the number to be checked\n"))
for i in range(2,n//2):
    if(n%i)==0:
        flag=0
        break
        
if(flag==0):
    print("is not prime number")
else:
    print("prime")"""
####REVERSE USING FUNCTIONS
"""n=int(input("enter the number to be reversed\n"))
def rev(n):
    r=0
    while(n>0):
       d=n%10
       r=r*10+d
       n=n//10
    print(r)
rev(n)"""
      
