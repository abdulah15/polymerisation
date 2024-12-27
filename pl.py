class price:   
    def __init__(self):
        self.__price = 1000
    def display(self):
        print("The amount is ",self.__price)
    def setprice(self,price):
        self.__price = price
    
obj = price()
obj.display()
obj.setprice(2000)
obj.display()

