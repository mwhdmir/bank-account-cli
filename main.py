from banking.models import BankAccount

account1 = BankAccount("1001", "Ali")
account2 = BankAccount("1002", "Sara")

account1.deposit(1000)

account1.transfer(300, account2)

print("Account 1 balance:", account1.balance)
print("Account 2 balance:", account2.balance)

print("Account 1 transactions:")
for transaction in account1._transactions:
    print(transaction)

print("Account 2 transactions:")
for transaction in account2._transactions:
    print(transaction)