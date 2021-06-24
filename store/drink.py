

class Drink(object):
    """Object represent Drink in the store"""
    def __init__(self, type: str, name: str, catalog_id: int, price: int, amount: int) -> object:
        """
        :param type: drink type
        :param name: name of the drink
        :param catalog_id: id of the drink
        :param price: price of the drink
        :param amount: amount from this drink
        """
        self.type = type
        self.name = name
        self.catalog_id = catalog_id
        self.price = price
        self.amount = amount

    def __str__(self):
        """Over-ride the str() function"""
        return 'Drink info:\n' \
               'Name: {0}, Type: {1}, Catalog ID: {2}, Price: {3}, Amount: {4}'.format(self.type, self.name, self.catalog_id, self.price, self.amount)
