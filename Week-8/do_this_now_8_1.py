class Product:
    def __init__(self, name="", price=0.0, is_on_sale=False):
        self.name = name
        self.price = price
        self.is_on_sale = is_on_sale

    def __str__(self):
        return "{} ${:.2f}{}.".format(self.name, self.price, self.is_on_sale)

    def put_on_sale(self, discount):
        self.is_on_sale = True
        self.price -= self.price * discount

    def __gt__(self, other):
        return self.price > other.price

    def __getitem__(self, item):
        return self.name[item]

def run_test():
    product_one = Product("pen", 5)
    product_two = Product("pencil", 4)
    print(product_one < product_two)
    print(product_two[-1])


run_test()
