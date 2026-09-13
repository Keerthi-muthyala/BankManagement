import json
import os

from .account import BankAccount


class Bank:

    def __init__(self):
        self.accounts = {}
        self.file_name = "data/accounts.json"
        self.load_accounts()

    def create_account(self):

        name = input("Enter your name: ")

        try:
            account_number = int(input("Enter account number: "))

            if account_number in self.accounts:
                print("Account already exists")
                return

            initial_balance = float(input("Enter initial balance: "))

            if initial_balance < 0:
                print("Balance cannot be negative")
                return

            account = BankAccount(
                name,
                account_number,
                initial_balance
            )

            self.accounts[account_number] = account
            self.save_accounts()

            print("Account created successfully")

        except ValueError:
            print("Please enter valid numbers")

    def find_account(self):

        try:
            account_number = int(
                input("Enter account number: ")
            )

            account = self.accounts.get(account_number)

            if account is None:
                print("Account not found")
                return None

            return account

        except ValueError:
            print("Please enter a valid account number")
            return None

    def deposit_money(self):

        account = self.find_account()

        if account is None:
            return

        try:
            amount = float(
                input("Enter deposit amount: ")
            )

            account.deposit(amount)
            self.save_accounts()

        except ValueError:
            print("Please enter a valid amount")

    def withdraw_money(self):

        account = self.find_account()

        if account is None:
            return

        try:
            amount = float(
                input("Enter withdrawal amount: ")
            )

            account.withdraw(amount)
            self.save_accounts()

        except ValueError:
            print("Please enter a valid amount")

    def check_balance(self):

        account = self.find_account()

        if account is None:
            return

        print(
            "Current balance:",
            account.get_balance()
        )

    def show_account_details(self):

        account = self.find_account()

        if account is None:
            return

        account.display_details()

    def show_transactions(self):

        account = self.find_account()

        if account is None:
            return

        account.display_transactions()
    def save_accounts(self):

        data = {}

        for account_number, account in self.accounts.items():
            data[str(account_number)] = account.to_dict()

        with open(self.file_name, "w") as file:
            json.dump(data, file, indent=4)

    def load_accounts(self):

        if not os.path.exists(self.file_name):
            return

        try:

            with open(self.file_name, "r") as file:
                data = json.load(file)

            for account_number, account_data in data.items():

                account = BankAccount.from_dict(account_data)

                self.accounts[int(account_number)] = account

        except (json.JSONDecodeError, KeyError):
            print("Unable to load account data")

    def menu(self):

        try:

            while True:

                print("\n==============================")
                print("     BANK MANAGEMENT SYSTEM")
                print("==============================")

                print("1. Create Account")
                print("2. Deposit Money")
                print("3. Withdraw Money")
                print("4. Check Balance")
                print("5. Account Details")
                print("6. Transaction History")
                print("7. Exit")

                choice = input("Enter your choice: ")

                if choice == "1":
                    self.create_account()

                elif choice == "2":
                    self.deposit_money()

                elif choice == "3":
                    self.withdraw_money()

                elif choice == "4":
                    self.check_balance()

                elif choice == "5":
                    self.show_account_details()

                elif choice == "6":
                    self.show_transactions()

                elif choice == "7":

                    print("Thank you for using the Bank Management System")
                    break

                else:
                    print("Invalid choice")

        except KeyboardInterrupt:

            print("\nProgram interrupted. Goodbye!")
