
class Buyer(object):
    def __init__(self, name: str, id: int, phone: int, age: int) -> object:
        self.name = name
        self.id = id
        self.phone = phone
        self.age = age

    def __str__(self):
        return "Buyer Info:\n" \
               "Name: {0}, Id: {1}, Phone: {2}, Age: {3}".format(self.name, self.id, self.phone, self.age)

