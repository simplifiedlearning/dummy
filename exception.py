#########  EXPECTIONAL HANDLING     ######
#exception is a       that disrupts the normal flow of program
#an exception is python object that represents an error
#two types of errors
#(1)compile time error does not occur in python because python intrepreted language
#(2)run time error
#two keywords in python are TRY And EXCEPT block used to handle runtime errors
#expection hierchy:
#the base class of all expection is
##name error----->
##type error----->
##index error---->it means that if i create a array of size 5 and insert 6 it throws error
##zerodivision error---->divide by zero error
##all the expections are dervied from the base class expection
##suspcisous code(one which might throw error) should be put in try block
####ZERODIVISION ERROR
"""try:
    a=int(input("enter the value of a "))
    b=int(input("enter the value of b "))
    c=a/b
    print("the value of c",c)
except ZeroDivisionError:
    print("error:please provide correct value for b")
print("hey")#to check if the error didnt distrub the normal flow"""
#there can be only one try block but can have multiple expections
"""try:
    a=3
    if a<4:
        b=a/(a-3)
    print("value of b ",d)
except(ZeroDivisionError,TypeError):
    print("error occured")"""
####INDEX ERROR
"""try:
    a=[1,2,3]
    print(a[2])
    print(a[3])
except IndexError:
    print("error occured")"""
####NAME ERROR
"""d=a-b
try:
    a=3
    if a<4:
        b=a/(a-3)
    print("value of b ",d)
except(NameError):
    print("error occured")"""
####TYPE ERROR
"""try:
    a="abc"
    if a<4:
        b=a/(a-3)
    print("value of b ",d)
except(TypeError):
    print("error occured")"""

####ASSERTION ERROR
try:
    n=int(input("enter the value of n:")
    assert n>=2 and n<=5
    print("THE number is ",n)
except AssertionError:
    print("Assertion error occured")
#finally keyword---->finally block is excuted whether or not the expection occurs
#sometimes there is need to close file which remains opened due to some processing in such cases finally used
#forcefully close the irrespective of whatever happens

################# PROGRAM TO DEMONSTRATE THE ERRORS #####

