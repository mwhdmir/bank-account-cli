from banking.models import BankAccount

acc = BankAccount()

try:
    acc.withdraw(-50)
except Exception as e:
    print(type(e).__name__)
    print(e)