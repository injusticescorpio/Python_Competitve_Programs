class Computer:
    def __init__(self, ram=None, hdd=None, prsr=None, os=None):
        self.ram = ram
        self.hdd = hdd
        self.prsr = prsr
        self.os = os

    def getspecs(self):
        self.ram = input("Enter RAM size:")
        self.hdd = input("Enter HDD size:")
        self.prsr = input("Enter processor name")
        self.os = input("Enter OS name")

    def displayspecs(self):
        print(self.ram)
        print(self.hdd)
        print(self.prsr)
        print(self.os)

class Desktop(Computer):
    def __init__(self):
        super().__init__(self.ram, self.hdd, self.prsr, self.os)

    def getspecs(self):
        self.power_supply = input("Enter the power supply in Watts")

    def displayspecs(self):
        print(self.power_supply)
        print(self.ram)
        print(self.hdd)
        print(self.prsr)
        print(self.os)




c=Computer()
c.getspecs()
d=Desktop()
d.getspecs()
d.displayspecs()