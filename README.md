# Bank Account Management

## Overview
This Python program simulates basic bank account management operations. It allows for the creation of an account with a specified holder name and initial balance. The program can display account details and perform deposit operations to update the account balance.

## Description
The `Account` class represents a bank account with attributes for the account holder's name and current balance. The class provides methods to display account information and to deposit money into the account.

## Class and Methods

### `Account` Class
- `__init__(self, name, balance=0)`: Initializes an account with the holder's name and an optional initial balance (default is 0).
- `__str__(self)`: Returns a string representation of the account, displaying the account holder's name and the current balance.
- `deposit(self, amount)`: Adds the specified amount to the current balance and prints the updated balance.

## Usage
To use this program, create an instance of the `Account` class with the account holder's name and an optional initial balance. Use the `deposit` method to add money to the account and update the balance.

## Example
Here's an example of how to use the program:

```python
class Account:

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    # Print method
    def __str__(self):
        return f"Account holder: {self.name}\nAccount balance: {self.balance}"

    # Deposit method
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(self.balance)


acct1 = Account('Jose', 100)
print(acct1)
print(acct1.name)
print(acct1.balance)

acct1.deposit(50)
In this example:

An account is created for 'Jose' with an initial balance of 100.
The account details are printed.
The account holder's name and current balance are accessed and printed.
A deposit of 50 is made, and the updated balance is printed.
Note
Ensure that the deposit amount is a valid number.
The account details can be displayed using the __str__ method.
Enjoy managing your bank account with this simple Python program!
