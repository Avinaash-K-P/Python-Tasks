# Smart Expense Manager

# SQL code
'''
CREATE DATABASE smart_expense;
USE smart_expense;

CREATE TABLE users(
	user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50)
);

CREATE TABLE expenses(
	exp_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    amount FLOAT,
    category VARCHAR(50),
    description VARCHAR(100),
    date DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
'''

# Python code

import mysql.connector
from datetime import datetime
import functools
from abc import ABC, abstractmethod

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mysql@123",
    database = "smart_expense",
    port = 3306
    )

print("Database connected successfully !!")

cursor = conn.cursor()

def user_create():
    name = input("Enter your name: ")
    cursor.execute("INSERT INTO users (name) VALUES (%s)",[name])
    conn.commit()
    print("New user created !!")


def add_expense():
    user_id = int(input("Enter user id: "))
    amount = int(input("Enter your amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")
    date = input("Enter date (yyyy-mm-dd): ")
    cursor.execute("INSERT INTO expenses (user_id,amount,category,description,date) VALUES (%s,%s,%s,%s,%s)",[user_id, amount, category, description, date])
    conn.commit()
    print("New expense added !!")

def view_expenses():
    cursor.execute("SELECT * FROM users as u INNER JOIN expenses as e ON e.user_id = u.user_id")
    print(cursor.fetchall())

def filter_expenses():
    cursor.execute("SELECT * from expenses")
    exp_list = cursor.fetchall()
    category = input("Enter category: ")
    filter_category = list(filter(lambda item : item[3] == category, exp_list))
    print(filter_category)
    date = input("Enter date (yyyy-mm-dd): ")
    date_format = datetime.strptime(date, "%Y-%m-%d").date()
    filter_date = [i if i[5] == date_format else "Not Available" for i in exp_list]
    print(filter_date)

def total_expense():
    cursor.execute("SELECT * from expenses")
    exp_list = cursor.fetchall()
    amount_list = list(map(lambda i: i[2], exp_list))    
    total_value = functools.reduce(lambda a,b: a+b, amount_list,0)
    print(total_value)

def category_spending():
    cursor.execute("SELECT category,amount from expenses")
    exp_list = cursor.fetchall()
    print(exp_list)
    category = ["Food","Travel","Shopping"]
    amount = []
    sum_food = 0
    sum_travel = 0
    sum_shopping = 0
    for i in exp_list:
        if i[0] == "Food":
            sum_food+=i[1]
        elif i[0] == "Travel":
            sum_travel+=i[1]
        elif i[0] == "Shopping":
            sum_shopping+=i[1]    
    amount.append(sum_food)
    amount.append(sum_travel)
    amount.append(sum_shopping)
    zipval = dict(zip(category,amount))
    result = {k:v for (k,v) in zipval.items()}
    print(result)

def delete_expense():
    id = int(input("Enter expense id to delete: "))
    cursor.execute("DELETE from expenses WHERE exp_id = %s",[id])
    conn.commit()
    print(f"Data of expense id:{id} is Deleted !!")

def update_expense():
    id = int(input("Enter expense id to update: "))
    amount = input("Update amount: ")
    category = input("Update category: ")
    description = input("Update description: ")
    date = input("Update date (yyyy-mm-dd): ")
    cursor.execute("UPDATE expenses SET amount = %s, category = %s, description = %s, date = %s WHERE exp_id = %s",[amount,category,description,date,id])
    conn.commit()
    print(f"Data of expense id:{id} is Updated !!")

print("Welcome to Smart Expense Management System !!") 
while True:
    print("------------------------------")
    print("1 -- > Create user")
    print("2 -- > Add expense")
    print("3 -- > View expenses")       
    print("4 -- > Filter expenses")
    print("5 -- > Calculate total expense")
    print("6 -- > Calculate category spending")
    print("7 -- > Delete expense")
    print("8 -- > Update expense")
    print("0 -- > Exit")
    inp = int(input("Enter the option: "))
    print("------------------------------")
    if inp == 1:
        user_create()
    elif inp == 2:
        add_expense()
    elif inp == 3:
        view_expenses()
    elif inp == 4:
        filter_expenses()
    elif inp == 5:
        total_expense()
    elif inp == 6:
        category_spending()
    elif inp == 7:
        delete_expense()
    elif inp == 8:
        update_expense()    
    elif inp == 0:
        break    
    else:
        print("Invalid input !!")

# OOP Implementation

class User(ABC):
    
    def __init__(self,user_id,name):
        self.user_id = user_id
        self.__name = name
    
    @abstractmethod
    def check(self):
        print("Welcome " + self.__name)

class Expense(User):

    def __init__(self,user_id,name):
        super().__init__(user_id,name)

    def check(self):
        print("Welcome user")

    def monthly_report(self):
        print("-----------------------------")
        print("Monthly report")
        cursor.execute("SELECT category,amount from expenses where user_id = %s",[self.user_id])
        result = cursor.fetchall()    
        food = 0
        travel = 0
        shopping = 0    
        for i in result:
            if i[0] == "Food":
                food += i[1]
            elif i[0] == "Travel":
                travel += i[1]
            elif i[0] == "Shopping":
                shopping += i[1]
        total_spending = food + travel + shopping
        print("Total Spending for this month:",total_spending)
        print("Food:",food)
        print("Travel:",travel)
        print("Shopping:",shopping)
        print("-----------------------------")

    def highest_expense(self):
        print("Highest expense")
        cursor.execute("Select category,amount from expenses where user_id = %s",[self.user_id])
        exp_list = cursor.fetchall()
        food_amt = []
        travel_amt = []
        shopping_amt = []
        for i in exp_list:
            if i[0] == "Food":
                food_amt.append(i[1])
            elif i[0] == "Travel":
                travel_amt.append(i[1])
            elif i[0] == "Shopping":
                shopping_amt.append(i[1])
        
        food_exp = functools.reduce(lambda a,b: a+b, food_amt,0)
        travel_exp = functools.reduce(lambda a,b: a+b, travel_amt,0)
        shopping_exp = functools.reduce(lambda a,b: a+b, shopping_amt,0)  

        if food_exp > shopping_exp and food_exp > travel_exp:
            print("Highest expense is Food:",food_exp)
        elif travel_exp > food_exp and travel_exp > shopping_exp:   
            print("Highest expense is Travel:",travel_exp)
        elif shopping_exp > food_exp and shopping_exp > travel_exp:     
            print("Highest expense is Shopping:",shopping_exp)    
        print("-----------------------------")       

    def smart_insights(self):
        print("Smart insights")
        food_limit = 5000
        shopping_limit = 15000
        travel_limit = 30000
        cursor.execute("Select category,amount from expenses where user_id = %s",[self.user_id])
        exp_list = cursor.fetchall()
        sum_food = 0
        sum_travel = 0
        sum_shopping = 0
        for i in exp_list:
            if i[0] == "Food":
                sum_food+=i[1]
            elif i[0] == "Travel":
                sum_travel+=i[1]
            elif i[0] == "Shopping":
                sum_shopping+=i[1]
        if sum_food > food_limit:
            print("You are spending too much on food this month !!")
        elif sum_travel > travel_limit:
            print("You are spending too much on travel this month !!")
        elif sum_shopping > shopping_limit:
            print("You are spending too much on shopping this month !!")     
        else:
            print("You are spending wisely this month !!")       
        print("-----------------------------")    

print("OOP Implementation of Smart Expense Management System !!")
id = int(input("Enter your id: "))
name = input("Enter your name: ")
cursor.execute("SELECT * from users")
users = cursor.fetchall()
exist = False
for user in users:
    if user[0] == id:
        if user[1] == name:
            exist = True
            print("Verified !!")
            break
if exist is False:
    print("User doesn't exist !!")
else:
    obj2 = Expense(id,name)
    obj2.check()
    obj2.monthly_report()
    obj2.highest_expense()
    obj2.smart_insights()
print("Thank you for using Smart Expense Management System !!")    