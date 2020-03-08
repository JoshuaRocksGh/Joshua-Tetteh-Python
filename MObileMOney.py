import sys
class momo:
    def __init__(self,pin,balance,deposit,withdrawal):
        self.pin = pin
        self.balance = balance
        self.deposit = deposit
        self.withdrawal = withdrawal

balance = 3000,

def pin():
    correct_pin = 1234

    number_of_tries = 1
    pin = int(input("Enter Pin: "))
    max_num = 3
    while number_of_tries < max_num and correct_pin != pin:
        pin = int(input("Enter Pin: "))
        number_of_tries+=1
        if pin == correct_pin:
            correct_pin = 1234

    if pin == correct_pin:
        print("Welcome")
    else:
        print("Try again Later")
        sys.exit()

def menu():
    pin()
    print("*"*50)
    print("\nWelcome to MobileMoney")
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
    print('Your new balance is GHc {}'.format(new_bal))



def withdrawal():
    withd = int(input("Enter amount you wish to withdraw Ghc: "))
    if withd == 2000:
        print("Maximum limit reached")
    elif withd < 2000:
        print("Daily limit not reached")
        withdd = int(input("\nEnter amount you wish to withdraw Ghc: "))
        second = withd + withdd
        if second == 2000:
            print("Maximum limit reached")
            print("Your have withdrawn Ghc{} today".format(second))
            print("Thank you for uisng momo")
        elif second != 2000:
            x = 2000 - (withd + withdd)
            print("You can only withdraw Ghc{} ".format(x))
            int(input("\nWithdraw the remaining balance Ghc: "))
            print("Maximum limit reached")
            print("Thank you for using momo")
        else:
            print("Thank You for using MoMo")
            sys.exit()
    else:
        print("Thank You for using MoMo")
        sys.exit()

def exit():
    print("Thank You for using MoMo")
    sys.exit()

option()


