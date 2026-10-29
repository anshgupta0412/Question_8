# Question 1 : Employee Salary Calculator
def calculate_salary(basic, allowance, deduction):
    net_salary = basic + allowance - deduction
    return net_salary

basic = 30000
allowance = 5000
deduction = 2000

print("Net Salary:: ",calculate_salary(30000, 5000, 2000))


# Question 2 : Electricity Bill Calculator

def calculate_bill(units):
    if units <= 95:
        bill = units * 5

    elif units <= 165:
        bill = (95 * 5) + ((units - 95) * 7)

    else:
        bill = (95 * 5) + (70 * 7) + ((units - 165) * 10)

    return bill

print(calculate_bill(230))

def calculate_bill(units):
    if units <= 100:
        bill = units * 5

    elif units <= 200:
        bill = (100 * 5) + ((units - 100) * 7)

    else:
        bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

    return bill

print(calculate_bill(230))

# Question 3 : Shopping Discount Calculator

def calculate_discount(amount):
    if amount <= 2000:
        discount = 0
        print("No discount to you!!... Fuck off")
        print("Total payable bill:: ", amount)
        return discount
    elif amount <= 5000:
        discount = amount * 10 / 100
        print("Total payable bill:: ", amount - discount)
        return discount
    else:
        discount = amount * 20 / 100
        print("Total payable bill:: ", amount - discount)
        return discount

print("Total Discount", calculate_discount(2500))

# Question 4 : ATM Withdrawal

def withdraw(balance, amount):

    if amount <= 0:
        print("Invalid withdrawl amount!!")
        return balance
    
    elif amount > balance:
        print("Insufficient Balance!!")
        return balance

    else:
        balance = balance - amount
        print("Withdrawl Successfull!!")
        return balance

new_balance = withdraw(10000, 200)
print("Updated balance", new_balance)

# Question 5 : Student Grade Calculator

def calculate_grade(avg):

    if avg >= 90:
        print("Grade :: A")

    elif avg >= 75:
        print("Grade :: B")

    elif avg >= 60:
        print("Grade :: C")

    elif avg >= 40:
        print("Grade :: D")

    elif avg >= 0:
        print("Fail")

    else:
        print("Invalid Average!!")

marks_1 = float(input("enter marks one:: "))
marks_2 = float(input("enter marks two:: "))
marks_3 = float(input("enter marks three:: "))
marks_4 = float(input("enter marks four:: "))
marks_5 = float(input("enter marks five:: "))

Total = marks_1 + marks_2 + marks_3 + marks_4 + marks_5
percentage = (Total / 500) * 100
avg = Total / 5

print("Total Marks:: ", Total)
print("Percentage:: ", percentage)
calculate_grade(avg)

# Question 6 : Bank Interest Calculator

def simple_interest(principal, rate, time):
    si = principal * rate * time
    return si

principal = float(input("enter principle:: "))
rate = float(input("enter rate:: "))
time = float(input("enter time:: "))

print("Simple Interest:: ",simple_interest(principal, rate, time))

# Question 7 : Restaurant Bill Generator

def restaurant_bill(food_bill, gst, tip):
    gst_amount = food_bill * gst / 100
    print("Gst Amount:: ", gst_amount)

    tip_amount = tip
    print("Tip amount:: ", tip_amount)

    food_Bill = food_bill
    print("Final bill:: ", food_Bill)

    final_Bill = food_bill + gst_amount + tip_amount
    print("==================================")

    return final_Bill

print("Total Payable amount:: ",restaurant_bill(550, 2.5, 50))

# Question 8 : Employee Attendance Calculator

def attendance(total_days, present_days):
    percentage = (present_days / total_days) * 100

    print("Attendance Percentage:", percentage)

    if percentage >= 75:
        return "Eligible"
    else:
        return "Attendance Shortage"


# Example
print("Status: ", attendance(120, 96))

# Question 9 : Mobile Recharge Plan

def recharge(plan):

    if plan == 199:
        return "Benifit: 1.5 GB/day, 28 days"
    elif plan == 299:
        return "2 GB/day, 28 days"
    else:
        return "2.5 GB/day, 56 days"

