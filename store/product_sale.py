
class ProductSale(object):
    def __init__(self, amount, sale, drink, buyer):
        """
        :param amount: int: amount of procut that saled.
        :param sale: object sale contains data about the sale.
        :param drink: object: contains data regarding the drinks.
        :param buyer: object: contains the data about the buyer
        """
        self.drink = drink
        self.sale = sale
        self.amount = amount
        self.buyer = buyer

    def __str__(self):
        return "Invoice:\n" \
               "{0}\n" \
               "{1}\n" \
               "{2}\n" \
               "{3}".format(self.drink, self.sale,self.buyer, self.amount)

