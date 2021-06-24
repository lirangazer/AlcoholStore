
class ProductPurchase(object):
    def __init__(self, dink, supplier, purchase_details: str, amount: int) -> object:
        """
        :param dink: object: contains data regarding the drinks.
        :param supplier: object: contains data about the supplier.
        :param purchase_details: object contant data about the purchase.
        :param amount:
        """
        self.dink = dink
        self.supplier = supplier
        self.purchase_details = purchase_details
        self.amount = amount

    def __str__(self):
        return "Drink purchases form the supplier:\n" \
               "{0}\n" \
               "{1}\n" \
               "{2}\n" \
               "{3}".format(self.dink,self.supplier, self.purchase_details, self.amount)