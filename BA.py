import sys
class bankacc:
    def __init__(self,login,menu,option,deposit,withdrawal,):
        self.login = login
        self.menu = menu
        self.option = option
        self.deposit = deposit
        self.withdrawal = withdrawal


balance = 500

def login():
    correct_username = "JOSHUA"
    correct_password = 1234

    number_of_tries = 1
    username = (input("\nEnter username: "))
    password = int(input("Enter password: "))
    max_num = 3
    while number_of_tries < max_num and correct_username != username and correct_password != password:
        username = (input("\nEnter username: "))
        password = int(input("Enter password: "))
        number_of_tries+=1
        if username == correct_username and password == correct_password:
            correct_username ="JOSHUA"
            correct_password = 1234

    if username==correct_username and password==correct_password:
        print("Welcome")
    else:
        print("Try again Later")
        sys.exit()

def menu():
    login()
    print("*"*50)
    print("\nWelcome to This ATM")
    print("\nChoose an option")
    print("\nPress 1 to deposit")
    print("\nPress 2 to withdrawal")
    print("\nPress 3 to exit")
    print("*"*50)

def option():
    menu()
    User_Option = int(input("Choose an option: "))
    if User_Option == 1:
        deposit()
    elif User_Option == 2:
        withdrawal()
    else:
        exit()

def deposit():
    dep = int(input("\nEnter deposit amount: "))
    new_bal = dep + balance
    print('Your new balance is GHc {}'.format(new_bal) )
    sys.exit()


def withdrawal():
    witd = int(input("\nEnter amount to withdraw: "))
    new_bal = balance - witd
    if witd > balance :
        print("You have insufficient funds in your account")
        print("\nPlease make a deposit.")
        sys.exit()

    else:
        print("Your account has been debited with GHc {}".format(witd))
        print('Your new balance is GHc {}'.format(new_bal))
        sys.exit()

def exit():
    print("Thank you for banking with us")
    sys.exit()


option()




