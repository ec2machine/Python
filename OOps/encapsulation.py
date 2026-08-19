# encapslution prodect your attribute access decreatly(pubilc,_prodect,__prive),
# private attribute accessand update only getter and setter

class Payment:  # Create a class named Payment

    def __init__(self, amount):  # Constructor that receives the payment amount
        self.__amount = amount  # Store amount as a private variable using __

    def show_amount(self):  # Define a method to display the payment amount
        print("Payment amount:", self.__amount)  # Access and print the private amount

    def update_amount(self, new_amount):  # Define a method to update the payment amount
        if new_amount > 0:  # Check whether the new amount is greater than zero
            self.__amount = new_amount  # Update the private amount
        else:  # Execute this block if the amount is not valid
            print("Invalid amount")  # Display an error message


payment = Payment(1000)  # Create a Payment object with amount 1000

payment.show_amount()  # Call the method to display the amount

payment.update_amount(2000)  # Update the payment amount to 2000

payment.show_amount()  # Display the updated amount

"""Encapsulation means keeping data and the 
methods that work on that data together inside a 
class and controlling how the data is accessed
"""
#eg:2
class BankAccount:  # Create a class
    def __init__(self, balance):  # Constructor
        self.__balance = balance  # Private data

    def deposit(self, amount):  # Method to add money
        self.__balance += amount  # Update balance

    def show_balance(self):  # Method to show balance
        print(self.__balance)  # Display balance


account = BankAccount(1000)  # Create object

account.deposit(500)  # Add 500

account.show_balance()  # Show balance

#=======================================================================================
'''
1. Getter

Getter is a method used to get/read the value of a private variable.

2. Setter

Setter is a method used to set/update the value of a private variable.
'''
class Student:  # Create Student class

    def __init__(self, name):  # Constructor
        self.__name = name  # Private variable

    def get_name(self):  # Getter method
        return self.__name  # Return the private name

    def set_name(self, name):  # Setter method
        self.__name = name  # Update the private name


student = Student("Vignesh")  # Create object

print(student.get_name())  # Getter: read the name

student.set_name("Vigneshwaran")  # Setter: update the name

print(student.get_name())  # Getter: read the updated name