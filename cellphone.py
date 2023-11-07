class CellPhone:
    def __init__(self, manufact, model, price):
        self.__manufacturer = manufact
        self.__model = model
        self.__price = price
        
    def getManufacturer(self):
        return self.__manufacturer
    
    def getModel(self):
        return self.__model
    
    def getPrice(self):
        return self.__price
    
    def __str__(self):
        return self.getManufacturer() + " ," + self.getModel() + " ,$" + str(self.getPrice())
    
def main():
    phones = make_list()
    for phone in phones:
        print(phone)
    
def make_list():
    phone_list = []
    
    print("Enter the data for five phone: ")
    for count in range(1,6):
        print("Cell Phone ", count)
        man = input("Enter the manufacturer: ")
        model = input("Enter the model: ")
        price = float(input("Enter the price: "))
        
        phone = CellPhone(man, model, price)
        phone_list.append(phone)
        
    return phone_list

main()