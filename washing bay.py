import random
from datetime import date

Attendant = input("\nEnter Attendants's name:  ")
Bay = {"AttendantID":" ", "CarsWashed":" ", "Date":" "}

def Attndt():
    Bay["AttendantID"] = random.randint(1, 99)
    Bay["CarsWashed"] = random.randint(1,30)
    Bay["Date"] = date.today()

Attndt()
#print(Attendant)
#print(Bay)

def sales():
    print("\n{} washed {} cars on {}".format(Attendant, Bay.get("CarsWashed"," "), Bay.get("Date"," ")))
    day = Bay.get("CarsWashed"," ")
    rate = 10
    comprct = 0.30
    earned = day * rate * comprct
    print("\n{} commission for {} is GHc {}".format(Attendant,Bay.get("Date"," "), earned))

sales()