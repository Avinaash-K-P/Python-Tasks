#1. User Info Manager (Functions + Dictionary)

def create_user(name,age,role):
    user_list = {"name": name.title(), "age": age, "role": role}
    return user_list

user_list=[ {"name": "Adam", "age": 26, "role": "Manager"}, {"name": "Lisa", "age": 24, "role": "HR"} ]
details = create_user("james",25,"Developer")
user_list.append(details)
print(user_list)

'''
[{'name': 'Adam', 'age': 26, 'role': 'Manager'}, {'name': 'Lisa', 'age': 24, 'role': 'HR'}, {'name': 'James', 'age': 25, 'role': 'Developer'}]
'''

#2. Dynamic Calculator (*args)

def calculate_total(*numbers):
    Sum = 0
    for i in numbers:
        Sum+=i
    return Sum

Total = calculate_total(1,2,3,4,5,6)
Average = Total/6
print("Sum of all numbers:",Total)
print("Average of all numbers:",Average)

'''
Sum of all numbers: 21
Average of all numbers: 3.5
'''

#3. Keyword Config System (**kwargs)

def system_config(**settings):
    for key,value in settings.items():
        print(key,value,sep=":")

system_config(mode ="debug", version =1.0, language ="Python",theme ="dark")

'''
mode:debug
version:1.0
language:Python
theme:dark
'''

#4. Factorial Service (Recursion)

def factorial(n):
    if n==0:
        return 1
    if n<0:
        print("Error: negative number")
        return 0
    return n*factorial(n-1)

print(factorial(-5))

'''
Error: negative number
0
'''

#5. Memory Optimization (Generator)

def square_generator(n):
    for i in range(1,n+1):
        yield i**2

newlist = square_generator(5)
print(newlist)
print("Generator:")
for i in newlist:
    print(i)

normal_list = []
print("Normal List:")
for i in range(1,6):
    normal_list.append(i)
print(normal_list)

'''
<generator object square_generator at 0x000002006686E340>
Generator:
1
4
9
16
25
Normal List:
[1, 2, 3, 4, 5]
'''

#6. Exception Handling Module

try:
    numerator = int(input("Enter a numerator: "))
    denominator = int(input("Enter a denominator: "))
    result = numerator/denominator
    print(result)

except ZeroDivisionError:
    print("You cannnot divide by zero")

except ValueError:
    print("Please enter a number")

finally:
    print("Program Completed")

'''
Enter a numerator: 45
Enter a denominator: 0
You cannnot divide by zero
'''

#7. File Handling

with open("team_data.txt") as f:
    print(f.read())
    print(f.closed)

'''
Username: John
password: john@123
email: john@gmail.com
False
'''
