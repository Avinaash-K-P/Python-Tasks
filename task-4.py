#Mini Project 1: Employee Management System

def add_emp():
    new_user = {"name": "Bob", "age": 28, "role": "Developer", "salary": 70000}
    employees.append(new_user)

def update_emp():
    employees[0]["salary"] = 60000

def delete_emp():
    employees.pop(0)

def display_emp():
    print("Employee Details:")
    print(employees)

employees = [{"name":'John', "age": 24, "role": 'Developer',"salary": 55000},{"name":'Tom', "age": 25, "role": 'Tester',"salary": 40000}]

add_emp()
update_emp()
delete_emp()
display_emp()

#Mini Project 2: Student Report Card

def total():
    totol = report_card["maths"]+ report_card["science"]+ report_card["english"]
    return totol

def average():
    totol = report_card["maths"] + report_card["science"] + report_card["english"]
    avg = totol/3
    return avg

def formatted_report(a,b):
    name = report_card["name"]
    math = report_card["maths"]
    sci = report_card["science"]
    eng = report_card["english"]
    print("*******REPORT CARD**********")
    print("----------------------------")
    text1 =  "Name: {}"
    text2 = "Maths: {}/100  Science: {}/100  English: {}/100"
    text3 = "Total: {}"
    text4 = "Average: {}"
    print(text1.format(name))
    print(text2.format(math,sci,eng))
    print(text3.format(a))
    print(text4.format(b))
    print("----------------------------")

def grade(g):
    if g > 90:
        print("GRADE: A")
    elif g > 80:
        print("GRADE: B")
    elif g > 70:
        print("GRADE: C")
    elif g > 60:
        print("GRADE: D")
    elif g > 50:
        print("GRADE: F")

report_card = {"name":"Arjun","maths":90,"science":85,"english":95}

tot = total()
avg = average()
formatted_report(tot,avg)
grade(avg)

#Mini Project 3: Shopping Cart System

def total_bill():
    total = 0
    for i in range(0,len(products)):
        total+= products[i]["price"]
    print("Total Bill: Rs.",total)

def remove_item():
    for i in range(0,len(products)):
        x = products[i]["name"]
        if x == "Watch":
            products.pop(i)
            print(x, "is removed from cart")
            break

def display_items():
    print("Total Items: ", len(products))
    print("----------------------------------------")
    print(products)

products = [{"name":"Watch","price":2000,"quantity":1} , {"name":"Hear phones","price":6000,"quantity":2}, {"name":"Camera","price":8000,"quantity":1}]

total_bill()
remove_item()
display_items()

#Mini Project 4: Login & User Validation

users = {"John":"john@123","Lisa":"lisa@123","Tom":"tom@123"}

user_login = input("Enter Username: ")
pwd = input("Enter Password: ")

if user_login in users:
    if pwd in users[user_login]:
        print("Login Success !!")
    else:
        print("Login Failure")
else:
    print("Login Failure")

#Mini Project 5: Unique Visitor Counter

visitors = {"John","Tom","Amy","Monica","Tom","Jim","Adam"}
print(visitors)

#Mini Project 6: String Formatter Tool

name = input("Enter your name: ")
product = input("Enter your product: ")

print("****{}****".format(name))
print("****{}****".format(product))

print("****{msg:<6}****".format(msg=name))
print("****{msg:<6}****".format(msg=product))

print("****{msg:>4}****".format(msg=name))
print("****{msg:>4}****".format(msg=product))

print("****{msg:^12}****".format(msg=name))
print("****{msg:^12}****".format(msg=product))

#Mini Project 7: Bank Account System

def deposit():
    money = int(input("Enter the amount to deposit: "))
    account["balance"] += money
    print("Rs.",money,"deposited")

def withdraw():
    money = int(input("Enter the amount to withdraw: "))
    account["balance"] -= money
    print("Rs.",money, "deposited")

def check_balance():
    print("Current Balance: Rs.",account["balance"])

account = {"name":"Ram","balance":65000}

deposit()
withdraw()
check_balance()

#Mini Project 8: Voting System

candidates_votes = {"John":50,"Linda":55,"Tom":42,"Sara":45}

print("-----Candidates List-----")
num = 1
for name in candidates_votes.keys():
    print(name," ---> press",num)
    num += 1
print("------------------")
vote = int(input("Enter your vote: "))

match(vote):
    case 1:
        candidates_votes["John"] += 1
    case 2:
        candidates_votes["Linda"] += 1
    case 3:
        candidates_votes["Tom"] += 1
    case 4:
        candidates_votes["Sara"] += 1

max_votes = 0
winner = ""
for key,value in candidates_votes.items():
    if value > max_votes:
        max_votes = value
        winner = key
print("The Winner is",winner,"won with",max_votes,"votes" )


#Mini Project 9: Course Enrollment System

print("student details --> name : course enrolled, student id, location")

enrollment_list = {"Aravind":["Civil",112,"Chennai"],"Geetha":["CSE",113,"Bangalore"]}
print(enrollment_list)

print("To add new student")
enrollment_list["Raju"] = ["EEE",114,"Mumbai"]
print(enrollment_list)

print("To update one student from CSE to IT course")
enrollment_list["Geetha"][0] = "IT"
print(enrollment_list)

print("To display student details")
name = input("Enter student name: ")
print("Name:", name)
print("Course enrolled:" , enrollment_list[name][0])
print("Student id:" , enrollment_list[name][1])
print("Location:" , enrollment_list[name][2])

#Mini Project 10: Number Utility Tool

num = int(input("Enter a number: "))

print("Binary value: {:b}".format(num))
print("Octal value: {:o}".format(num))
print("Hexa value: {:x}".format(num))

num = int(input("Enter a large number: "))

print("Comma seperated: {:,}".format(num))
print("Scientific notation: {:e}".format(num))

