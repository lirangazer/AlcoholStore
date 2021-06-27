

class Supplier(object):
    def __init__(self, name, address, id, phone):
        """
        :param name: str: name of the supplier
        :param address: str: Address of the supplier
        :param id: int: id of the supplier in the store
        :param phone: int: the supplier phone.
        """
        self.phone = phone
        self.id = id
        self.address = address
        self.name = name

    def __str__(self):
        return "Supplier info:\n" \
               "name: {0}, id: {1}, address: {2}, phone: {3}".format(self.name, self.id, self.address,self.phone,)