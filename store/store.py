
from common.root_logger import *

class Store(object):
    """Store object contains the data and the method of the store"""
    def __init__(self):
        """Creating list to store the data for the store"""
        self.drinks_in_store = []
        self.suppliers = []
        self.product_purchases_from_supplier = []
        self.product_sales = []
        self.buyers = []
        self.sales = []
        self.logger = get_logger()

    def sell_product(self, product_sale):

        item_exsit = False
        if product_sale.buyer.age < 18:
            self.logger.info("The buyer {0} is under age, {1}".format(product_sale.buyer.name, product_sale.buyer.age))

        product_id = product_sale.drink.catalog_id

        for i in range(len(self.drinks_in_store)):
            if self.drinks_in_store[i].catalog_id == product_id:
                if self.drinks_in_store[i].amount >= product_sale.amount:
                    self.drinks_in_store[i].amount -= product_sale.amount
                    self.product_sales.append(product_sale)
                    self.logger.info("Sold: {0} drinks of {1}".format(product_sale.amount, product_sale.drink.name))
                    item_exsit = True

                else:
                    self.logger.info("Not enough product\n"
                                     "The item {0} amount is: {1}".format(product_sale.drink.name, self.drinks_in_store[i].amount))
                    return

    def purchase_product_from_supplier(self, product_purchase):
        pass

    def display_drinks_in_store(self):
        pass

    def display_product_purchases_from_supplier(self):
        pass