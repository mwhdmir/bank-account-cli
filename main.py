from banking.models import SavingsAccount

account = SavingsAccount("2001", "Ali", 0.05, 500)

account.deposit(1000)

print("Before interest:", account.balance)

account.apply_interest()

print("After interest:", account.balance)
print(account.get_transaction_history())