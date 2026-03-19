#Section 1:Loop Basics

#1. Print numbers from 1 to 50 using for loop

for i in range(1,51):
    print(i,end=" ")

'''
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50
'''

#2. Print even numbers from 1 to 100

for i in range(1,101):
    if i%2==0:
        print(i,end=" ")

'''
2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68 70 72 74 76 78 80 82 84 86 88 90 92 94 96 98 100 
'''

#3. Print odd numbers from 1 to 100

for i in range(1,101):
    if i%2!=0:
        print(i,end=" ")

'''
1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95 97 99 
'''

#4. Print multiplication table of 7

num = 7
for i in range(1,11):
    print(num,"x",i,"=",num*i)

'''
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
'''

#5. Find sum of numbers from 1 to 100

Sum = 0
for i in range(1,101):
    Sum = Sum + i
print(Sum)

'''
5050
'''

#6. Print numbers in reverse from 50 to 1

for i in range(50,0,-1):
    print(i,end=" ")

'''
50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 
'''

#7. Count how many numbers are divisible by 3 (1–100)

count = 0
for i in range(1,101):
    if i%3==0:
        count+=1
print(count,"numbers are divisible by 3 in (1-100)")

'''
33 numbers are divisible by 3 in (1-100)
'''

#8. Print squares of numbers from 1 to 10

for i in range(1,11):
    sqr = i**2
    print(sqr,end =" ")

'''
1 4 9 16 25 36 49 64 81 100 
'''

#9. Print cube of first 10 numbers

for i in range(1,11):
    cube = i**3
    print(cube,end=" ")

'''
1 8 27 64 125 216 343 512 729 1000 
'''

#10. Take input n, print numbers from 1 to n

n = int(input("Enter a number: "))
for i in range(1,n+1):
    print(i, end=" ")

'''
Enter a number: 12
1 2 3 4 5 6 7 8 9 10 11 12 
'''

#Section 2: While loop

#11. Print numbers from 1 to 20 using while

i = 1
while(i < 21):
    print(i,end=" ")
    i+=1

'''
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 
'''

#12. Find factorial of a number using while

num = 6
i = 1
fact = 1
while(i < num):
    fact = fact * i
    i+=1
print("Factorial of",num,"is",fact)

'''
Factorial of 6 is 120
'''

#13. Reverse a number using while

num = 2008
i = num
rev = 0
while(i > 0):
    t = i % 10
    rev = rev * 10 + t
    i = i // 10
print("Given number:", num)
print("Reverse number:", rev)

'''
Given number: 2008
Reverse number: 8002
'''

#14. Count digits in a number

num = 80345
i = num
count = 0
while(i > 0):
    i = i // 10
    count += 1
print("Given Number:", num)
print("Number of digits:",count)

'''
Given Number: 80345
Number of digits: 5
'''

#15. Keep asking input until user enters "stop"

n = input("Enter a input: ")
while(n != "stop"):
    n = input("Enter again: ")
    print(n)

'''
Enter a input: hih
Enter again: sfd
sfd
Enter again: dfg
dfg
Enter again: stop
stop
'''

#Seciton 3: Nested Loop

#16. Print pattern

for i in range(1,5):
    for j in range(1,i+1):
        print("*",end="")
    print(" ")

'''
*
**
***
****
'''

#17. Print pattern

for i in range(1,5):
    for j in range(1,i+1):
        print(j,end="")
    print(" ")

'''
1 
12 
123 
1234 
'''

#18. Print multiplication table (1 to 5) using nested loop

for i in range(1,6):
    for j in range(1,11):
        print(i,"x",j,"=",i*j)
    print(" ")

'''
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
1 x 5 = 5
1 x 6 = 6
1 x 7 = 7
1 x 8 = 8
1 x 9 = 9
1 x 10 = 10
 
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20
 
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30
 
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
4 x 6 = 24
4 x 7 = 28
4 x 8 = 32
4 x 9 = 36
4 x 10 = 40
 
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
'''

#19. Print

letter = 'A'
for i in range(0,3):
    for j in range(0,3):
        conversion = ord(letter) + j
        result = chr(conversion)
        print(result, end=" ")
    print(" ")

'''
A B C  
A B C  
A B C 
'''

#20. Print

for i in range(0,7,3):
    for j in range(1,4):
        print(i+j, end=" ")
    print(" ")

'''
1 2 3  
4 5 6  
7 8 9 
'''

# Section 4: String Basics

#21. Count total characters in a string

string = "Happy"
print(string)
print("Total Characters:",len(string))

