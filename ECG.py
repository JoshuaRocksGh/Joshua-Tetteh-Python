import random

Customer = input("\nEnter Customers Name: ")
Meter = {"ReceiptCode": " ", "Customer Acc NO": " ", "Meter NO":" ", "Consumption":" "}

def customer():
    Meter["ReceiptCode"] = random.randint(0, 10000000)
    Meter["Customer Acc NO"] = random.randint(0, 999999)
    Meter["Meter NO"] = random.randint(0, 1000)
    Meter["Consumption"] = random.randint(0, 999)

customer()
print("\nHello {}!".format(Customer))
print("Your Acc NO is {} and Meter NO is {}".format(Meter.get("Customer Acc NO", " "), Meter.get("Meter NO", " ")))


def charges():
    print('\nYour monthly consumption is {} KWH'.format(Meter.get("Consumption"," ")))
    month = Meter.get("Consumption"," ")
    rate = 0.5
    charge = month * rate
    print("Amount Due is GHc {}".format(charge))
    print("\nThank You {}, your reciept no is {}".format(Customer, Meter.get("ReceiptCode"," ")))

charges()