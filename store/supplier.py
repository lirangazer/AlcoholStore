

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