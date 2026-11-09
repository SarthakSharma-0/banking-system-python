#Banking Management System in Python

A command-line banking system built in Python as a Class 12 Computer Science project. It simulates basic bank operations, and all data is saved to a file so it stays after the program closes.

## Features
- Create, update and delete accounts
- Deposit and withdraw money
- Check balance and view a mini statement (last 5 transactions)
- Search accounts by account number or name
- List all savings or current accounts
- Show the richest and poorest customer
- Calculate yearly interest for savings accounts
- Input validation for numbers, amounts and account types

## Built With
- Python 3
- `pickle` for saving and loading account data
- Lists, dictionaries and functions

## How to Run
1. Make sure Python 3 is installed.
2. Download `banking_system.py` from this repo.
3. Run it:
   ```
   python banking_system.py
   ```
4. Choose an option from the menu. An `accounts.dat` file is created automatically to store your data.

## Sample Menu
```
===== BANKING SYSTEM =====
1. Create Account
2. Display All Accounts
3. Search by Account Number
4. Search by Name
5. Update Account Details
...
16. Exit
```

## Future Improvements
- Date and time for each transaction
- Password protection and encryption
- Monthly and yearly reports
- Fund transfer, fixed deposits and loans

## Author
Sarthak Sharma