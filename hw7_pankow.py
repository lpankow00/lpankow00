class ShippingCharges:
    def __init__(self, companyName=None, username=None, packages=0, weight=0, total=0, List=[]):
        self.__companyName = companyName
        self.__username = username
        self.__packages = packages
        self.__weight = weight
        self.__total = total
        self.__List = List
    def PackageCharge(self):
        self.__companyName = input("Enter company name: ")
        self.__username = input("Enter name: ")
        answer = "y"
        while (answer == "y"):
            self.__weight = eval(input("Please enter your package weight in pounds: "))
            if self.__weight <= 2:
                self.__weight = self.__weight * 1.10
                self.__total = self.__total + self.__weight
                self.__List.append(self.__weight)
            elif self.__weight > 2 and self.__weight <= 6:
                self.__weight = self.__weight * 2.20
                self.__total = self.__total + self.__weight
                self.__List.append(self.__weight)
            elif self.__weight > 6 and self.__weight <= 10:
                self.__weight = self.__weight * 3.70
                self.__total = self.__total + self.__weight
                self.__List.append(self.__weight)
            elif self.__weight > 10:
                self.__weight = self.__weight * 3.80
                self.__total = self.__total + self.__weight
                self.__List.append(self.__weight)
            answer = input("Would you like to enter another package? <y/n>: ")

    def getCompanyName(self):
        return self.__companyName
    def setCompanyName(self):
        self.__companyName = companyName
    
    def getUsername(self):
        return self.__username
    def setUsername(self):
        self.__username = username
    
    def getPackages(self):
        return self.__packages
    def setPackages(self):
        self.__packages = packages

    def getWeight(self):
        return self.__weight
    def setWeight(self):
        self.__weight = weight

    def getTotal(self):
        return self.__total
    def setTotal(self):
        self.__total = total

    def displayShippingCharges(self):
        print("Company Name:", self.__companyName)
        print("User:", self.__username)
        print("Number of Packages:", len(self.__List))
        print("Total weight of packages:", sum(self.__List))
        print("Total package cost charges: %.2f" % self.__total)
        
def main():
    default = ShippingCharges()
    default.displayShippingCharges()

    print(" ")

    hardCode = ShippingCharges("College of Dupage", "Luke Pankow", 10, 500, 8.500)
    hardCode.displayShippingCharges()



    print(" ")

    userInput = ShippingCharges()
    userInput.PackageCharge()
    userInput.displayShippingCharges()


main()

