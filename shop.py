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
      for i in range (3):
        print(self.products[i], self.price[i])

      
       # self.price
       # for i in range (len(self.price)):
          #  print(self.products[i], self.price[i])
            

# add cost of item to the total

    def buy(self, item):
        idx = self.products.index(item)
        cost = self.price[idx]
        self.total += cost
        

    def getTotal(self):
        return self.total
        
        #self.total += self.price

        

s = Shop()
s.displayShopName()
s.printItemsAndPrices()
punch = input("What type of items are you looking for?")

while punch !="None":
    s.buy(punch)
    s.displayShopName()
    s.printItemsAndPrices()
    punch = input("What type of items are you looking for?")



print(s.getTotal())
    
