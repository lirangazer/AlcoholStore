
from datetime import datetime

class Sale(object):
    """Sale the represent the invoice"""
    def __init__(self, invoice_number):
        """
        :param invoice_number: int: number of the invoice.
        """
        self.invoice_number = invoice_number
        now = datetime.now()
        date = now.strftime("%m/%d/%Y, %H:%M:%S")

    def __str__(self):
        return "Sale invoice number:\n" \
               "{0}, Date: {1}".format(self.invoice_number, self.date)
