#Bitwise Operator Tasks

#1. Create two variables a = 10 and b = 6. Print the result of a & b.

a = 10
b = 6
print(a&b)

'''
2
'''

#2. Create two variables x = 12 and y = 5. Print the result of x | y.

x = 12
y = 5
print(x|y)

'''
13
'''

#3. Create a variable num = 8. Print the result of ~num.

num = 8
print(~num)

'''
-9
'''

#4. Create two variables a = 15 and b = 9. Print the result of a ^ b.

a = 15
b = 9
print(a^b)

'''' 
6 
'''

#5. Create a variable num = 7. Perform left shift by 2 and print the result.

num = 7
print(num << 2)

'''
28    
'''

#6. Create a variable num = 20. Perform right shift by 1 and print the result.

num = 20
print(num >> 1)

'''
10    
'''

#7. Take two numbers from user input and print AND result.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a&b)

'''
Enter first number: 20
Enter second number: 15
4
'''

#8. Take two numbers from user input and print XOR result.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a^b)

'''
Enter first number: 25
Enter second number: 50
16
'''

#String Tasks

#9. Create a string "hi" and print it 4 times using replication.

a = "hi"
print(a * 4)

'''
hihihihi
'''

#10. Create a string "python" and print it 3 times.

text = "python"
print(text * 3)

'''
pythonpythonpython
'''

#11. Create two strings "super" and "man" and combine them using + operator.

a = "super"
b = "man"
print(a + b)

'''
superman
'''

#12. Create three strings "hello", " ", "world" and print "hello world".

x = "hello"
y = " "
z = "world"
print(x+y+z)

'''
hello world
'''

#13. Take a name from user input and print it 5 times.

name = input("Enter your name: ")
print(name*5)

'''
Enter your name: John
JohnJohnJohnJohnJohn
'''

#14. Take two strings from user input and concatenate them.

a = input("Enter first word: ")
b = input("Enter second word: ")
print(a+b)

'''
Enter first word: ice
Enter second word: cream
icecream
'''

# Input & Type Casting Tasks

#15. Take a name from user input and print its data type.

name = input("Enter your name: ")
print(type(name))

'''
Enter your name: Jim
<class 'str'>
'''

#16. Take age from user input and convert it into integer.

age = input("Enter your age: ")
print(int(age))

'''
Enter your age: 24
24
'''

#17. Take two numbers from user input and print their sum.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum:", num1 + num2)

'''
Enter first number: 22
Enter second number: 26
Sum: 48
'''

#18. Take two marks from user input and print their average.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
avg = (num1 + num2) / 2
print("Average:", avg)

'''
Enter first number: 100
Enter second number: 200
Average: 150.0
'''

#19. Take two numbers from user input and print 3*a*2 + b - 2.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(3*a*2 + b - 2)

'''
Enter first number: 3
Enter second number: 6
22
'''

#20. Take a number from user input and print its data type before and after type casting.

num = input("Enter a number: ")
print("before type casting:",type(num))
num = int(num)
print("after type casting:",type(num))

'''
Enter a number: 200
before type casting: <class 'str'>
after type casting: <class 'int'>
'''

#Unit Digit Tasks

#21. Take a number as string input and print the last digit.

num = input("Enter a number: ")
print(num[-1])

'''
Enter a number: 105
5
'''

#22. Take a number and print the unit digit using % operator.

num = 2008
num = num%10
print(num)

'''
8
'''

#23. Take a number and remove the last digit using // operator

num = 123
num = num//10
print(num)

'''
12
'''

#24. Take a number and print the second last digit.

num = 1258
str_num = str(num)
print(str_num[-2])

'''
5
'''

#25. Take a 5 digit number and print its last digit.

num = 50235
num = num % 10
print(num)

'''
5
'''

#If Statement Tasks

#26. Create a program that checks if 10 ≥ 5 and prints a message.

if 10 >= 5:
    print("Yes 10 is greater than and equal to 5")

'''
Yes 10 is greater than and equal to 5
'''

#27. Take a number from user input and check if it is greater than 50.

num = int(input("Enter a number: "))
if num>50:
    print("Yes given number is greater than 50")

'''
Enter a number: 88
Yes given number is greater than 50
'''

#28. Take age from user input and check if age ≥ 18.

age = int(input("Enter your age: "))
if age>=18:
    print("You are eligible")

'''
Enter your age: 22
You are eligible
'''

#29. Take a number and check if it is greater than 100.

num = 200
if num>100:
    print("Number is greater than 100")

'''
Number is greater than 100
'''

#30. Take a number and check if number ≥ 0.

num = 25
if num>=0:
    print("Yes")

'''
Yes
'''

#If-Else Tasks

#31. Take a number and check if it is even or odd.

num = 26
if num%2==0:
    print("Even")
else:
    print("Odd")

'''
Even
'''

#32. Take marks from user input and check if pass or fail (pass ≥ 35).

marks = int(input("Enter your marks: "))
if marks >= 35:
    print("Pass")
else:
    print("Fail")

'''
Enter your marks: 96
Pass
'''

#33. Take a number and check if it is positive or negative.

num = -10
if num > 0:
    print("Positive")
else:
    print("Negative")

'''
Negative
'''

#34. Take a number and check if it is greater than 10 or not.

num = 7
if num > 10:
    print("Greater than 10")
else:
    print("Not greater than 10")

'''
Not greater than 10
'''

#Nested If Tasks

#35. Create a program for job eligibility

age = int(input("Enter your age: "))
height = int(input("Enter your height: "))
weight = int(input("Enter your weight: "))

if age >= 18:
    if height >= 160:
        if weight >= 60:
            print("Selected")
        else:
            print("Rejected")
    else:
        print("Rejected")
else:
    print("Rejected")

'''
Enter your age: 18
Enter your height: 165
Enter your weight: 58
Rejected
'''

#36. Create a college admission program

marks = int(input("Enter your marks: "))
age = int(input("Enter your age: "))
if marks >= 60:
    if age >= 17:
        print("Admission Available")
    else:
        print("Rejected")
else:
    print("Rejected")

'''
Enter your marks: 80
Enter your age: 18
Admission Available
'''

#37. Create a sports selection program

age = int(input("Enter your age: "))
height = int(input("Enter your height: "))
weight = int(input("Enter your weight: "))

if age >= 16:
    if height >= 150:
        if weight >= 50:
            print("Selected")
    else:
        print("Rejected")
else:
    print("Rejected")

'''
Enter your age: 20
Enter your height: 162
Enter your weight: 55
Selected
'''

#Match Statement Tasks

#38. Take a number (1-7) and print day name using match.

num = 7
match num:
    case 1: print("Monday")
    case 2: print("Tuesday")
    case 3: print("Wednesday")
    case 4: print("Thursday")
    case 5: print("Friday")
    case 6: print("Saturday")
    case 7: print("Sunday")

'''
Sunday
'''

#39. Take a number (1-3) and print

num = 3
match num:
    case 1: print("Red")
    case 2: print("Blue")
    case 3: print("Green")

'''
Green
'''

#40. Take a number (1-4) and print

num = 2
match num:
    case 1: print("Apple")
    case 2: print("Mango")
    case 3: print("Orange")
    case 4: print("Banana")

'''
Mango
'''
