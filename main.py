from banking.models import BankAccount

account1 = BankAccount("1001", "Ali")
account2 = BankAccount("1002", "Sara")

account1.deposit(1000)
account1.withdraw(200)
account1.transfer(300, account2)

print("Account 1 history:")

for log in account1.get_transaction_history():
    print(log)

print("\nAccount 2 history:")

for log in account2.get_transaction_history():
    print(log)