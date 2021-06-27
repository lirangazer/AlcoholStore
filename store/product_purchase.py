
class ProductPurchase(object):
    def __init__(self, drink, supplier, purchase_details: str, amount: int) -> object:
        """
        :param dink: object: contains data regarding the drinks.
        :param supplier: object: contains data about the supplier.
        :param purchase_details: object contant data about the purchase.
        :param amount:
        """
        self.drink = drink
        self.supplier = supplier
        self.purchase_details = purchase_details
        self.amount = amount

    def __str__(self):
        return "Drink purchases form the supplier:\n" \
               "{0}\n" \
               "{1}\n" \
               "Product details: {2}\n" \
               "Amount: {3}".format(self.drink,self.supplier, self.purchase_details, self.amount)