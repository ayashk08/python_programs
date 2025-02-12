class ShoppingCart:
    sname = 'MY Icare'
    stock = {
        'iphone13': 35,
        'iphone14': 25,
        'iphone15': 15,
        'iphone13promax': 5,
        'iphone14promax': 5,
        'iphone15promax': 5,
        'ipadmini': 25,
        'ipadpro': 20,
        'ipadair': 15
    }
    price = {
        'iphone13': 62000,
        'iphone14': 72948,
        'iphone15': 87349,
        'iphone13promax': 115345,
        'iphone14promax': 132489,
        'iphone15promax': 157942,
        'ipadmini': 30421,
        'ipadpro': 43741,
        'ipadair': 57265
    }

    def __init__(self, name, pno, email, add):
        self.name = name
        self.pno = pno
        self.email = email
        self.add = add
        self.cart = {}

    def additem(self, item, count=1):
        if self.stock[item] >= count:
            if item in self.stock:
                if item in self.cart:
                    self.cart[item] += count
                else:
                    self.cart[item] = count
                ShoppingCart.stock[item] -= count
            else:
                print('Sorry !..Product not available')
        else:
            print('sorry the stock is not as much you expected')
            print(f"The Available stock of {item} is : {self.stock[item]}units")


c1 = ShoppingCart('likith', 8179267926, 'likith@gmail.com', 'lpk')