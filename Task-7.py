#1. Use super() properly

class User:
    
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def register(self):
        print("register " + self.name)    

    def login(self):
        print("login " + self.name)

class Student(User):
    
    def __init__(self,name, id, dept, fees):
        super().__init__(name,id)
        self.dept = dept 
        self.fees = fees

    def greet(self):
        print("Welcome Student "+ self.name)

class Faculty(User):

    def __init__(self,name,id,salary):
        super().__init__(name,id)
        self.salary = salary
    
    def greet(self):
        print("Welcome Faculty "+ self.name)

class TempFaculty(User):

    def __init__(self,name,id,duration):
        super().__init__(name,id)
        self.duration = duration

    def greet(self):
        print("Welcome Temporary Faculty " + self.name)            

stud = Student("Tom",101,"CSE","2 lakhs")
facl = Faculty("Max",302,45000)
tempfacl = TempFaculty("Lisa",403,"15 days") 
stud.greet()
facl.greet()
tempfacl.greet()

'''
Welcome Student Tom
Welcome Faculty Max
Welcome Temporary Faculty Lisa
'''

#2.  Apply Abstraction

from abc import ABC, abstractmethod

class Abstractuser(ABC):

    @abstractmethod
    def __init__(self,name):
        self.name = name
    
    def get_details(self):
        print("Base user "+ self.name)

class First_user(Abstractuser):

    def __init__(self,name):
        self.name = name

    def get_details(self):
        print("First User " + self.name)

class Second_user(First_user): 

    def __init__(self,name):
        super().__init__(name)
       
    def get_details(self):
        print("Second User " + self.name)


user1 = First_user("John")
user1.get_details()
user2 = Second_user("Mike")
user2.get_details()

'''
First User John
Second User Mike
'''

#3. Sorting using key

students = [("Jim",60000),("Sara",70000),("Bob",50000),("Lily",40000)]
students.sort(key=lambda x:x[1])
print(students)
faculty = [("John",35000),("Emily",15000),("Mike",40000),("Dave",28000)]
faculty.sort(key=lambda x:x[1])
print(faculty)

'''
[('Lily', 40000), ('Bob', 50000), ('Jim', 60000), ('Sara', 70000)]
[('Emily', 15000), ('Dave', 28000), ('John', 35000), ('Mike', 40000)]
'''

#4. Use map()

names = list(map(lambda name:name[0],students))
print(names)

'''
['Lily', 'Bob', 'Jim', 'Sara']
'''

#5. Use filter()

high_fee_students = list(filter(lambda fees:fees[1]>50000,students))
print(high_fee_students)
high_salary_faculty = list(filter(lambda salary:salary[1]>30000,faculty))
print(high_salary_faculty)

'''
[('Jim', 60000), ('Sara', 70000)]
[('John', 35000), ('Mike', 40000)]
'''

#6. Use reduce()

import functools
total_salary = functools.reduce(lambda acc, salary: acc + salary[1],faculty,0)
print("Total Salary:", total_salary)
total_fees = functools.reduce(lambda acc, fees: acc + fees[1],students,0)
print("Total Fees:",total_fees)

'''
Total Salary: 118000
Total Fees: 220000
'''

#7. Higher Order Function

def process_users(users,func):
    return list(filter(lambda x:x[0][0] == func ,users))

def character():
    Char = 'M'
    return Char
 
user_list = ["Tom", "Mike", "John", "Monica", "Lisa"]
result = process_users(user_list,character())
print("First letter starts with M: ", result)

'''
First letter starts with M:  ['Mike', 'Monica']
'''

#8. Build a mini system

def get_details(users):
    print(users)

def sorted_data(users):
    users.sort(key = lambda x:x[0])
    print(users)

def filtered_data(users):
    result = list(filter(lambda x: x[1] % 3 ==0 ,users))
    print("Filter by second element divisible by 3:",result)

def total_fees_salary(users):
    result = functools.reduce(lambda acc, salary: acc + salary[1],users,0)
    print(result)


students = [("Jim",60000),("Sara",70000),("Bob",50000),("Lily",40000)]
faculty = [("John",35000),("Emily",15000),("Mike",40000),("Dave",28000)]

get_details(students)
get_details(faculty)
sorted_data(students)
sorted_data(faculty)
filtered_data(students)
filtered_data(faculty)
total_fees_salary(students)
total_fees_salary(faculty)

'''
[('Jim', 60000), ('Sara', 70000), ('Bob', 50000), ('Lily', 40000)]
[('John', 35000), ('Emily', 15000), ('Mike', 40000), ('Dave', 28000)]
[('Bob', 50000), ('Jim', 60000), ('Lily', 40000), ('Sara', 70000)]
[('Dave', 28000), ('Emily', 15000), ('John', 35000), ('Mike', 40000)]
Filter by second element divisible by 3: [('Jim', 60000)]
Filter by second element divisible by 3: [('Emily', 15000)]
220000
118000
'''

