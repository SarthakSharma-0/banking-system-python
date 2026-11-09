"""
Banking Management System in Python
A command-line banking system with file-based storage (pickle).
"""

import pickle

filename = "accounts.dat"
VALID_TYPES = ("savings", "current")


# ---------------- Input helpers ----------------
def ask_int(prompt):
    """Keep asking until the user enters a whole number."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid whole number.")


def ask_amount(prompt, allow_zero=False):
    """Keep asking until the user enters a valid, non-negative amount."""
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if value < 0 or (value == 0 and not allow_zero):
            print("Amount must be greater than zero." if not allow_zero
                  else "Amount cannot be negative.")
            continue
        return value


def ask_account_type(prompt, allow_blank=False):
    """Accept only Savings or Current (case-insensitive)."""
    while True:
        value = input(prompt).strip()
        if allow_blank and value == "":
            return ""
        if value.lower() in VALID_TYPES:
            return value.capitalize()
        print("Account type must be 'Savings' or 'Current'.")


# ---------------- File handling ----------------
def load_accounts():
    """Load all accounts from the file."""
    try:
        with open(filename, "rb") as f:
            accounts = pickle.load(f)
    except (FileNotFoundError, EOFError, pickle.UnpicklingError):
        accounts = []
    return accounts


def save_accounts(accounts):
    """Save all accounts to the file."""
    with open(filename, "wb") as f:
        pickle.dump(accounts, f)


# Feature 1: Create New Account
def create_account():
    accounts = load_accounts()

    acc_no = ask_int("Enter Account Number: ")
    # Check if account number already exists
    for acc in accounts:
        if acc['acc_no'] == acc_no:
            print("Account number already exists!")
            return

    name = input("Enter Name: ").strip()
    if not name:
        print("Name cannot be empty!")
        return
    acc_type = ask_account_type("Enter Account Type (Savings/Current): ")
    balance = ask_amount("Enter Initial Deposit: ", allow_zero=True)

    # Each account keeps a transaction list for mini-statement
    account = {
        'acc_no': acc_no,
        'name': name,
        'type': acc_type,
        'balance': balance,
        'transactions': [f"Account created with ₹{balance}"]
    }

    accounts.append(account)
    save_accounts(accounts)
    print("✅ Account created successfully!")


# Feature 2: Display All Accounts
def display_accounts():
    accounts = load_accounts()
    if not accounts:
        print("No accounts found!")
        return
    print("\n===== All Accounts =====")
    for acc in accounts:
        print(f"\nAccount Number: {acc['acc_no']}")
        print(f"Name         : {acc['name']}")
        print(f"Type         : {acc['type']}")
        print(f"Balance      : ₹{acc['balance']}")


# Feature 3: Search by Account Number
def search_by_acc_no():
    accounts = load_accounts()
    search_no = ask_int("Enter Account Number to search: ")
    for acc in accounts:
        if acc['acc_no'] == search_no:
            print("\n✅ Account Found!")
            print(f"Account Number: {acc['acc_no']}")
            print(f"Name         : {acc['name']}")
            print(f"Type         : {acc['type']}")
            print(f"Balance      : ₹{acc['balance']}")
            return
    print("Account not found!")


# Feature 4: Search by Name
def search_by_name():
    accounts = load_accounts()
    search_name = input("Enter Name to search: ").strip().lower()
    found = False
    for acc in accounts:
        if acc['name'].lower() == search_name:
            print("\n✅ Account Found!")
            print(f"Account Number: {acc['acc_no']}")
            print(f"Name         : {acc['name']}")
            print(f"Type         : {acc['type']}")
            print(f"Balance      : ₹{acc['balance']}")
            found = True
    if not found:
        print("No account found with that name.")


# Feature 5: Update Account Details
def update_account():
    accounts = load_accounts()
    acc_no = ask_int("Enter Account Number to update: ")
    for acc in accounts:
        if acc['acc_no'] == acc_no:
            new_name = input(
                f"Enter new Name (or press Enter to keep '{acc['name']}'): ").strip()
            if new_name:
                acc['name'] = new_name
            new_type = ask_account_type(
                f"Enter new Type (or press Enter to keep '{acc['type']}'): ",
                allow_blank=True)
            if new_type:
                acc['type'] = new_type
            save_accounts(accounts)
            print("✅ Account updated successfully!")
            return
    print("Account not found!")


# Feature 6: Delete Account
def delete_account():
    accounts = load_accounts()
    acc_no = ask_int("Enter Account Number to delete: ")
    for acc in accounts:
        if acc['acc_no'] == acc_no:
            accounts.remove(acc)
            save_accounts(accounts)
            print("✅ Account deleted successfully!")
            return
    print("Account not found!")


# Feature 7: Deposit Money
def deposit_money():
    accounts = load_accounts()
    acc_no = ask_int("Enter Account Number to deposit money: ")
    for acc in accounts:
        if acc['acc_no'] == acc_no:
            amount = ask_amount("Enter amount to deposit: ")
            acc['balance'] += amount
            acc['transactions'].append(f"Deposited ₹{amount}")
            save_accounts(accounts)
            print(f"✅ ₹{amount} deposited successfully!")
            return
    print("Account not found!")


# Feature 8: Withdraw Money
def withdraw_money():
    accounts = load_accounts()
    acc_no = ask_int("Enter Account Number to withdraw money: ")
    for acc in accounts:
        if acc['acc_no'] == acc_no:
            amount = ask_amount("Enter amount to withdraw: ")
            if amount > acc['balance']:
                print("Insufficient balance!")
            else:
                acc['balance'] -= amount
                acc['transactions'].append(f"Withdrew ₹{amount}")
                save_accounts(accounts)
                print(f"✅ ₹{amount} withdrawn successfully!")
            return
    print("Account not found!")


# Feature 9: Check Balance
def check_balance():
    accounts = load_accounts()
    acc_no = ask_int("Enter Account Number to check balance: ")
    for acc in accounts:
        if acc['acc_no'] == acc_no:
            print(f"Current Balance: ₹{acc['balance']}")
            return
    print("Account not found!")


# Feature 10: Mini Statement (last 5 transactions)
def mini_statement():
    accounts = load_accounts()
    acc_no = ask_int("Enter Account Number for mini statement: ")
    for acc in accounts:
        if acc['acc_no'] == acc_no:
            print(f"\nMini Statement for Account {acc_no}:")
            last_txns = acc['transactions'][-5:]
            for txn in last_txns:
                print(txn)
            return
    print("Account not found!")


# Feature 11: List All Savings Accounts
def list_savings_accounts():
    accounts = load_accounts()
    found = False
    for acc in accounts:
        if acc['type'].lower() == "savings":
            print(f"\nAccount Number: {acc['acc_no']}, Name: {acc['name']}, Balance: ₹{acc['balance']}")
            found = True
    if not found:
        print("No savings accounts found.")


# Feature 12: List All Current Accounts
def list_current_accounts():
    accounts = load_accounts()
    found = False
    for acc in accounts:
        if acc['type'].lower() == "current":
            print(f"\nAccount Number: {acc['acc_no']}, Name: {acc['name']}, Balance: ₹{acc['balance']}")
            found = True
    if not found:
        print("No current accounts found.")


# Feature 13: Show Richest Customer
def richest_customer():
    accounts = load_accounts()
    if not accounts:
        print("No accounts found.")
        return
    richest = accounts[0]
    for acc in accounts:
        if acc['balance'] > richest['balance']:
            richest = acc
    print(f"Richest Customer: {richest['name']} (Account {richest['acc_no']}), Balance: ₹{richest['balance']}")


# Feature 14: Show Poorest Customer
def poorest_customer():
    accounts = load_accounts()
    if not accounts:
        print("No accounts found.")
        return
    poorest = accounts[0]
    for acc in accounts:
        if acc['balance'] < poorest['balance']:
            poorest = acc
    print(f"Poorest Customer: {poorest['name']} (Account {poorest['acc_no']}), Balance: ₹{poorest['balance']}")


# Feature 15: Interest Calculation for Savings
def calculate_interest():
    accounts = load_accounts()
    rate = ask_amount("Enter yearly interest rate (%) for savings accounts: ", allow_zero=True)
    found = False
    for acc in accounts:
        if acc['type'].lower() == "savings":
            interest = acc['balance'] * rate / 100
            print(f"Account {acc['acc_no']} ({acc['name']}): Interest = ₹{interest:.2f}")
            found = True
    if not found:
        print("No savings accounts found.")


# ---------------- Main Menu ----------------
def main():
    actions = {
        "1": create_account,
        "2": display_accounts,
        "3": search_by_acc_no,
        "4": search_by_name,
        "5": update_account,
        "6": delete_account,
        "7": deposit_money,
        "8": withdraw_money,
        "9": check_balance,
        "10": mini_statement,
        "11": list_savings_accounts,
        "12": list_current_accounts,
        "13": richest_customer,
        "14": poorest_customer,
        "15": calculate_interest,
    }

    while True:
        print("\n===== BANKING SYSTEM =====")
        print("1. Create Account")
        print("2. Display All Accounts")
        print("3. Search by Account Number")
        print("4. Search by Name")
        print("5. Update Account Details")
        print("6. Delete Account")
        print("7. Deposit Money")
        print("8. Withdraw Money")
        print("9. Check Balance")
        print("10. Mini Statement")
        print("11. List All Savings Accounts")
        print("12. List All Current Accounts")
        print("13. Show Richest Customer")
        print("14. Show Poorest Customer")
        print("15. Interest Calculation")
        print("16. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "16":
            print("Exiting. Goodbye!")
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
