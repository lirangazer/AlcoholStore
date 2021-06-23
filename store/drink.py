

class Drink(object):
    """Object represent Drink in the store"""
    def __init__(self, type, name, catalog_id, price, amount):
        self.type = type
        self.name = name
        self.catalog_id = catalog_id
        self.price = price
        self.amount = amount

    def __str__(self):
        """Over-ride the str() function"""
        return 'Drink info:\n' \
               'Name: {0}, Type: {1}, Catalog ID: {2}, Price: {3}, Amount: {4}'.format(self.type, self.name, self.catalog_id, self.price, self.amount)
