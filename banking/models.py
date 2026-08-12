from dataclasses import dataclass
from datetime import datetime
from banking.exceptions import InsufficientFundsError, InvalidAmountError


@dataclass
class Transaction:
    amount: float
    transaction_type: str
    timestamp: datetime
    target_account: str | None = None


class BankAccount:
    def __init__(self, account_number: str, owner_name: str):
        self.account_number = account_number
        self.owner_name = owner_name
        self._balance = 0.0
        self._transactions = []


    @property
    def balance(self):
        return self._balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise InvalidAmountError("amount must be positive")
        self._balance += amount

        transactions = Transaction(
            amount=amount,
            transaction_type="deposit",
            timestamp=datetime.now()

        )
        self._transactions.append(transactions)

    def withdraw(self, amount: float):
        if amount <= 0:
            raise InvalidAmountError("amount must be positive")
        if amount > self._balance:
            raise InsufficientFundsError("insufficient balance")
        self._balance -= amount

        transactions = Transaction(
            amount=amount,
            transaction_type="withdraw",
            timestamp=datetime.now()
        )

        self._transactions.append(transactions)

    def transfer(self, amount: float, target_account):
        if amount <= 0:
            raise InvalidAmountError("amount must be positive")
        if amount > self._balance:
            raise InsufficientFundsError("insufficient balance")
        
        self._balance -= amount
        target_account._balance += amount

        transaction = Transaction(
            amount=amount,
            transaction_type="transfer",
            timestamp=datetime.now(),
            target_account=target_account.account_number
        )
        self._transactions.append(transaction)

        target_transaction = Transaction(
            amount=amount,
            transaction_type="deposit",
            timestamp=datetime.now(),
            target_account=self.account_number
        )
        target_account._transactions.append(target_transaction)
