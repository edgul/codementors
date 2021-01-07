# classes.py
'''
scope
members
    variables
    methods
constructor
'''

import random

class Employee:
    def __init__(self, name : str, hourlyWage : int):
        self.name = name
        self.hourlyWage = hourlyWage 
        self.hoursWorked = 0
    def clearHours(self):
        self.hoursWorked = 0
    def addHours(self, hours : int):
        self.hoursWorked += hours 
    def isOwed(self):
        return self.hoursWorked * self.hourlyWage
    def pay(self, payCheck : int):
        self.hoursWorked -= int(payCheck / self.hourlyWage)

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

