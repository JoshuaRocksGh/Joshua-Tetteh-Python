class Temperature:
    def __init__(self, value):
        self.temperature = value
        #print(self.temperature)

    def Celsius_to_Fahrenheit(self):
        print((self.temperature - 32)*5/9)

    def Farenheit_to_Celsius(self):
        print((self.temperature * 9/5)+32)

c = Temperature(100)
c.Farenheit_to_Celsius()
print(c.temperature)