print(recharge(199))

# Question 10: Password Validator

def validate_password(password):

    if len(password) < 8:
        print("Invalid Password!!")

    has_digit = False
    has_upper = False
    has_lower = False

    for i in password:
        if i.isdigit():
            has_digit = True
        elif i.isupper():
            has_upper = True
        elif i.islower():
            has_lower = True

    if has_digit and has_lower and has_upper:
        return "Valid Password"
    else:
        return "Invalid Password"

print(validate_password("Ansh_1234"))

# Question 11: Online Shopping Delivery Charge
def calculate_order_amount(order_amount):
    if order_amount > 2000:
        delivery_charge = 0
    elif order_amount >= 1000:
        delivery_charge = 50
    else:
        delivery_charge = 100

    final_amount = order_amount + delivery_charge
    return final_amount


amount = float(input("Enter order amount: ₹"))

final_amount = calculate_order_amount(amount)

print("Final Amount: ₹", final_amount)


# Question 12 : Loan EMI Calculator
def calculate_emi(loan_amount, annual_rate, months):
    monthly_rate = annual_rate / (12 * 100)

    emi = (loan_amount * monthly_rate * (1 + monthly_rate) ** months) / \
          ((1 + monthly_rate) ** months - 1)

    return emi


loan = float(input("Enter loan amount: ₹"))
rate = float(input("Enter annual interest rate (%): "))
months = int(input("Enter number of months: "))

emi = calculate_emi(loan, rate, months)

print("Monthly EMI: ₹", round(emi, 2))


# Question 13 : Cab Fare Calculator
def calculate_fare(distance, waiting_time):
    base_fare = 50
    distance_charge = distance * 15
    waiting_charge = waiting_time * 2

    total_fare = base_fare + distance_charge + waiting_charge

    return total_fare


distance = float(input("Enter distance in km: "))
waiting = float(input("Enter waiting time in minutes: "))

fare = calculate_fare(distance, waiting)

print("Total Cab Fare: ₹", fare)

# Question 14 : Employee Bonus Calculator
def calculate_bonus(salary, experience):

    if experience > 10:
        bonus_percent = 20
    elif experience >= 5:
        bonus_percent = 10
    else:
        bonus_percent = 5

    bonus = salary * bonus_percent / 100
    final_salary = salary + bonus

    return bonus, final_salary


salary = float(input("Enter salary: ₹"))
experience = int(input("Enter years of experience: "))

bonus, final_salary = calculate_bonus(salary, experience)

print("Bonus: ₹", bonus)
print("Final Salary: ₹", final_salary)

# Question 15 : Grocery Billing System
def grocery_bill(items):

    total = sum(items)

    if total > 1000:
        discount = total * 10 / 100
    else:
        discount = 0

    amount_after_discount = total - discount

    gst = amount_after_discount * 5 / 100

    final_amount = amount_after_discount + gst

    return total, discount, gst, final_amount


items = [120, 250, 80, 450, 300]

total, discount, gst, final_amount = grocery_bill(items)

print("Total Amount: ₹", total)
print("Discount: ₹", discount)
print("GST: ₹", gst)
print("Final Payable Amount: ₹", final_amount)

# Question 16 : Hospital Consultation Bill
def hospital_bill(consultation_fee, number_of_tests, cost_per_test, medicine_cost):

    test_cost = number_of_tests * cost_per_test

    total_bill = consultation_fee + test_cost + medicine_cost

    if total_bill > 10000:
        discount = total_bill * 5 / 100
    else:
        discount = 0

    final_bill = total_bill - discount

    return total_bill, discount, final_bill


consultation = float(input("Enter consultation fee: ₹"))
tests = int(input("Enter number of tests: "))
test_cost = float(input("Enter cost per test: ₹"))
medicine = float(input("Enter medicine cost: ₹"))

total, discount, final = hospital_bill(
    consultation, tests, test_cost, medicine
)

print("Total Bill: ₹", total)
print("Discount: ₹", discount)
print("Final Bill: ₹", final)

