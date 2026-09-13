class BankAccount:

    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.__balance = balance
        self.__transactions = []

    def deposit(self, amount):

        if amount <= 0:
            print("Invalid deposit amount")
            return

        self.__balance += amount
        self.__transactions.append(
            f"Deposited: {amount}"
        )

        print("Deposit successful")

    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid withdrawal amount")
            return

        if amount > self.__balance:
            print("Insufficient balance")
            return

        self.__balance -= amount
        self.__transactions.append(
            f"Withdrawn: {amount}"
        )

        print("Withdrawal successful")

    def get_balance(self):
        return self.__balance

    def display_details(self):

        print("\n--- Account Details ---")
        print("Name:", self.name)
        print("Account Number:", self.account_number)
        print("Balance:", self.__balance)

    def display_transactions(self):

        print("\n--- Transaction History ---")

        if not self.__transactions:
            print("No transactions found")
            return

        for transaction in self.__transactions:
            print(transaction)

    def to_dict(self):

        return {
            "name": self.name,
            "account_number": self.account_number,
            "balance": self.__balance,
            "transactions": self.__transactions
        }

    @classmethod
    def from_dict(cls, data):

        account = cls(
            data["name"],
            data["account_number"],
            data["balance"]
        )

        account.__transactions = data["transactions"]

        return account
