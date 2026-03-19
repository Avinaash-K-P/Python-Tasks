#Task 1 - Print Formatting

print("Hello","World","Welcome","Python",end="\n")
print("Laptop","Mouse","Keyboard",sep="|")

'''
Hello World Welcome Python
Laptop|Mouse|Keyboard
'''

#Task 2 - Variables

name = "Ravi"
age = 22
city = "Chennai"
print(name,age,city,sep="-")

'''
Ravi-22-Chennai
'''

#Task 3 - Multiple Assignment

name = "Meena"
age = 20
student = True

print(name*age*student)

'''
MeenaMeenaMeenaMeenaMeenaMeenaMeenaMeenaMeenaMeenaMeenaMeenaMeenaMeenaMeenaMeenaMeenaMeenaMeenaMeena
'''

#Task 4 - Indexing

word = "Python"

print("First Letter: ", word[0])
print("Third Letter: ", word[2])
print("Last Letter: ", word[5])

'''
First Letter:  P
Third Letter:  t
Last Letter:  n
'''

#Task 5 - Arithemetic Operators

print(25+10)
print(50-20)
print(8*5)
print(100/10)
print(10%3)
print(2**4)
print(20//3)

'''
35
30
40
10.0
1
16
6
'''

#Task 6 - BODMAS Expression

print(3 + 2 * 5 ** 2)

''' 
53 
'''

#Task 7 - Assignment Operator

num = 50
num+= 25
print(num)
num = 100
num/= 10
print(num)

'''
75
10.0
'''

#Task 8 - Comparison Operators

print(10>5)
print(20<15)
print(5==5)
print(10!=8)
print(7>=7)
print(6<=2)

'''
True
False
True
True
True
False
'''

#Task 9 - String Comparison

a = "apple"
b = "Apple"
print(a==b)

'''
False
'''

#Task 10 - Logical Operators

print(10>5 and 5==5)
print(5>10 or 10==10)
print(not(5>2))

'''
True
True
False
'''

#Task 11 - Membership Operator

numbers = [10,20,30,40,50]
print(20 in numbers)
print(60 in numbers)
print(30 not in numbers)

'''
True
False
False
'''

#Task 12 - Swap Variables

a = 10
b = 20
a,b = b,a
print("a =",a)
print("b =",b)

'''
a = 20
b = 10
'''

#Task 13 - Bitwise XOR

a=6
b=3
print(a^b)

'''
5
'''


