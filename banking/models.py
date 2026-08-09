from dataclasses import dataclass
from datetime import datetime


@dataclass
class Transaction:
    amount: float
    transaction_type: str
    timestamp: datetime
    target_account: str | None = None


class BankAccount:
    def __init__(self):
        self._balance = 0.0
        self._transactions = []
    @property
    def balance(self):
        return self._balance

    def deposit(self,amount:float):
        if amount<=0:
            raise ValueError("mojodi kamtar az 0 hast")
        self._balance+=amount
        
        
        



    
