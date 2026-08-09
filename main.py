from banking.models import BankAccount
acc = BankAccount()
acc.deposit(500)

print(acc.balance)