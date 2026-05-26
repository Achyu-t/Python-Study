def show_balance(x):
    print(f"Your balance is {x}")

def withdraw(z):
    amount = float(input("Enter amount you want to withdraw: "))
    z -= amount
    return z

def deposit(y):
    amount = float(input("Enter amount you want to deposit: "))
    y += amount
    return y

def main():

    balance = 0

    while True:

        print("--------------Welcome to Money Bank--------------")
        print("Select an Operation: ")
        print("1. Show Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Quit")
        print('-----------------------------------------------------')

        transaction = input("Enter number equivalent to your choice: ")

        match transaction :
            case '1':
                show_balance(balance)
            case '2':
                balance = deposit(balance)
            case '3':
                balance = withdraw(balance)
            case '4':
                break

        if input("Do you want to perform other transactions? Press Y for yes:").lower() != 'y':
            break

if __name__ == "__main__":
    main()