'''
Happy
Total Characters: 5
'''

#22. Count vowels in a string

vowels = "aeiouAEIOU"
string = "Umbrella"
count = 0
for i in string:
    for j in vowels:
        if i in j:
            count += 1
print(string)
print("Total vowels:", count)

'''
Umbrella
Total vowels: 3
'''

#23. Count consonants in a string

Consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
string = "Elephant"
count = 0
for i in string:
    for j in Consonants:
        if i in j:
            count+=1
print(string)
print("Total Consonants:", count)

'''
Elephant
Total Consonants: 5
'''

#24. Reverse a string using loop

string = "Tiger"
length = len(string)
print(string)
for i in range(length-1,-1,-1):
    print(string[i],end="")

'''
Tiger
regiT
'''

#25. Check if string is palindrome

string = "level"
length = len(string)
rev_string = ""
for i in range(length-1,-1,-1):
    rev_string += string[i]
print(string,"|",rev_string)
if (rev_string == string):
    print("Pallindrome")
else:
    print("Not Palindrome")

'''
level | level
Pallindrome
'''

#Section 5: String Slicing

#26. Print first 5 characters of a string

string = "Hippopotamus"
x = slice(0,5)
print(string)
print(string[x])

'''
Hippopotamus
Hippo
'''

#27. Print last 3 characters

string = "Black Bear"
length = len(string)
string_slice = string[-3:length+1]
print(string)
print(string_slice)

'''
Black Bear
ear
'''

#28. Print string in reverse using slicing

string = "Watermelon"
print(string)
print(string[::-1])

'''
Watermelon
nolemretaW
'''

#29 Print every 2nd character

string = "Pineapple"
print(string)
print(string[1:-1:2])

'''
Pineapple
iepl
'''

#30. Remove first and last character from string

string = "Tomato"
length = len(string)
print(string)
print(string[1:length-1])

'''
Tomato
omat
'''

#Section 6: List Basics

#31. Create a list of 5 numbers and print sum

mylist = [1,6,7,2,8]
Sum = 0
for i in mylist:
    Sum += i
print(Sum)

'''
24
'''

#32. Find maximum value in list

mylist = [22,44,200,132,54,100]
Max = 0
for i in mylist:
    if i > Max:
        Max = i
print(Max)

'''
200
'''

#33. Find minimum value in list

mylist = [22,44,200,132,54,100]
Min = 50
for i in mylist:
    if i < Min:
        Min = i
print(Min)

'''
22
'''

#34. Count total elements in list

mylist = [22,44,200,132,54,100]
count = 0
for i in mylist:
    count += 1
print("Total Elements:", count)

'''
Total Elements: 6
'''

#35. Check if element exists in list

element = "mouse"
mylist = ["CPU","printer","mouse","keyboard"]
exist = False
for i in mylist:
    if element == i:
        exist = True
        break
if exist==True:
    print("Element exists")
else:
    print("Element not exists")

'''
Element exists
'''

#Section 7: List Operations

#36. Add 3 elements using append()

mylist = ["apple","orange"]
print(mylist)
mylist.append("banana")
mylist.append("mango")
mylist.append("grapes")
print(mylist)
print("3 elements added")

'''
['apple', 'orange']
['apple', 'orange', 'banana', 'mango', 'grapes']
3 elements added
'''

#37. Insert element at specific index

mylist = ["apple", "orange", "banana"]
mylist.insert(1,"guava")
print(mylist)
print("new element inserted at index 1")

'''
['apple', 'guava', 'orange', 'banana']
new element inserted at index 1
'''

#38. Remove element using remove()

mylist = ["apple", "guava", "orange", "banana"]
mylist.remove("orange")
print(mylist)
print("Element orange is removed")

'''
['apple', 'guava', 'banana']
Element orange is removed
'''

#39. Reverse list without using .reverse()

mylist = ["apple", "guava", "banana"]
newlist =[]
for i in range(len(mylist)-1,-1,-1):
    newlist.append(mylist[i])
print(newlist)

'''
['banana', 'guava', 'apple']
'''

#40. Sort list without using .sort()

mylist = [8,3,10,6]
print("Given list:", mylist)
t = 0
for i in range(0,len(mylist)):
    for j in range(0,len(mylist)):
        if(mylist[i]<mylist[j]):
            t = mylist[i]
            mylist[i] = mylist[j]
            mylist[j] = t

print("Sorted list:", mylist)

'''
Given list: [8, 3, 10, 6]
Sorted list: [3, 6, 8, 10]
'''
