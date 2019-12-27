# I just found https://stackoverflow.com/questions/58591423/python-prints-escape-keys-while-entering-input-when-pressing-the-arrow-keys-on-t which is SUCH useful info to know! I thought 
# there was no way to keep out those nasty ^[[D's when trying to arrow around in a python input. 
# You bet your life I added `import readline`.

from product import Product
import sys, os, readline

products = []

options = """
view    --Shows all the products
see     --Lets you look at only a certain product
show    --Shows all possible commands
edit    --edit products
buy     --buys a product
delete  --Deletes a product
backup  --Backs up the current list of products
import  --Imports an already existing list of products"""



def buy(productsList, productNum, count):
    index = productNum - 1
    if productsList[index].inventory == '0':
        productsList.pop(index)
    elif count <= productsList[index].inventory:
        print('Bought '+ str(count) +' of "' + productsList[index].name+'"'+'.')
        for i in range(count):
            productsList[index].setInventory(productsList[index].inventory - 1)
        if productsList[index].inventory == 0:
            print('Your total is $' + str(round(count * productsList[index].price, 2)))
            productsList.pop(index)
            print('There are now no more of that product left.\n')
        else:
            print('There are now', productsList[index].inventory, 'left in stock.')
            print('Your total is $' + str(round(count * productsList[index].price, 2)) + '\n')
    else:
        print('Sorry, there are not that many of this product. There are only', str(productsList[index].inventory) + '.\n')

def backup():
    whatFile = input('Enter the file to backup to: ')
    if os.path.exists(whatFile):
        overWrite = input('There is already a file named ' + whatFile + '. Do you want to over-write it? ').lower()
        if overWrite[0] == 'y':
            fo = open(whatFile, 'w')
            for prod in products:
                fo.write((str(prod.name) + '\n' + str(prod.description) + '\n' + str(prod.price) + '\n' + str(prod.inventory)  + '\n'))
            fo.close()
            print('The product list was backed up to', whatFile + '.')
    else:
        new = input('There is no file named ' + whatFile + '. Would you like to create a new one? ')
        if new.lower()[0] == 'y':
            fo = open(whatFile, 'w')
            for prod in products:
                fo.write((str(prod.name) + '\n' + str(prod.description) + '\n' + str(prod.price) + '\n' + str(prod.inventory)  + '\n'))
            fo.close()
            print('The product list was backed up to a new file named', whatFile +'.')



try:
    while True:
        action = input('Press enter to add a product, type \'exit\' to end, or \'show\' to see all commands: ')
            
        if action == '':
            try:
                print()
                print('PRODUCT NUMBER', str(len(products) + 1))
                name = input('Name: ')
                desc = input('Description: ')
                price = float(input('Price: $'))
                inv = int(input('Quantity: '))
                print()
                products.append(Product(name, desc, price, inv))
            except KeyboardInterrupt:
                pass

        elif action == 'exit':
            backerup = input('Do you want to backup the product listing before you close? ').lower()
            if backerup[0] == 'y':
                backup()
                break
            else:
                break

        elif action == 'view':
            print()
            print('Showing', str(len(products)), 'products: ')
            prodNum = 1
            if len(products) == 0:
                print('\nRight now there are no products in stock. \n')
            for prod in products:
                print()
                print('PRODUCT NUMBER', str(prodNum) + ':') 
                print(prod)
                print()
                prodNum += 1
        
        elif action == 'show':
            print()
            print(options)
            print('\n')
        
        elif action == 'edit':
            try:
                index = int(input('Enter the product number to edit: '))
                index -= 1
                print('Editing '+'"' +products[index].name+'"'+'. Press enter to leave a field the same.')
                name = input('Name: ')
                desc = input('Description: ')
                price = input('Price: $')
                count = input('Quantity: ')
                if name != '':
                    products[index].setName(name)
                if desc != '':
                    products[index].setDescription(desc)
                if price != '':
                    products[index].setPrice(float(price))
                if count != '':
                    products[index].setInventory(int(count))
            except KeyboardInterrupt:
                pass

        elif action == 'buy':
            try:
                index = int(input('Enter the product number to buy: '))
                print('BUYING ' + '"'+(products[index - 1].name)+'"' + '...')
                count = int(input('How many would you like to buy? There are ' + str(products[(index - 1)].inventory) + ' left in stock: '))
                buy(products, index, count)
            except KeyboardInterrupt:
                pass

        
        elif action == 'see':
            try:
                which = (int(input('Which Product number would you see? ')) - 1)
                print()
                print('PRODUCT NUMBER', str(which + 1) + ':')
                print(products[which])
                print()
            except IndexError:
                print("You entered an invalid product number. There are only", len(products), "different products.")

        elif action == 'delete':
            which = int(input('Enter the Product Number you wish to delete: '))
            nameOfProduct = (products[which - 1].name)
            sure = input('Are you sure you want to delete ' + '"'+nameOfProduct+'"? ')
            if sure.lower()[0] == 'y':
                products.pop(which - 1)
                print('"'+nameOfProduct+'"', 'was deleted.\n')
            else:
                pass

        elif action == 'backup':
            backup()
        
        elif action == 'import':
            whatFile = input('Enter the file to import from: ')
            if os.path.exists(whatFile):
                file = open(whatFile, 'r')
                Textfile = file.read().split('\n')
                length = int(len(Textfile) / 4)

                for i in range(length):
                    products.append(Product(str(Textfile[0]), str(Textfile[1]), float(Textfile[2]), int(Textfile[3])))
                    for i in range(4):
                        Textfile.pop(0)
                print('The product list was imported from', whatFile + '.')
            else:
                print('Sorry, we see no file named', whatFile + '. Try again.')
                



except KeyboardInterrupt:
    backEmUP = input('\nDo you want to backup the product listing before you close? ').lower()
    if backEmUP[0] == 'y':
        backup()
    sys.exit()
