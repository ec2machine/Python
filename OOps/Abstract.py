# abstract use complasery that method inside and use your class from praent(abstact class) class


from abc import ABC, abstractmethod  # Import ABC and abstractmethod from abc module


class Payment(ABC):  # Create an abstract class named Payment

    @abstractmethod  # Mark this method as an abstract method
    def pay(self, amount):  # Define the abstract pay method
        pass  # No implementation here; child classes must implement it


class GooglePay(Payment):  # Create GooglePay class that inherits Payment

    def pay(self, amount):  # Implement the pay method
        print(f"Paid ₹{amount} using Google Pay")  # Display payment information


class PhonePe(Payment):  # Create PhonePe class that inherits Payment

    def pay(self, amount):  # Implement the pay method
        print(f"Paid ₹{amount} using PhonePe")  # Display payment information


class CreditCard(Payment):  # Create CreditCard class that inherits Payment

    def pay(self, amount):  # Implement the pay method
        print(f"Paid ₹{amount} using Credit Card")  # Display payment information


payment1 = GooglePay()  # Create a GooglePay object

payment1.pay(1000)  # Call the pay method with ₹1000


payment2 = PhonePe()  # Create a PhonePe object

payment2.pay(2000)  # Call the pay method with ₹2000


payment3 = CreditCard()  # Create a CreditCard object

payment3.pay(5000)  # Call the pay method with ₹5000