class Product:
    
    def __init__(self, name, desc, price, inv):
        self.setDescription(desc)
        self.setInventory(inv)
        self.setPrice(price)
        self.setName(name)

    def __str__(self):
        return 'Name: ' + self.name + '\nDescription: ' + self.description + '\nPrice: $' + str(self.price) + '\nInventory: '+ str(self.inventory)

    def setName(self, name):
        self.name = name
    def setDescription(self, desc):
        self.description = desc

    def getDescription(self):
        return self.description

    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price

    def setInventory(self, inv):
        self.inventory = inv
    
    def getInventory(self):
        return self.inventory
