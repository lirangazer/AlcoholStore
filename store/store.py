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
        return_flag = 0
        item_exist = False
        if product_sale.buyer.age < 18:
            self.logger.info("The buyer {0} is under age, {1}".format(product_sale.buyer.name, product_sale.buyer.age))
            return return_flag

        product_id = product_sale.drink.catalog_id

        for i in range(len(self.drinks_in_store)):
            if self.drinks_in_store[i].catalog_id == product_id:
                if self.drinks_in_store[i].amount >= int(product_sale.amount):
                    self.drinks_in_store[i].amount -= product_sale.amount
                    self.product_sales.append(product_sale)
                    self.logger.info("Sold: {0} drinks of {1}".format(product_sale.amount, product_sale.drink.name))
                    item_exist = True

                else:
                    self.logger.info("Not enough product\n"
                                     "The item {0} amount is: {1}".format(product_sale.drink.name,
                                                                          self.drinks_in_store[i].amount))
                    return_flag = 1
                    return return_flag

        if not item_exist:
            self.logger.info("The item: {0} is not exist in the stock".format(product_sale.drink.name))
            return_flag = 2
            return return_flag

        for sale in self.sales:
            if sale.invoice_number == product_sale.sale.invoice_number:
                return

        self.sales.append(product_sale.sale)

    def product_purchase_from_supplier(self, product_purchase):
        if len(self.drinks_in_store) == 0:
            self.drinks_in_store.append(product_purchase.drink)
        else:
            flag = 0
            for i in self.drinks_in_store:
                if i.catalog_id == product_purchase.drink.catalog_id:
                    i.amount += product_purchase.amount
                    flag = 1
                    break
                else:
                    continue
            if flag == 0:
                self.drinks_in_store.append(product_purchase.drink)


        # for i in range(len(self.drinks_in_store)):
        #     if self.drinks_in_store[i].catalog_id == product_purchase.drink.catalog_id:
        #         self.drinks_in_store[i].amount += product_purchase.amount
        #         break
        #

        self.product_purchases_from_supplier.append(product_purchase)
        self.logger.info("{0} {1} has been purchased".format(product_purchase.amount, product_purchase.drink.name))

    def display_drinks_in_store(self):

        for drink in self.drinks_in_store:
            self.logger.info("The drinks in store are:\nType: {0}, Name: {1}, id: {2}, price: {3}, amount: {4}"
                             .format(drink.type, drink.name, drink.catalog_id, drink.price, drink.amount))

    def display_product_purchases_from_supplier(self):

        for purchase in self.product_purchases_from_supplier:
            self.logger.info(purchase)