# Question 17 : Movie Ticket Booking
def calculate_food_bill(food_items, distance):

    food_total = sum(food_items)

    if food_total > 500:
        delivery_charge = 0
    else:
        delivery_charge = 40

    if distance > 5:
        extra_distance = distance - 5
        delivery_charge = delivery_charge + (extra_distance * 10)

    final_amount = food_total + delivery_charge

    return food_total, delivery_charge, final_amount


items = [200, 150, 100]
distance = float(input("Enter delivery distance in km: "))

food_total, delivery, final = calculate_food_bill(items, distance)

print("Food Total: ₹", food_total)
print("Delivery Charge: ₹", delivery)
print("Final Amount: ₹", final)


# Question 18 : Food Delivery Order
def calculate_food_bill(food_items, distance):

    food_total = sum(food_items)

    if food_total > 500:
        delivery_charge = 0
    else:
        delivery_charge = 40

    if distance > 5:
        extra_distance = distance - 5
        delivery_charge = delivery_charge + (extra_distance * 10)

    final_amount = food_total + delivery_charge

    return food_total, delivery_charge, final_amount


items = [200, 150, 100]
distance = float(input("Enter delivery distance in km: "))

food_total, delivery, final = calculate_food_bill(items, distance)

print("Food Total: ₹", food_total)
print("Delivery Charge: ₹", delivery)
print("Final Amount: ₹", final)

# Question 19 : Salary Tax Calculator
def calculate_tax(annual_salary):

    if annual_salary <= 300000:
        tax = 0
    elif annual_salary <= 600000:
        tax = annual_salary * 5 / 100
    elif annual_salary <= 1000000:
        tax = annual_salary * 10 / 100
    else:
        tax = annual_salary * 20 / 100

    return tax


salary = float(input("Enter annual salary: ₹"))

tax = calculate_tax(salary)

print("Annual Tax: ₹", tax)


# Question 20 : Mini Banking Application
def create_account():
    name = input("Enter account holder name: ")
    account_number = input("Enter account number: ")
    balance = float(input("Enter initial deposit: ₹"))

    account = {
        "name": name,
        "account_number": account_number,
        "balance": balance
    }

    print("Account created successfully!")

    return account


def deposit(account):
    amount = float(input("Enter deposit amount: ₹"))

    if amount > 0:
        account["balance"] = account["balance"] + amount
        print("Amount deposited successfully!")
    else:
        print("Invalid amount!")


def withdraw(account):
    amount = float(input("Enter withdrawal amount: ₹"))

    if amount <= 0:
        print("Invalid amount!")

    elif amount > account["balance"]:
        print("Insufficient balance!")

    else:
        account["balance"] = account["balance"] - amount
        print("Amount withdrawn successfully!")


def check_balance(account):
    print("Current Balance: ₹", account["balance"])


def display_account(account):
    print("\n----- Account Details -----")
    print("Name:", account["name"])
    print("Account Number:", account["account_number"])
    print("Balance: ₹", account["balance"])
    print("---------------------------")


# Main Program

account = None

while True:

    print("\n===== MINI BANKING APPLICATION =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Display Account Details")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        account = create_account()

    elif choice == "2":
        if account is not None:
            deposit(account)
        else:
            print("Please create an account first!")

    elif choice == "3":
        if account is not None:
            withdraw(account)
        else:
            print("Please create an account first!")

    elif choice == "4":
        if account is not None:
            check_balance(account)
        else:
            print("Please create an account first!")

    elif choice == "5":
        if account is not None:
            display_account(account)
        else:
            print("Please create an account first!")

    elif choice == "6":
        print("Thank you for using Mini Banking Application!")
        break

    else:
        print("Invalid choice! Please try again.")


# question 21 : Bill generator
def shopping(items):
    total_bill = sum(items)

    if total_bill > 1000:
        discount = total_bill * 10 / 100
        total_bill = total_bill - discount
        
    else:
        print("no discount")


    gst = total_bill * 2.5 / 100
    final_bill = total_bill + gst

    return final_bill

items = []
n = int(input("enter number of items: "))
print("no of items: ", n)
for i in range(n):
    product = input("enter product name: ")
    price = int(input("enter price: "))

    items.append(price)

