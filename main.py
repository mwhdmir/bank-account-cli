from banking.models import BankAccount, SavingsAccount

def create_account():
    print("1. Standard Account")
    print("2. Savings Account")

    account_type = input("Choose account type: ")

    if account_type == "1":
        account_number = input("Enter account number: ")
        owner_name = input("Enter owner name: ")

        return BankAccount(account_number, owner_name)

    if account_type == "2":
        account_number = input("Enter account number: ")
        owner_name = input("Enter owner name: ")
        interest_rate = float(input("Enter interest rate: "))
        minimum_balance = float(input("Enter minimum balance: "))

        return SavingsAccount(
            account_number,
            owner_name,
            interest_rate,
            minimum_balance
        )




def main_menu(account):
    while True:
        print("\n--- Main Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. Check Balance")
        print("5. View Logs")
        print("6. Apply Interest")
        print("7. Exit")

        choice = input("Choose an option: ")
        if choice == "7":
            print("Goodbye!")
            break

account = create_account()
main_menu(account)