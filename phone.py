from item import Item

class Phone(Item):

    def __init__(self, name:str, price:float, quantity = 0, broken_phones = 0):
        #call to super function
        super().__init__(
            name, 
            price, 
            quantity)
        #run validation
        assert broken_phones >= 0, f"broken phones {broken_phones} is not greater or equal to zero"

        self.broken_phones = broken_phones


