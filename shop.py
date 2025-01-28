# set up the shop items and prices, and other variables
class Shop:
    def __init__(self):
        self.products = ["shirt","pants","T-shirt","shoes"]
        self.price = [20.00 , 45.00 , 25.00 , 99.99]
        self.total= 0

# print the name of your shop

    def displayShopName(self):
         print("Elizabeth's Shop")

# print all of the items and their prices

# HINT use a for loop

    def printItemsAndPrices (self):
        self.price
        for i in range (len(self.price)):
            print(self.products[i], self.price[i])
            

# add cost of item to the total

    def buy(self, item):
        idx = self.products.index(item)
        cost = self.price[idx]
        self.total += cost
        print(input(self.total))
        

    def getTotal(self):
        self.total += self.price
        

s = Shop()
s.displayShopName()
s.printItemsAndPrices()
s.buy

