class Address:
    
    def __init__(self, street, city, state, zip):
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zip = zip

    def __str__(self):
        return 'Address: {:s} {:s} {:s} {:s}'.format(self.__street, self.__city, self.__state, self.__zip)

class ShoppingCart:

    def __init__(self, number, addr):
        self.__store_num = number
        self.__addr = addr
        self.__products = []
        self.__next_products_index = 0

    def set_address(self, in_addr):
        self.__addr = in_addr

    def add_product(self, products):
        self.__products.append(products)

    def __str__(self):
        return 'Store #{:d} {:} List of products: {:}'.format(self.__store_num, self.__addr, self.__products)

    def __iter__(self):
         print("__iter__ is called")
         self.__next_products_index = 0
         return self

    def __next__(self):
        print("__next__ is called")
        if self.__next_products_index >= len(self.__products):
            print("in __next__, at end of iteration, raise StopIteration")
            raise StopIteration
        curr_index_to_return = self.__next_products_index
        self.__next_products_index += 1
        return self.__products[curr_index_to_return]
 
class Product:
    
    def __init__(self, id, desc, price):
        self.__id = id
        self.__desc = desc
        self.__price = price

    def __str__(self):
        return 'Product: {:d} {:s} {:}'.format(self.__id, self.__desc, self.__price)

    def __repr__(self):
        return self.__str__()

def main():

    ship = Address('345 King', 'Aldie', 'VA', '20167')
    cart = ShoppingCart(1024, ship)
    p1 = Product(123, 'Java I Book', 59.99)
    p2 = Product(345, 'Python II Book', 79.99)
    p3 = Product(567, 'C++ Book', 89.99)
    cart.add_product(p1)
    cart.add_product(p2)
    cart.add_product(p3)
    print(cart)

    for product in cart:
        print('product in cart is', product)

    for product in cart:
        print('product in cart is', product)

        
main()
