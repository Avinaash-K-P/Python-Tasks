#1. Encapsulation (User Class)

class User:

    def __init__(self):
        self.__user_name = None
        self.__pwd = None

    def set_user(self,user_name,pwd):
        self.__user_name = user_name
        self.__pwd = pwd

    def get_user(self):
        return self.__user_name

    def register(self):
        print(self.__user_name)

    def login(self):
        print("Logging in:", self.__user_name)

obj = User()
obj.set_user("john", "john@123")
x = obj.get_user()
print("Get username: ", x)
obj.register()
obj.login()

'''
Get username:  john
john
Logging in: john
'''

#2. Inheritance (User → Student, Faculty)

class User():

    def register(self):
        print("Registered")

    def login(self):
        print("Logged in")

class Student(User):

    def student_greet(self):
        print("Hello Student")

class Faculty(User):

    def faculty_greet(self):
        print("Hello Faculty")

class TempFaculty(Faculty):
    def tempFaculty_greet(self):
        print("Hello Temp Faculty")

student = Student()
student.register()
student.login()
student.student_greet()

faculty = Faculty()
faculty.register()
faculty.login()
faculty.faculty_greet()

tempFaculty = TempFaculty()
tempFaculty.register()
tempFaculty.login()
tempFaculty.faculty_greet()
tempFaculty.tempFaculty_greet()

parent = User()
# parent.student_greet()
# parent.faculty_greet()
# parent.tempFaculty_greet()

'''
Registered
Logged in
Hello Student
Registered
Logged in
Hello Faculty
Registered
Logged in
Hello Faculty
Hello Temp Faculty
'''

#3. Method Overriding

class User():

    def register(self):
        print("Registered")

    def login(self):
        print("Logged in")

    def greet(self):
        print("Welcome user")

class Student(User):

    def greet(self):
        print("Welcome Student")

class Faculty(User):

    def greet(self):
        print("Welcome Faculty")

student = Student()
faculty = Faculty()
student.greet()
faculty.greet()

'''
Welcome Student
Welcome Faculty
'''

#4. Method Chaining

class User:

    def register(self):
        print("registered")
        return self

    def login(self):
        print("logined")
        return self

    def greet(self):
        print("enjoy everyone")
        return self

user = User()
user.login().greet().register()

'''
logined
enjoy everyone
registered
'''

#5. Combined Task(Real-Time)

class User():

    username: None
    password: None
    users = 0

    def __init__(self,username,password):
        self.__username = username
        self.__password = password
        User.users += 1

    def register(self):
        print("Registerd")
        return self

    def login(self):
        print("Logged in")
        return self

    def greet(self):
        print("Welcome User")
        return self

class Student(User):

    def greet(self):
        print("Welcome Student")

    def student_greet(self):
        print("Hello Student")

class Faculty(User):

    def faculty_greet(self):
        print("Hello Faculty")

print("Mini User System")
user1 = User("John","john@123")
user2 = Student("Lisa","lisa@123")
user3 = Faculty("Bob","bob@123")

user1.register()
user1.login()
user2.register()
user3.login()
user2.student_greet()
user3.faculty_greet()
user2.greet()
user3.greet()
print("Number of users:", user3.users)
user1.login().greet().register()

'''
Mini User System
Registerd
Logged in
Registerd
Logged in
Hello Student
Hello Faculty
Welcome Student
Welcome User
Number of users: 3
Logged in
Welcome User
Registerd
'''