obj = shopping(items)

print(obj)


# Question 22 : Number Analyzer
def Number_Analyzer(num):
    result = []

    if num > 0:
        result.append("positive") 
    elif num < 0:
        result.append("negative")
    else:
        result.append("non")

    if num % 2 == 0:
        result.append("even")
    else:
        result.append("negative")
    
    if num // 5 == 0:
        result.append("Number is divisible by 5")
    else:
        result.append("Number is not divisble by 5")

    return result
num = int(input("enter a number: "))

obj = Number_Analyzer(num)
print(obj)

# Question 23 : Shopping Coupon System 
def apply_coupon(amount, coupon):

    if coupon == "SAVE10":
        discount = amount * 10 / 100
        amount = amount - discount

    elif coupon == "SAVE20":
        discount = amount * 20 / 100
        amount = amount - discount

    elif coupon == "FLAT100":
        discount = 100
        amount = amount - discount

    else:
        print("Invalid Coupon..... No Discount")

    return amount

amount = int(input("enter your bill amount: "))
coupon = input("enter coupon code: ")
coupon = coupon.upper()

obj = apply_coupon(amount, coupon)
print("Total payable amount: ", obj)


# Question 24 : Internet Data Usage
def calculate_data_usage(data_used, plan_limit):
    usage = (data_used / plan_limit) * 100

    if usage < 80:
        return "normal usage..."

    elif usage <= 100:
        return "Data almost Finished..."

    else:
        return "Data limit exceeded..."


data_used = int(input("enter data usage: "))
plan_limit = int(input("enter plan limit: "))
print(calculate_data_usage(data_used, plan_limit))


# Question 25 : Exam Result Analyzer
def result(marks):
    Total = 0
    count = 0

    # Calculate Total
    for i in marks:
        Total += i
    print("The total marks obtained: ", Total)

    # Calculate Average
    avg = Total / len(marks)
    print("The avg of marks is : ", avg)

    # Highest and Lowest
    print("The highest marks: ",max(marks))
    print("The Lowest marks: ",min(marks))

    # Count Passed Subjects
    for i in marks:
        if i >= 40:
            count += 1
    print("Total number of subjects passed: ", count)

marks = [40, 50, 32, 24, 75, 22]
result(marks)

#Question 26 : Constructor 
class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee Name:", self.name, "having salary:", self.salary)

e1 = Employee("John", 50000)
e1.display()

#Question 27 : Question on single inheritance with constructor
class Animal:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Animal Name:", self.name)

class Dog(Animal):
    def __init__(self):
        super().__init__("Tommy")

    def sound(self):
        print("Dog barks")

d1 = Dog()
d1.display()
d1.sound()

#Question 28 : Multiple inheritance
class Father:
    def __init__(self):
        self.father_name = "Raj"

class Mother:
    def __init__(self):
        self.mother_name = "Priya"

class child(Father, Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)
        self.child_name = "Aman"

    def display(self):
        print("Father: ", self.father_name)
        print("Father: ", self.mother_name)
        print("Father: ", self.child_name)

c = child()
c.display()


#Question 29 : Multiple inheritance in another way
class Father:
    def __init__(self, name):
        self.father_name = name

class Mother:
    def __init__(self, name):
        self.mother_name = name

class child(Father, Mother):
    def __init__(self):
        Father.__init__(self, "Raj")
        Mother.__init__(self, "Priya")
        self.child_name = "Aman"

    def display(self):
        print("Father: ", self.father_name)
        print("Father: ", self.mother_name)
        print("Father: ", self.child_name)

c = child()
c.display()

# Question 30:
class Grandfather:
    def __init__(self, name):
        self.Grandfather_name = name

class Father:
    def __init__(self, name):
        self.Father_name = name

class Son(Grandfather, Father):
    def __init__(self):
        Grandfather.__init__(self, "Bapuiji")
        Father.__init__(self,"Jhetalal")
        self.child_name = "Tapu"

    def display(self):
        print("GrandFather Name: ", self.Grandfather_name)
        print("Father Name: ", self.Father_name)
        print("Son Name: ", self.child_name)

s = Son()
s.display()