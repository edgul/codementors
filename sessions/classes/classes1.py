# classes1.py

#Purpose: Program to manage Payroll:
#* Track employee hours
#* Pay employees

# Object and Classes discussion topics:
# * object is synonymous with instance
# * object is an instance of a class
# * class is like a blueprint for objects
# * constructor runs when you create the object (put init code here)
# * methods are functions that belong to an object
# * "self" is used to refer to the calling/created object
# * static methods belong to the class (set of objects)

#OO principles Learned: 
#* Abstraction - hide implementation details
#* Encapsulation - packaging of similar concepts
#* Polymorphism - a name can mean different things in different contexts

#Improvments Made to code:
#* readable
#* intuitive
#* change-tolerant
#
#

# Tangents:
# * Copying or reference passing (see mutability)

# FIRST ATTEMPT (WITHOUT CLASSES) - Note the problems encountered
# problem: parameters would expand with the amount of employee properties
# def payEmployees(employees : list, employeeRates : list):
#     pass
# 
# def removeEmployee(employees : list, employeeRates : list, employToRemove)
#     pass
# 
# # problem: if list changes -> indexs will need to change
# LEIA = 0
# LUKE = 1
# VADER = 2
# employeeHours = [0,0,0]
# employeeRates = [1,2,3]
# # problem: new property -> additional list
# 
# # problem: explicit use of structure -> not very change tolerant
# employeeHours[LEIA] += 5
# len(employeeHours)
#

import random

class Employee:
    numbers = []
    def __init__(self, name : str, hourlyWage : int):
        self.name = name
        self.hourlyWage = hourlyWage 
        self.hoursWorked = 0
        self.number = Employee.generateEmployeeNumber()
    def clearHours(self):
        self.hoursWorked = 0
    def addHours(self, hours : int):
        self.hoursWorked += hours 
    def isOwed(self):
        return self.hoursWorked * self.hourlyWage
    def pay(self, payCheck : int):
        self.hoursWorked -= int(payCheck / self.hourlyWage)
    def generateEmployeeNumber():
        i = 0
        while (Employee.numbers.count(i) != 0):
            i+= 1
        Employee.numbers.append(i)
        return i

class PayRoll:
    def __init__(self, cash : int):
        self.employees = []
        self.cash = cash
    def addEmployee(self, employee : Employee):
        self.employees.append(employee)
    def totalOwing(self) -> int:
        weeklyWages = 0
        for employee in self.employees:
            weeklyWages += employee.isOwed()
        return weeklyWages
    def payOutEachEmployee(self) -> None:
        for employee in self.employees:
            self.cash -= employee.isOwed()
            employee.pay(employee.isOwed())
    def scheduleRandomEmployee(self, hours : int):
        employeeIndex = random.randint(0, len(self.employees)-1)
        self.employees[employeeIndex].addHours(hours)
    def printBalanceSheet(self):
        print("Cash: " + str(self.cash))
        for employee in self.employees:
            print("Owing: " + employee.name + " " + str(employee.isOwed()))
        print("Total Owing: " + str(self.totalOwing()))

   
payroll = PayRoll(1000)
payroll.addEmployee(Employee("Luke", 11))
payroll.addEmployee(Employee("Leia", 15))
payroll.addEmployee(Employee("Darth", 7))

# schedule employees for the week
payroll.scheduleRandomEmployee(5)
payroll.scheduleRandomEmployee(5)
payroll.scheduleRandomEmployee(5)

# ...


payroll.printBalanceSheet()
print()
payroll.payOutEachEmployee()
payroll.printBalanceSheet()

